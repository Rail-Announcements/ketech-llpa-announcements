# ketech-llpa-announcements

- `segs/` contains the raw data from the FOI to Irish Rail
- `wavs/` contains decoded audio from the `.seg` files
- `mp3s/` contains the decoded audio in MP3 format for wider compatibility and lower file size
- `renamed/` contains the MP3 files for each voice, renamed and grouped using their transcriptions csv file

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

We're currently working to transcribe all announcements within CSV files in this repository.

| Voice                      | Progress                                                |
| -------------------------- | ------------------------------------------------------- |
| Phil Sayer (`Male1`)       | ✅ [Complete](./Male1_transcriptions.csv) (11382/11382) |
| Michael Comyn (`Male3`)    | ❌ Not yet started                                      |
| Michael Comyn (`default`)  | ❌ Not yet started                                      |
| Celia Drummond (`Female1`) | ❌ Not yet started                                      |
| Alison McKay (`Female1`)   | ❌ Not yet started                                      |

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
sudo apt install parallel
find "$(pwd)" -type f -name "*.wav" | parallel 'ffmpeg -y -hide_banner -loglevel error -i "{}" -q:a 0 "$(dirname "{}")/$(basename "{}" .wav).mp3"'
```

## Renaming files to remove `.seg`/`.wav`

On Linux:

```bash
sudo apt install rename
rename 's/\.SEG|\.seg//' *
rename 's/\.WAV|\.wav//' *
```

## .seg file format

Most seg files start with a 48 character header, e.g.
`1483                                        12FF`

The first four characters are a space padded ID (which may be absent, or padded
with zeroes instead of spaces), the last four characters are mandatory, are in
hexadecimal range, and may be uppercase or lowercase. The ID will usually (but
not always) match the filename.

A very small number also include a transcription.

Examples:

- `1483                                        12FF`
- ` 130                                        FFFF`
- `                                            12ff`
- `2456                       a security alert.04FF`
- `0400                                        FFFF`
- `2439                                    FROM8440`

### Unusual .seg files

A small number of the .seg files contain strange header contents that don't
match this pattern in some way, or have odd file descriptions.

| File                  | Description                                                                            |
| --------------------- | -------------------------------------------------------------------------------------- |
| segs/default/306.seg  | `                                            FFFF\x9d` only                            |
| segs/default/1871.seg | `                                            ffff` only                                |
| segs/default/199.seg  | `                                            FFFFt` only                               |
| segs/Male3/306.seg    | `                                            FFFF\x9d` only                            |
| segs/Male3/199.seg    | `                                            FFFFt` only                               |
| segs/Male1/399.seg    | ` 399ader->End,HeaderEnd,3);           /*RecoFFFF`, ...                                |
| segs/Female2/0.seg    | Header is correct length, but is padded with null bytes instead of spaces, ends `FFFF` |
| segs/Female2/1400.seg | Has no header                                                                          |
