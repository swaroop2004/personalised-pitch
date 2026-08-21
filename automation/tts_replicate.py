#!/usr/bin/env python3
"""Cloud TTS: generate per-scene narration WAVs via Replicate Chatterbox.

Contract with the daily-pitch agent:
  - Input:  pitches/<slug>/audio/scene-NN.txt   (one plain-text narration per scene)
  - Output: pitches/<slug>/audio/scene-NN.wav   (chunked, trimmed, concatenated)

Env:
  REPLICATE_API_TOKEN   required
  CHATTERBOX_MODEL      default: resemble-ai/chatterbox
  EXAGGERATION          default: 0.5
  CFG_WEIGHT            default: 0.5
  TEMPERATURE           default: 0.8
  SEED                  default: YYYYMMDD-derived int

Usage: python automation/tts_replicate.py pitches/<slug>
"""

import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
import urllib.error
from pathlib import Path

API_URL = "https://api.replicate.com/v1/models/{model}/predictions"
MAX_CHUNK = 300
POLL_SECONDS = 2
POLL_TIMEOUT = 300

SENTENCE_RE = re.compile(r"(?<=[.!?…])\s+")


def die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def env_float(name: str, default: float) -> float:
    return float(os.environ.get(name, default))


def run_ffmpeg(args: list[str], what: str) -> None:
    proc = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        die(f"ffmpeg failed ({what}): {proc.stderr.strip()[:500]}")


def prepare_reference(ref_path: Path, tmp: Path) -> str:
    """Downmix reference to 24kHz mono WAV and return as data URI."""
    if not ref_path.exists():
        die(f"voice reference not found at {ref_path}")
    norm = tmp / "reference-normalized.wav"
    run_ffmpeg(["-i", str(ref_path), "-ar", "24000", "-ac", "1",
                "-c:a", "pcm_s16le", str(norm)], "normalize reference audio")
    b64 = base64.b64encode(norm.read_bytes()).decode()
    return f"data:audio/wav;base64,{b64}"


def chunk_text(text: str) -> list[str]:
    sentences = [s.strip() for s in SENTENCE_RE.split(text.replace("\n", " ")) if s.strip()]
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        if current and len(current) + 1 + len(sentence) > MAX_CHUNK:
            chunks.append(current)
            current = sentence
        else:
            current = f"{current} {sentence}".strip()
    if current:
        chunks.append(current)
    return chunks


def replicate_predict(model: str, token: str, input_data: dict, what: str) -> str:
    body = json.dumps({"input": input_data}).encode()
    req = urllib.request.Request(
        API_URL.format(model=model), data=body, method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Prefer": "wait",
        })
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:800]
        die(f"Replicate rejected request for {what} (HTTP {e.code}). "
            f"If this is a 422, check the model's input field names. Body: {detail}")
    except urllib.error.URLError as e:
        die(f"cannot reach Replicate for {what}: {e}")

    deadline = time.time() + POLL_TIMEOUT
    while payload.get("status") not in ("succeeded", "failed", "canceled"):
        if time.time() > deadline:
            die(f"Replicate prediction for {what} timed out after {POLL_TIMEOUT}s")
        time.sleep(POLL_SECONDS)
        poll = urllib.request.Request(payload["urls"]["get"],
                                      headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(poll, timeout=30) as resp:
                payload = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            die(f"polling failed for {what}: HTTP {e.code}")

    if payload.get("status") != "succeeded":
        die(f"prediction for {what} ended with status={payload.get('status')}: "
            f"{str(payload.get('error'))[:500]}")

    output = payload.get("output")
    if isinstance(output, list):
        output = output[-1] if output else None
    if not output or not isinstance(output, str):
        die(f"unexpected output shape for {what}: {str(output)[:200]}")
    return output


def download(url: str, dest: Path, what: str) -> None:
    try:
        with urllib.request.urlopen(url, timeout=120) as resp, open(dest, "wb") as fh:
            fh.write(resp.read())
    except urllib.error.URLError as e:
        die(f"failed downloading audio for {what}: {e}")


def synth_scene(txt_path: Path, out_wav: Path, ref_uri: str, opts: dict, seed: int,
                scratch: Path) -> None:
    scene = txt_path.stem
    text = txt_path.read_text(encoding="utf-8").strip()
    if not text:
        die(f"{txt_path.name} is empty")
    chunks = chunk_text(text)
    print(f"  {scene}: {len(chunks)} chunk(s), {len(text)} chars")

    chunk_files: list[Path] = []
    for i, chunk in enumerate(chunks):
        what = f"{scene} chunk {i + 1}/{len(chunks)}"
        url = replicate_predict(
            opts["model"], opts["token"],
            {"text": chunk, "audio_prompt_path": ref_uri,
             "exaggeration": opts["exaggeration"], "cfg_weight": opts["cfg_weight"],
             "temperature": opts["temperature"], "seed": seed},
            what)
        raw = scratch / f"{scene}-{i:02d}-raw.wav"
        download(url, raw, what)
        trimmed = scratch / f"{scene}-{i:02d}.wav"
        # Trim trailing breath/silence artifact documented in voice-setup.md
        run_ffmpeg(["-i", str(raw),
                    "-af", "silenceremove=stop_periods=1:stop_threshold=-45dB,"
                           "areverse,silenceremove=stop_periods=1:stop_threshold=-45dB,"
                           "areverse",
                    "-c:a", "pcm_s16le", str(trimmed)], f"trim {what}")
        raw.unlink()
        chunk_files.append(trimmed)

    if len(chunk_files) == 1:
        run_ffmpeg(["-i", str(chunk_files[0]), "-c:a", "pcm_s16le", str(out_wav)],
                   f"finalize {scene}")
    else:
        listing = scratch / f"{scene}-list.txt"
        listing.write_text("".join(f"file '{f}'\n" for f in chunk_files), encoding="utf-8")
        run_ffmpeg(["-f", "concat", "-safe", "0", "-i", str(listing),
                    "-c:a", "pcm_s16le", str(out_wav)], f"concat {scene}")
    print(f"  -> {out_wav}")


def main() -> None:
    if len(sys.argv) != 2:
        die("usage: tts_replicate.py <pitch-dir>")
    pitch_dir = Path(sys.argv[1])
    audio_dir = pitch_dir / "audio"
    scenes = sorted(audio_dir.glob("scene-*.txt"))
    if not scenes:
        die(f"no scene-NN.txt files in {audio_dir}")

    token = os.environ.get("REPLICATE_API_TOKEN")
    if not token:
        die("REPLICATE_API_TOKEN is not set")

    seed = int(os.environ.get("SEED") or time.strftime("%Y%m%d"))
    opts = {
        "model": os.environ.get("CHATTERBOX_MODEL", "resemble-ai/chatterbox"),
        "token": token,
        "exaggeration": env_float("EXAGGERATION", 0.5),
        "cfg_weight": env_float("CFG_WEIGHT", 0.5),
        "temperature": env_float("TEMPERATURE", 0.8),
    }

    with tempfile.TemporaryDirectory(prefix="tts-replicate-") as tmp_name:
        scratch = Path(tmp_name)
        ref_uri = prepare_reference(Path("voice/reference.wav"), scratch)
        for txt_path in scenes:
            out_wav = audio_dir / f"{txt_path.stem}.wav"
            synth_scene(txt_path, out_wav, ref_uri, opts, seed, scratch)

    print(f"OK: generated {len(scenes)} scene WAV(s) in {audio_dir}")


if __name__ == "__main__":
    main()
