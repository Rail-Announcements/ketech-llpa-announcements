# ketech-llpa-announcements

> **Note**
>
> Please remember to use these files with courtesy. Information released under Freedom of Information retains its copyright status and protections even after being released into the public domain, and you could face penalties for using these files without prior permission, particularly for commercial purposes.

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

| Voice                      | Progress                                                  |
| -------------------------- | --------------------------------------------------------- |
| Phil Sayer (`Male1`)       | ✅ [Complete](./Male1_transcriptions.csv) (11382/11382)   |
| Michael Comyn (`Male3`)    | ❌ Not yet started                                        |
| Michael Comyn (`default`)  | ❌ Not yet started                                        |
| Celia Drummond (`Female1`) | ✅ [Complete](./Female1_transcriptions.csv) (10570/10570) |
| Alison McKay (`Female2`)   | ✅ [Complete](./Female2_transcriptions.csv) (1989/1989)   |

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

## Missing files

For Phil and Celia, some modern-day stations are missing from their announcements. Many of these opened after their recordings were made.

Some of these stations have been bodged by combining clips from other snippets together, but some are still unrecorded.

### Missing stations for Male1 (131)

| Station name                   | CRS code |
| ------------------------------ | -------- |
| Abercynon                      | ACY      |
| Alloa                          | ALO      |
| Apperley Bridge                | APY      |
| Ashfield                       | ASF      |
| Aylesbury Vale Parkway         | AVP      |
| Barking Riverside              | BGV      |
| Barry Links                    | BYL      |
| Bearley                        | BER      |
| Belfast Central                | BFC      |
| Bermuda Park                   | BEP      |
| Bicester Village               | BIT      |
| Blackridge                     | BKR      |
| Bow Street                     | BOW      |
| Braintree Freeport             | BTP      |
| Brent Cross West               | BCZ      |
| Brunstane                      | BSU      |
| Buckshaw Parkway               | BSV      |
| Caldercruix                    | CAC      |
| Cambridge North                | CMB      |
| Capenhurst                     | CPU      |
| Cardiff International Airport  | XCF      |
| Castleton                      | CAS      |
| Chapleton                      | CPN      |
| Chatelherault                  | CTE      |
| Clacton-On-Sea                 | CLT      |
| Coatdyke                       | COA      |
| Conon Bridge                   | CBD      |
| Coombe                         | COE      |
| Corby                          | COR      |
| Coulsdon Town                  | CDN      |
| Coventry Arena                 | CAA      |
| Cranbrook (Devon)              | CBK      |
| Creswell (Derbys)              | CWD      |
| Crosskeys                      | CKY      |
| Cynghordy                      | CYN      |
| Dagenham East L.T.             | ZDE      |
| Dereham Market Place           | DEB      |
| Dinas Rhondda                  | DMG      |
| Drayton Manor                  | DRY      |
| Dunfermline Queen Margaret     | DFL      |
| Dunfermline City               | DFE      |
| Dunoon                         | DUO      |
| Duns                           | DUU      |
| Ealing Common                  | ZEC      |
| Earl's Court L.T.              | ZET      |
| East Linton                    | ELT      |
| Ebbsfleet International        | EBD      |
| Ebbw Vale Parkway              | EBV      |
| Ebbw Vale Town                 | EBB      |
| Edinburgh Gateway              | EGY      |
| Energlyn & Churchill Park      | ECP      |
| Eskbank                        | EKB      |
| Exhibition Centre              | EXG      |
| Fellgate                       | FEG      |
| Fishguard & Goodwick           | FGW      |
| Frinton-On-Sea                 | FRI      |
| Gartcosh                       | GRH      |
| Garve                          | GVE      |
| Gilshochill                    | GSC      |
| Gorebridge                     | GBG      |
| Gourock Pier                   | GXX      |
| Hayle                          | HYL      |
| Headbolt Lane                  | HBL      |
| Heathrow Terminal 4 Rail       | HAF      |
| Heathrow Terminal 5 Rail       | HWV      |
| Heathrow Terminals 1-2-3 Rail  | HXX      |
| Horden                         | HRE      |
| Ilkeston                       | ILN      |
| Imperial Wharf                 | IMW      |
| Inverness Airport              | IVA      |
| James Cook University Hospital | JCH      |
| Kelvindale                     | KVD      |
| Kenilworth                     | KNW      |
| Kintore                        | KTR      |
| Kirkstall Forge                | KLF      |
| Langwith - Whaley Thorns       | LAG      |
| Larkhall                       | LRH      |
| Laurencekirk                   | LAU      |
| Lea Bridge                     | LEB      |
| Lea Green                      | LEG      |
| Llanharan                      | LLR      |
| Llanhilleth                    | LTH      |
| Llantwit Major                 | LWM      |
| Maghull North                  | MNS      |
| Marsh Barton                   | MBT      |
| Meridian Water                 | MRW      |
| Merryton                       | MEY      |
| Newbridge                      | NBE      |
| Newbury Park                   | ZNP      |
| Newcastle Airport              | APN      |
| Newcastle Central (Metro)      | NCZ      |
| Newcourt                       | NCO      |
| Newcraighall                   | NEW      |
| Newton Heath and Moston        | NMM      |
| Newtongrange                   | NEG      |
| North Fambridge                | NFA      |
| Oxford Parkway                 | OXP      |
| Pickering Eastgate             | PIZ      |
| Portway Park & Ride            | PRI      |
| Pye Corner                     | PYE      |
| Reading Green Park             | RGP      |
| Reston                         | RSN      |
| Rhoose Cardiff Airport         | RIA      |
| Risca & Pontymister            | RCA      |
| Robroyston                     | RRN      |
| Rogerstone                     | ROR      |
| Shawfair                       | SFI      |
| Shirebrook                     | SHB      |
| Shoreditch High Street         | SDC      |
| Smallbrook Junction            | SAB      |
| Soham                          | SOJ      |
| South Woodham Ferrers          | SOF      |
| Southampton Town Quay          | STQ      |
| St Peters                      | STZ      |
| Stadium of Light               | STI      |
| Stow                           | SOI      |
| Stratford-upon-Avon Parkway    | STY      |
| Tan-Y-Bwlch                    | TYB      |
| Thanet Parkway                 | THP      |
| Tottenham Court Road           | TCR      |
| Tweedbank                      | TWB      |
| Warrington West                | WAW      |
| Waterloo (Merseyside)          | WLO      |
| Wavertree Technology Park      | WAV      |
| Wedgwood Lane                  | WER      |
| Wells Next The Sea             | WEN      |
| Westcliff                      | WCF      |
| Westerton                      | WES      |
| Whitwell                       | WWL      |
| Woolwich                       | WWC      |
| Worcestershire Parkway         | WOP      |

### Missing stations for Female1 (160)

| Station name                   | CRS code |
| ------------------------------ | -------- |
| Abercynon                      | ACY      |
| Alloa                          | ALO      |
| Apperley Bridge                | APY      |
| Aylesbury Vale Parkway         | AVP      |
| Balloch Central                | BHC      |
| Barking Riverside              | BGV      |
| Barry Links                    | BYL      |
| Bearley                        | BER      |
| Belfast Central                | BFC      |
| Bermuda Park                   | BEP      |
| Bicester Village               | BIT      |
| Blackridge                     | BKR      |
| Bond Street                    | BDS      |
| Bolton-On-Dearne               | BTD      |
| Bow Street                     | BOW      |
| Braintree Freeport             | BTP      |
| Brent Cross West               | BCZ      |
| Brighouse                      | BGH      |
| Brunstane                      | BSU      |
| Buckshaw Parkway               | BSV      |
| Burneside                      | BUD      |
| Burnside                       | BUI      |
| Burscough Bridge               | BCB      |
| Caldercruix                    | CAC      |
| Cambridge North                | CMB      |
| Canary Wharf                   | CWX      |
| Cardiff International Airport  | XCF      |
| Cark                           | CAK      |
| Cartsdyke                      | CDY      |
| Chapleton                      | CPN      |
| Chatelherault                  | CTE      |
| Chorley                        | CRL      |
| Clacton-On-Sea                 | CLT      |
| Conon Bridge                   | CBD      |
| Coombe                         | COE      |
| Corby                          | COR      |
| Cottingham                     | CGM      |
| Coulsdon Town                  | CDN      |
| Coventry Arena                 | CAA      |
| Cranbrook (Devon)              | CBK      |
| Creswell (Derbys)              | CWD      |
| Crosskeys                      | CKY      |
| Croy                           | CRO      |
| Cynghordy                      | CYN      |
| Dagenham East L.T.             | ZDE      |
| Dereham Market Place           | DEB      |
| Dinas Rhondda                  | DMG      |
| Drayton Manor                  | DRY      |
| Dunfermline Queen Margaret     | DFL      |
| Dunfermline City               | DFE      |
| Dunoon                         | DUO      |
| Duns                           | DUU      |
| Ealing Common                  | ZEC      |
| Earl's Court L.T.              | ZET      |
| East Linton                    | ELT      |
| Eastrington                    | EGN      |
| Ebbsfleet International        | EBD      |
| Ebbw Vale Parkway              | EBV      |
| Ebbw Vale Town                 | EBB      |
| Edinburgh Gateway              | EGY      |
| Edinburgh Park                 | EDP      |
| Energlyn & Churchill Park      | ECP      |
| Eskbank                        | EKB      |
| Exhibition Centre              | EXG      |
| Falkirk Grahamston             | FKG      |
| Fellgate                       | FEG      |
| Fishguard & Goodwick           | FGW      |
| Frinton-On-Sea                 | FRI      |
| Gartcosh                       | GRH      |
| Garve                          | GVE      |
| Gathurst                       | GST      |
| Gatley                         | GTY      |
| Giggleswick                    | GIG      |
| Gilberdyke                     | GBD      |
| Gilshochill                    | GSC      |
| Glasshoughton                  | GLH      |
| Golf Street                    | GOF      |
| Gorebridge                     | GBG      |
| Gourock Pier                   | GXX      |
| Haltwhistle                    | HWH      |
| Hayle                          | HYL      |
| Headbolt Lane                  | HBL      |
| Heathrow Terminal 4 Rail       | HAF      |
| Heathrow Terminal 5 Rail       | HWV      |
| Heathrow Terminals 1-2-3 Rail  | HXX      |
| Horden                         | HRE      |
| Ilkeston                       | ILN      |
| Imperial Wharf                 | IMW      |
| Inverness Airport              | IVA      |
| James Cook University Hospital | JCH      |
| Kelvindale                     | KVD      |
| Kenilworth                     | KNW      |
| Kingsknowe                     | KGE      |
| Kingussie                      | KIN      |
| Kintore                        | KTR      |
| Kirk Sandall                   | KKS      |
| Kirkby                         | KIR      |
| Kirkstall Forge                | KLF      |
| Langwith - Whaley Thorns       | LAG      |
| Larkhall                       | LRH      |
| Laurencekirk                   | LAU      |
| Layton                         | LAY      |
| Lea Bridge                     | LEB      |
| Lea Green                      | LEG      |
| Llanharan                      | LLR      |
| Llanhilleth                    | LTH      |
| Llantwit Major                 | LWM      |
| Lockwood                       | LCK      |
| Maghull North                  | MNS      |
| Marsh Barton                   | MBT      |
| Meridian Water                 | MRW      |
| Merryton                       | MEY      |
| Milngavie                      | MLN      |
| Newbridge                      | NBE      |
| Newbury Park                   | ZNP      |
| Newcastle Airport              | APN      |
| Newcastle Central (Metro)      | NCZ      |
| Newcourt                       | NCO      |
| Newcraighall                   | NEW      |
| Newton Heath and Moston        | NMM      |
| Newtongrange                   | NEG      |
| North Fambridge                | NFA      |
| Outwood                        | OUT      |
| Oxford Parkway                 | OXP      |
| Pickering Eastgate             | PIZ      |
| Portway Park & Ride            | PRI      |
| Pye Corner                     | PYE      |
| Reading Green Park             | RGP      |
| Reston                         | RSN      |
| Rhoose Cardiff Airport         | RIA      |
| Ribblehead                     | RHD      |
| Risca & Pontymister            | RCA      |
| Robroyston                     | RRN      |
| Rogerstone                     | ROR      |
| Selkirk                        | SKK      |
| Shawfair                       | SFI      |
| Shepley                        | SPY      |
| Shirebrook                     | SHB      |
| Shoreditch High Street         | SDC      |
| Snaith                         | SNI      |
| Soham                          | SOJ      |
| South Woodham Ferrers          | SOF      |
| Southampton Town Quay          | STQ      |
| St Peters                      | STZ      |
| Stadium of Light               | STI      |
| Stow                           | SOI      |
| Stratford-upon-Avon Parkway    | STY      |
| Tan-Y-Bwlch                    | TYB      |
| Thanet Parkway                 | THP      |
| Tottenham Court Road           | TCR      |
| Tweedbank                      | TWB      |
| Warrington West                | WAW      |
| Waterloo (Merseyside)          | WLO      |
| Wavertree Technology Park      | WAV      |
| Wedgwood Lane                  | WER      |
| Wells Next The Sea             | WEN      |
| Westcliff                      | WCF      |
| Whitwell                       | WWL      |
| Woolwich                       | WWC      |
| Worcestershire Parkway         | WOP      |
