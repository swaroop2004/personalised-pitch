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

## Daily cloud automation

A GitHub Actions workflow (`.github/workflows/daily-pitch.yml`) builds one pitch per
day, fully unattended — no approvals, no local machine. **Scope for now is text-only:
research, gap analysis, narration script, and storyboarded scene JSONs** (voice/video
disabled until enabled).

1. **Discover** — picks a funded D2C/e-commerce brand from the last ~45 days of funding
   news, skipping anything already under `pitches/` or in `automation/history.txt`.
2. **Build** — runs skill phases 1–4 headless via `opencode run --agent daily-pitch
   --auto` (agent definition: `.opencode/agent/daily-pitch.md`). Also emits
   `audio/scene-NN.txt` narration files so voice can be generated later without a re-run.
3. **Ship** — commits `pitches/<brand>/` to master, uploads research/gap/script +
   scene JSONs as a workflow artifact, and writes `automation/LAST_RUN.md`.

Schedule: 03:30 UTC (09:00 IST) daily; GitHub crons can slip ~15 min.

### One-time setup

1. **Keep this repo private** — it contains your voice sample and unreleased outreach.
2. Repo → *Settings → Secrets and variables → Actions*, add:
   - `OPENROUTER_API_KEY` — [openrouter.ai/keys](https://openrouter.ai/keys).
     **Recommended:** make the one-time **$10 credit top-up** on the OpenRouter
     account — free-model limits jump from **50 to 1,000 requests/day**, and one
     agent run needs ~60–120 calls. The $10 sits unused unless you call paid models.
   - *(optional)* variable `MODEL` = `provider/model-id`; defaults to
     `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free`. Free endpoints get delisted
     often — if a run fails with model-not-found, pick any current `:free` model with
     the **Tools** tag from [openrouter.ai/models?q=free](https://openrouter.ai/models?q=free)
     (or `openrouter/free`, which routes to whichever capable model is up) and set it here.
3. Push this branch to master, then test with *Actions → daily-pitch → Run workflow*
   and a company name in the input (e.g. `olipop.com`) before trusting the cron.

### Enabling voice + video later

1. Add secret `REPLICATE_API_TOKEN`
   ([replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)).
2. In `.opencode/agent/daily-pitch.md`, restore the Phases 5–6 instructions (git
   history has the full version) and un-scope the run message.
3. Workflow then verifies `pitch.mp4`, and `automation/tts_replicate.py` clones your
   voice through Replicate's hosted Chatterbox (`resemble-ai/chatterbox` — same model
   as the local server) using the committed `voice/reference.wav`. Pay-per-run pennies,
   no subscription.

### Cost per day

**$0 at current scope** — free-tier OpenRouter model + free-tier Actions minutes.
Voice adds ~$0.05–0.10/pitch once enabled. If free-model flakiness gets annoying,
`vars.MODEL` swaps to a cheap paid model (e.g. `openai/gpt-oss-120b`, ~$0.04/1M in)
for cents per run with no rate limits.

### Manual / local alternative

Run the same unattended flow locally anytime:
`opencode run --agent daily-pitch --auto "Build an unattended pitch for <company>"`
(requires the local Chatterbox server instead — swap Phase 5 per SKILL.md).

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
