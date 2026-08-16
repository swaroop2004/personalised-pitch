# Voice cloning setup — Chatterbox TTS (local)

Chosen model: **Chatterbox** by Resemble AI — MIT license (code AND weights, commercial
use OK), zero-shot cloning from ~10 s of audio, community-consensus most natural local
TTS (breath intakes, hesitation beats, micro pitch inflections). Repo:
https://github.com/resemble-ai/chatterbox

Model strategy — pick per machine (`model.repo_id` in `chatterbox-server/config.yaml`):
- **GPU machine**: `chatterbox` (original 500M) — maximum quality. This is what
  `config.yaml` in this repo is set to. Fast on any recent NVIDIA card.
- **CPU-only machine**: `chatterbox-turbo` (350M) — near-original quality, roughly
  realtime to ~2–5 min per minute of audio on CPU. Nano (110M) for drafts only.
- **Tag support differs**: Turbo/Nano support paralinguistic tags (`[laugh]`,
  `[chuckle]`, `[cough]`, `[sigh]`); the **original model does NOT** — with
  `repo_id: chatterbox` it will read tags aloud, so keep them out of scripts and
  write breaths/hesitations with punctuation instead ("um…", em-dashes, ellipses).

## Recording the reference sample (`voice/reference.wav`)

- 10–20 seconds, quiet room, phone/laptop mic at consistent distance.
- Speak NATURALLY — conversational energy, not "announcer voice". The clone copies the
  delivery style of the sample, so include normal pauses and inflection.
- WAV or MP3, mono. Avoid background music, clipping, echo.

## Server: devnen/Chatterbox-TTS-Server (OpenAI-compatible HTTP API)

Repo: https://github.com/devnen/Chatterbox-TTS-Server

The server is vendored in this repo at `chatterbox-server/` (its Python environment and
model weights are gitignored — first launch on a new machine sets both up). Install via
its launcher, which auto-detects hardware and installs the matching PyTorch build:
- Windows: `chatterbox-server\start.bat` (offers a portable embedded-Python env)
- Linux/macOS: `cd chatterbox-server && python3 start.py`
- Skip the interactive menu with flags: `--nvidia` (CUDA 12.1, RTX 20/30/40),
  `--nvidia-cu128` (RTX 50 series), `--rocm` (AMD), `--cpu`.
Model weights download from Hugging Face on first run (a few GB, one time).
`config.yaml` ships with `device: auto`, so a CUDA GPU is used when present.

Setup steps:
1. Copy the user's sample into the server's `reference_audio/` folder as `user.wav`.
2. Start the server (run `start.bat` via a background shell task; first launch is slow
   while weights download). Default port is shown in its console output (typically 8004).
3. **Verify the exact request schema at runtime**: fetch `http://localhost:<port>/docs`
   (FastAPI OpenAPI page) — don't guess field names from memory. It exposes both a
   native `/tts` endpoint (full control: reference audio file, `temperature`,
   `exaggeration`, `cfg_weight`, `speed_factor`, `seed`) and an OpenAI-compatible
   `/v1/audio/speech`.
4. Smoke test with one short sentence, save to the scratchpad, and have the user listen
   before batch-generating scenes.

Fallback server: https://github.com/travisvn/chatterbox-tts-api (`DEVICE=cpu`,
OpenAI-compatible, uv/pip/Docker). MCP option exists (digitarald/chatterbox-mcp) but
the HTTP servers are more robust — plain curl from Claude Code works fine.

## Generation settings & script rules (Chatterbox-specific)

- **Chunk the script**: 1–3 sentences per request. Long texts drift. Generate per-scene,
  and within a scene split on paragraph breaks, then concatenate with ffmpeg.
- **Fix the seed** once a take sounds right, so regenerated neighbours stay consistent.
- `exaggeration` ~0.4–0.6 for narration (higher = more dramatic); default `cfg_weight`
  ~0.5; lower cfg slightly if pacing sounds rushed.
- Scripted imperfections render well: "um…", "y'know", em-dashes, ellipses. Paralinguistic
  tags (Turbo/Nano only — never with the original model) sparingly: one `[chuckle]` per
  pitch, max.
- Known artifact: occasional trailing breath/silence at clip ends — trim with
  `ffmpeg -af silenceremove=stop_periods=1:stop_threshold=-45dB` or `areverse,silenceremove,areverse`.
- Outputs carry Resemble's inaudible Perth watermark (disclosure feature, not a
  restriction).

## Verified server usage (first verified 2026-08-15, CPU laptop)

- Server lives at `chatterbox-server/`; port **8004** (set in `config.yaml`).
- On a fresh machine: run the launcher (above), then copy `voice/reference.wav` to
  `chatterbox-server/reference_audio/user.wav` — reference audio is gitignored, so
  this copy is a required setup step after every clone.
- Configured engine is **chatterbox** (original 500M, max quality — no paralinguistic
  tags). Weights cache to `~/.cache/huggingface/hub/`, downloaded once.
- Check status: `GET /api/model-info` (`loaded: true` before generating).
  Restart after config changes: `POST /restart_server` (times out as it restarts —
  that's normal; poll model-info after).
- Working `/tts` request body: `{"text", "voice_mode": "clone",
  "reference_audio_filename": "user.wav", "output_format": "wav", "exaggeration",
  "cfg_weight", "seed"}`. Server chunks long text itself (`split_text`, default on).

### Troubleshooting: "paging file is too small" (OS error 1455) on model load

Seen on low-RAM Windows machines (16 GB, often <1 GB free) with tight C: disk space.
If the model fails to load with error 1455: free disk space on C: (pip cache purge is the
easy ~2.5 GB win; the auto-managed pagefile needs room to grow), ask the user to close
heavy apps, then `POST /restart_server`. Keep C: free space above ~5 GB before starting
generation batches.

## If Chatterbox is too slow/heavy on a CPU-only machine

Runner-up: **NeuTTS Air** (https://github.com/neuphonic/neutts) — Apache 2.0, 748M GGUF
via llama-cpp-python, realtime-or-faster on laptop CPUs in ~2–3 GB RAM, clones from
3–15 s. No off-the-shelf server: wrap its Python API in a ~20-line FastAPI shim.
(Its Nano/2E variants use a revenue-capped license — prefer Air, which is pure Apache.)

Licensing note: do NOT substitute F5-TTS, Fish Speech/OpenAudio, or IndexTTS-2 —
non-commercial weight licenses, unusable for business pitches.
