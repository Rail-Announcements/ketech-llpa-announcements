# ketech-llpa-announcements

- `segs/` contains the raw data from the FOI to Irish Rail
- `wavs/` contains decoded audio from the `.seg` files
- `mp3s/` contains the decoded audio in MP3 format for wider compatibility and lower file size

## Contents

Each of the above folders contains various voice packs supplied or managed by KeTech.

The most well-known are likely Phil Sayer and Celia Drummond due to their extensive coverage of the
UK railway network during their time as announcers for the KeTech, Amey and Ditra customer information
systems.

| Folder name           | Common name                |
| --------------------- | -------------------------- |
| `Male1`               | Phil Sayer                 |
| `Male3` and `default` | Michael Comyn (Irish Rail) |
| `Female1`             | Celia Drummond             |
| `Female2`             | Alison McKay (ScotRail)    |

## Transcriptions

We're currently working to transcribe all announcements within CSV files in this repository, starting
with Phil Sayer (`Male1`).

This is a mammoth task, and takes some time. The hope is that, with one voice transcribed, the IDs of
other voices' audio snippets, or at least Celia's, will predominantly match Phil's.

You can see the [current progress here](./Male1_transcriptions.csv).

## Decoding .seg files

A [kind user on RailForums](https://www.railforums.co.uk/threads/ketech-cellia-drummond-and-only-woman-announcements-publicly-availible.254181/page-2#post-6406413) managed to work out a method of decoding the "proprietary" format.

On Debian/Ubuntu:

```bash
sudo apt install sox
find -iname "*.SEG" -exec bash -c "tail -c +48 '{}' | sox -t raw -b 8 -r 16000 -e a-law -X - '{}.wav'" \;
```

This command:

1. Iterates over every .SEG file
2. Provides the content of each file, skipping the first 48 bytes, to sox
3. sox then converts the audio into a more widely used `.wav` format

## Converting to mp3

On Linux:

```bash
find "$(pwd)" -type f -name "*.wav" | parallel 'ffmpeg -y -
hide_banner -loglevel error -i "{}" -q:a 0 "$(dirname "{}")/$(basename "{}" .wav).mp3"'
```
