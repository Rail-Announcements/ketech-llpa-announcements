# ketech-llpa-announcements

- `segs/` contains the raw data from the FOI to Irish Rail
- `wavs/` contains decoded audio from the `.seg` files
- `mp3s/` contains the decoded audio in MP3 format for wider compatibility and lower file size

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
