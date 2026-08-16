# personalised-pitch

Claude Code project that builds personalised outreach pitch videos end-to-end:
research a target company → find a docs gap Manicule can fill → Excalidraw visuals →
narration script → voice-cloned audio (local Chatterbox TTS) → assembled pitch video.

Everything is driven by the `personalised-pitch` skill — open this repo in Claude Code
and say `pitch <company>` or `build a pitch for <url>`.

## Layout

| Path | What it is |
|---|---|
| `.claude/skills/personalised-pitch/` | The skill: workflow, voice-setup reference, video-assembly scripts |
| `profile.md` | Sender profile (Manicule) used for pitch voice and proof points |
| `voice/reference.wav` | Voice-clone reference sample |
| `chatterbox-server/` | Vendored [devnen/Chatterbox-TTS-Server](https://github.com/devnen/Chatterbox-TTS-Server) (OpenAI-compatible local TTS, MIT) |
| `pitches/<company>/` | One folder per pitch: research, gap, script, audio, visuals, final `pitch.mp4` |

## Setup on a new machine

Prereqs: Python 3.10+, ffmpeg, Claude Code.
(macOS: `brew install python ffmpeg`; Windows: winget/installer; Linux: apt/dnf.)

1. Clone the repo.
2. Install the TTS server — its launcher auto-detects your hardware and installs the
   matching PyTorch build:
   - Windows: run `chatterbox-server\start.bat`
   - Linux/macOS: `cd chatterbox-server && python3 start.py`
   - Non-interactive: pass `--nvidia` (CUDA 12.1, RTX 20/30/40), `--nvidia-cu128`
     (RTX 50 series), `--rocm` (AMD), or `--cpu`.
   - **macOS**: choose the default/CPU install when prompted (or pass `--cpu`) —
     the standard macOS PyTorch build includes MPS (Metal GPU) support, and on
     Apple Silicon the server auto-selects MPS at runtime. The launcher also
     auto-applies an MPS float32 compatibility patch, so use the launcher rather
     than a manual `pip install`. Intel Macs run on CPU.
3. First launch downloads model weights from Hugging Face (a few GB, one time) and
   starts the server on port **8004**.
4. Copy the voice reference into the server (reference audio is gitignored):
   - `voice/reference.wav` → `chatterbox-server/reference_audio/user.wav`
5. Smoke test: `GET http://localhost:8004/api/model-info` should report `loaded: true`,
   then generate one short sentence via `/tts` before batch work.

## Model / quality configuration

`chatterbox-server/config.yaml` is set to the **maximum-quality model**
(`model.repo_id: chatterbox`, the original 500M) and `device: auto`, which resolves
CUDA → MPS (Apple Silicon) → CPU automatically.

- On an NVIDIA box or Apple Silicon Mac this is the right setting — best quality.
- On a CPU-only box (including Intel Macs), switch to `repo_id: chatterbox-turbo`
  for ~near-original quality at usable speed.
- Note: the original model does **not** support paralinguistic tags (`[laugh]`,
  `[sigh]`, …) — scripts must express those with punctuation. Turbo does support tags.

Full details, generation settings, and troubleshooting:
`.claude/skills/personalised-pitch/references/voice-setup.md`.
