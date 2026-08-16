---
name: personalised-pitch
description: End-to-end personalised pitch builder — research a target company's website/docs/blogs, find a gap we can fill, create Excalidraw visuals, write a natural narration script, generate voice-cloned audio with a local TTS, and assemble a pitch video. Use when the user says "pitch <company>", "build a pitch for <url>", or asks for personalised outreach material.
---

# Personalised Pitch Builder

Build a personalised pitch video for a target company. Input: a company name or URL.
Output: research notes, a gap-driven pitch narrative, Excalidraw visuals, a narration
script, voice-cloned audio, and an assembled MP4 — all under `pitches/<company-slug>/`.

## Prerequisites (check once per session)

1. **Sender profile**: read `profile.md` in the project root. It describes who WE are and
   what we bring to the table. If it doesn't exist, ask the user for: their offering,
   proof points (past work, metrics), and the call-to-action they want. Save answers to
   `profile.md` before continuing.
2. **Voice reference**: check `voice/reference.wav` exists (the user's voice sample).
   If missing, tell the user to record 10–20 seconds of natural speech (see
   `references/voice-setup.md` for recording tips) and stop the voice/video phases until
   it exists. Phases 1–4 can proceed regardless.
3. **Voice server**: see `references/voice-setup.md` for how to start and call the local
   TTS server. Only needed for Phase 5.

## Output layout

```
pitches/<company-slug>/
  research.md      # phase 1 findings with source URLs
  gap.md           # phase 2 gap analysis + chosen pitch angle
  visuals/         # phase 3: scene-01.excalidraw.json ... + exported PNG frames
  script.md        # phase 4 narration script, split per scene
  audio/           # phase 5: scene-01.wav ... + narration-full.wav
  pitch.mp4        # phase 6 final video
```

## Phase 1 — Research the company

Goal: understand what they build, how they talk about it, and where the seams are.
Use WebSearch + WebFetch. Prefer primary sources. Collect, with URLs:

- **Homepage + product pages**: positioning, ICP, pricing model.
- **Technical docs**: stack, APIs, integrations, limits. Note anything marked "coming
  soon", "beta", "contact us", or conspicuously absent (no SDK for X, no self-host, thin
  docs sections — absence is signal).
- **Engineering blog / changelog**: what they've shipped recently, what they struggle
  with (posts about migrations, incidents, scaling pain are gold).
- **Careers page**: open roles reveal gaps (hiring 3 DevOps engineers = infra pain).
- **GitHub org** (if any): activity, abandoned repos, open issues with many 👍.
- **Community**: recent Reddit/HN/X threads, G2 reviews — recurring complaints.

Fan out subagents for independent areas (docs vs blog vs community) when the site is
large. Write findings to `research.md` — facts with sources, not summary fluff.

## Phase 2 — Find the gap

From `research.md` + `profile.md`, list candidate gaps: things they need (evidenced)
that we can credibly provide (per profile). Score each on evidence strength, fit with
our offering, and urgency. Pick ONE primary gap — a pitch about three things is a pitch
about nothing. Write `gap.md` with: the gap, the evidence trail (quote their own words
back at them), our fix, and the specific proof point from `profile.md` that backs it.

## Phase 3 — Excalidraw visuals

Storyboard 4–6 scenes that follow the narration arc:

1. Hook — their world today (their product/stack, drawn simply)
2. The gap — same picture with the missing piece highlighted (red/dashed)
3. Cost of the gap — what it's costing them (numbers from research if available)
4. Our fix — the picture completed (our piece slotted in, green)
5. Proof — one visual proof point from `profile.md`
6. CTA — one line, one next step

For each scene:
- Call `mcp__claude_ai_Excalidraw__read_me` once first, then
  `mcp__claude_ai_Excalidraw__create_view` to render for user review.
- Save the element JSON to `visuals/scene-NN.excalidraw.json` (wrap in the standard
  `{"type":"excalidraw","version":2,"elements":[...]}` envelope).
- Offer `export_to_excalidraw` links so the user can hand-edit; if they edit, re-import
  the edited JSON before rendering frames.

Keep scenes visually consistent: same palette, same font size scale, ≤7 elements of
text per scene (it's narrated — the voice carries detail, the visual carries structure).
Use the company's actual product names/terms from research, never generic placeholders.

Render frames to PNG (1920×1080) with the script in `scripts/render-frames.md`
(instructions there — uses Playwright against excalidraw.com, no API key needed).

## Phase 4 — Narration script

Write `script.md`: one section per scene, 2–4 sentences each, 60–120 seconds total.
Rules for sounding human when synthesized:

- Write like the user talks, not like marketing copy. Contractions everywhere.
- Short sentences. Vary length. One-word sentences land well.
- Open with something specific to THEM ("I was reading your post on X...") — the
  personalisation must be audible in the first five seconds.
- Punctuation drives prosody: commas = short pause, em-dash = hesitation beat,
  ellipsis = trailing thought, question marks lift the tone. Use them deliberately.
- Follow the model-specific guidance in `references/voice-setup.md` (tags for breaths /
  hesitations, expressiveness settings, chunking rules).
- Read it aloud mentally; anything you'd stumble on, the model will too. Numbers and
  URLs: write them out as spoken words ("forty percent", "acme dot com").

Show the script to the user for approval before generating audio — iterate on text,
not audio (generation is expensive on CPU-only machines; cheap but still not free on GPU).

## Phase 5 — Voice generation (local TTS server)

Follow `references/voice-setup.md` for install, server start, and the generation calls.
Generate one WAV per scene (short chunks are more reliable than one long take), then
concatenate. Listen check: ask the user to review `narration-full.wav` before video
assembly. Regenerate only failed scenes.

## Phase 6 — Assemble the video

Use ffmpeg per `scripts/assemble-video.md`: each scene PNG is shown for the duration of
its scene WAV (probe with ffprobe), simple 0.4s crossfades, audio concatenated, output
`pitch.mp4` (H.264 + AAC, 1080p). Verify with ffprobe that duration ≈ narration length
and play back the first seconds' waveform is non-silent before declaring done.

## Notes

- Never fabricate research facts. If evidence for a gap is thin, say so in `gap.md`
  and pick a better-evidenced gap.
- All temp/intermediate junk goes to the scratchpad, only deliverables in `pitches/`.
- Everything up to Phase 4 is fast; Phases 5–6 are slow on this hardware — set that
  expectation with the user up front and batch the audio generation.
