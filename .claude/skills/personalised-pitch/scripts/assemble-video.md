# Assembling the pitch video with ffmpeg

Inputs: `visuals/scene-NN.png` + `audio/scene-NN.wav` (matched by number).
Output: `pitches/<slug>/pitch.mp4` — 1080p H.264 + AAC.

Check ffmpeg exists first (`ffmpeg -version`); if missing: `winget install Gyan.FFmpeg`
then restart the shell so PATH updates.

## 1. Per-scene clips

For each scene, hold the PNG for the WAV's duration (+0.5s of breathing room):

```powershell
# duration of the wav
ffprobe -v error -show_entries format=duration -of csv=p=0 audio/scene-01.wav
```

```powershell
ffmpeg -y -loop 1 -i visuals/scene-01.png -i audio/scene-01.wav `
  -af "apad=pad_dur=0.5" -t <dur+0.5> `
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:white,format=yuv420p" `
  -c:v libx264 -r 30 -c:a aac -b:a 192k scratch/clip-01.mp4
```

## 2. Concatenate

```
# scratch/list.txt
file 'clip-01.mp4'
file 'clip-02.mp4'
...
```

```powershell
ffmpeg -y -f concat -safe 0 -i scratch/list.txt -c copy pitch.mp4
```

Optional polish (only if the user asks): replace concat with `xfade`/`acrossfade`
filter chains for 0.4s crossfades, and a 1s fade-to-black at the end.

## 3. Verify before declaring done

- `ffprobe pitch.mp4` — duration ≈ sum of scene durations, streams: h264 + aac.
- Extract a mid-video frame and Read it: `ffmpeg -ss <mid> -i pitch.mp4 -frames:v 1 check.png`
- Confirm audio is non-silent: `ffmpeg -i pitch.mp4 -af volumedetect -f null NUL` —
  mean_volume should be well above -70 dB.
- Tell the user the output path and total duration; let THEM judge the voice quality.
