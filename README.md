# ketech-llpa-announcements

## Decoding .seg files

A kind user on Rail Forums managed to work out a method of decoding the "proprietary" format.

Linux users:

```
find -iname "*.SEG" -exec sox -t raw -b 8 -r 16000 -e a-law -X \{\} \{\}.wav \;
```
