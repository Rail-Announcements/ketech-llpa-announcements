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

| Station name                   | CRS code | Bodged? |
| ------------------------------ | -------- | ------- |
| Abercynon                      | ACY      | ❌ 0/2  |
| Alloa                          | ALO      | ❌ 0/2  |
| Apperley Bridge                | APY      | ✅ 2/2  |
| Ashfield                       | ASF      | ✅ 2/2  |
| Aylesbury Vale Parkway         | AVP      | ✅ 2/2  |
| Barking Riverside              | BGV      | ✅ 2/2  |
| Barry Links                    | BYL      | ✅ 2/2  |
| Bearley                        | BER      | ❌ 0/2  |
| Belfast Central                | BFC      | ❌ 0/2  |
| Bermuda Park                   | BEP      | ❌ 0/2  |
| Bicester Village               | BIT      | ❌ 0/2  |
| Blackridge                     | BKR      | ❌ 0/2  |
| Bow Street                     | BOW      | ✅ 2/2  |
| Braintree Freeport             | BTP      | ❌ 0/2  |
| Brent Cross West               | BCZ      | ✅ 2/2  |
| Brunstane                      | BSU      | ❌ 0/2  |
| Buckshaw Parkway               | BSV      | ❌ 0/2  |
| Caldercruix                    | CAC      | ❌ 0/2  |
| Cambridge North                | CMB      | ❌ 0/2  |
| Capenhurst                     | CPU      | ❌ 0/2  |
| Cardiff International Airport  | XCF      | ❌ 0/2  |
| Castleton                      | CAS      | ❌ 0/2  |
| Chapleton                      | CPN      | ❌ 0/2  |
| Chatelherault                  | CTE      | ❌ 0/2  |
| Clacton-On-Sea                 | CLT      | ✅ 2/2  |
| Coatdyke                       | COA      | ❌ 0/2  |
| Conon Bridge                   | CBD      | ❌ 0/2  |
| Coombe                         | COE      | ❌ 0/2  |
| Corby                          | COR      | ❌ 0/2  |
| Coulsdon Town                  | CDN      | ❌ 0/2  |
| Coventry Arena                 | CAA      | ❌ 0/2  |
| Cranbrook (Devon)              | CBK      | ❌ 0/2  |
| Creswell (Derbys)              | CWD      | ✅ 2/2  |
| Crosskeys                      | CKY      | ❌ 0/2  |
| Cynghordy                      | CYN      | ❌ 0/2  |
| Dagenham East L.T.             | ZDE      | ❌ 0/2  |
| Dereham Market Place           | DEB      | ❌ 0/2  |
| Dinas Rhondda                  | DMG      | ❌ 0/2  |
| Drayton Manor                  | DRY      | ❌ 0/2  |
| Dunfermline Queen Margaret     | DFL      | ❌ 0/2  |
| Dunfermline City               | DFE      | ❌ 0/2  |
| Dunoon                         | DUO      | ❌ 0/2  |
| Duns                           | DUU      | ❌ 0/2  |
| Ealing Common                  | ZEC      | ❌ 0/2  |
| Earl's Court L.T.              | ZET      | ❌ 0/2  |
| East Linton                    | ELT      | ❌ 0/2  |
| Ebbsfleet International        | EBD      | ❌ 0/2  |
| Ebbw Vale Parkway              | EBV      | ❌ 0/2  |
| Ebbw Vale Town                 | EBB      | ❌ 0/2  |
| Edinburgh Gateway              | EGY      | ❌ 0/2  |
| Energlyn & Churchill Park      | ECP      | ❌ 0/2  |
| Eskbank                        | EKB      | ❌ 0/2  |
| Exhibition Centre              | EXG      | ❌ 0/2  |
| Fellgate                       | FEG      | ❌ 0/2  |
| Fishguard & Goodwick           | FGW      | ❌ 0/2  |
| Frinton-On-Sea                 | FRI      | ✅ 2/2  |
| Gartcosh                       | GRH      | ❌ 0/2  |
| Garve                          | GVE      | ❌ 0/2  |
| Gilshochill                    | GSC      | ❌ 0/2  |
| Gorebridge                     | GBG      | ❌ 0/2  |
| Gourock Pier                   | GXX      | ❌ 0/2  |
| Hayle                          | HYL      | ❌ 0/2  |
| Headbolt Lane                  | HBL      | ❌ 0/2  |
| Heathrow Terminal 4 Rail       | HAF      | ❌ 0/2  |
| Heathrow Terminal 5 Rail       | HWV      | ❌ 0/2  |
| Heathrow Terminals 1-2-3 Rail  | HXX      | ❌ 0/2  |
| Horden                         | HRE      | ❌ 0/2  |
| Ilkeston                       | ILN      | ❌ 0/2  |
| Imperial Wharf                 | IMW      | ❌ 0/2  |
| Inverness Airport              | IVA      | ❌ 0/2  |
| James Cook University Hospital | JCH      | ❌ 0/2  |
| Kelvindale                     | KVD      | ❌ 0/2  |
| Kenilworth                     | KNW      | ❌ 0/2  |
| Kintore                        | KTR      | ❌ 0/2  |
| Kirkstall Forge                | KLF      | ❌ 0/2  |
| Langwith - Whaley Thorns       | LAG      | ✅ 2/2  |
| Larkhall                       | LRH      | ❌ 0/2  |
| Laurencekirk                   | LAU      | ❌ 0/2  |
| Lea Bridge                     | LEB      | ✅ 2/2  |
| Lea Green                      | LEG      | ❌ 0/2  |
| Llanharan                      | LLR      | ❌ 0/2  |
| Llanhilleth                    | LTH      | ❌ 0/2  |
| Llantwit Major                 | LWM      | ❌ 0/2  |
| Maghull North                  | MNS      | ❌ 0/2  |
| Marsh Barton                   | MBT      | ❌ 0/2  |
| Meridian Water                 | MRW      | ❌ 0/2  |
| Merryton                       | MEY      | ❌ 0/2  |
| Newbridge                      | NBE      | ❌ 0/2  |
| Newbury Park                   | ZNP      | ❌ 0/2  |
| Newcastle Airport              | APN      | ❌ 0/2  |
| Newcastle Central (Metro)      | NCZ      | ❌ 0/2  |
| Newcourt                       | NCO      | ❌ 0/2  |
| Newcraighall                   | NEW      | ❌ 0/2  |
| Newton Heath and Moston        | NMM      | ❌ 0/2  |
| Newtongrange                   | NEG      | ❌ 0/2  |
| North Fambridge                | NFA      | ✅ 2/2  |
| Oxford Parkway                 | OXP      | ❌ 0/2  |
| Pickering Eastgate             | PIZ      | ❌ 0/2  |
| Portway Park & Ride            | PRI      | ❌ 0/2  |
| Pye Corner                     | PYE      | ❌ 0/2  |
| Reading Green Park             | RGP      | ✅ 2/2  |
| Reston                         | RSN      | ❌ 0/2  |
| Rhoose Cardiff Airport         | RIA      | ❌ 0/2  |
| Risca & Pontymister            | RCA      | ❌ 0/2  |
| Robroyston                     | RRN      | ❌ 0/2  |
| Rogerstone                     | ROR      | ❌ 0/2  |
| Shawfair                       | SFI      | ❌ 0/2  |
| Shirebrook                     | SHB      | ✅ 2/2  |
| Shoreditch High Street         | SDC      | ✅ 2/2  |
| Smallbrook Junction            | SAB      | ❌ 0/2  |
| Soham                          | SOJ      | ❌ 0/2  |
| South Woodham Ferrers          | SOF      | ✅ 2/2  |
| Southampton Town Quay          | STQ      | ❌ 0/2  |
| St Peters                      | STZ      | ❌ 0/2  |
| Stadium of Light               | STI      | ❌ 0/2  |
| Stow                           | SOI      | ❌ 0/2  |
| Stratford-upon-Avon Parkway    | STY      | ❌ 0/2  |
| Tan-Y-Bwlch                    | TYB      | ❌ 0/2  |
| Thanet Parkway                 | THP      | ❌ 0/2  |
| Tottenham Court Road           | TCR      | ✅ 2/2  |
| Tweedbank                      | TWB      | ❌ 0/2  |
| Warrington West                | WAW      | ❌ 0/2  |
| Waterloo (Merseyside)          | WLO      | ❌ 0/2  |
| Wavertree Technology Park      | WAV      | ❌ 0/2  |
| Wedgwood Lane                  | WER      | ❌ 0/2  |
| Wells Next The Sea             | WEN      | ❌ 0/2  |
| Westcliff                      | WCF      | ✅ 2/2  |
| Westerton                      | WES      | ❌ 0/2  |
| Whitwell                       | WWL      | ❌ 0/2  |
| Woolwich                       | WWC      | ✅ 2/2  |
| Worcestershire Parkway         | WOP      | ✅ 2/2  |

### Missing stations for Female1 (160)

| Station name                   | CRS code | Bodged? |
| ------------------------------ | -------- | ------- |
| Abercynon                      | ACY      | ❌ 0/2  |
| Alloa                          | ALO      | ❌ 0/2  |
| Apperley Bridge                | APY      | ❌ 0/2  |
| Aylesbury Vale Parkway         | AVP      | ❌ 0/2  |
| Balloch Central                | BHC      | ❌ 0/2  |
| Barking Riverside              | BGV      | ❌ 0/2  |
| Barry Links                    | BYL      | ❌ 0/2  |
| Bearley                        | BER      | ❌ 0/2  |
| Belfast Central                | BFC      | ❌ 0/2  |
| Bermuda Park                   | BEP      | ❌ 0/2  |
| Bicester Village               | BIT      | ❌ 0/2  |
| Blackridge                     | BKR      | ❌ 0/2  |
| Bond Street                    | BDS      | ❌ 0/2  |
| Bolton-On-Dearne               | BTD      | ❌ 0/2  |
| Bow Street                     | BOW      | ❌ 0/2  |
| Braintree Freeport             | BTP      | ❌ 0/2  |
| Brent Cross West               | BCZ      | ❌ 0/2  |
| Brighouse                      | BGH      | ❌ 0/2  |
| Brunstane                      | BSU      | ❌ 0/2  |
| Buckshaw Parkway               | BSV      | ❌ 0/2  |
| Burneside                      | BUD      | ❌ 0/2  |
| Burnside                       | BUI      | ❌ 0/2  |
| Burscough Bridge               | BCB      | ❌ 0/2  |
| Caldercruix                    | CAC      | ❌ 0/2  |
| Cambridge North                | CMB      | ❌ 0/2  |
| Canary Wharf                   | CWX      | ❌ 0/2  |
| Cardiff International Airport  | XCF      | ❌ 0/2  |
| Cark                           | CAK      | ❌ 0/2  |
| Cartsdyke                      | CDY      | ❌ 0/2  |
| Chapleton                      | CPN      | ❌ 0/2  |
| Chatelherault                  | CTE      | ❌ 0/2  |
| Chorley                        | CRL      | ❌ 0/2  |
| Clacton-On-Sea                 | CLT      | ❌ 0/2  |
| Conon Bridge                   | CBD      | ❌ 0/2  |
| Coombe                         | COE      | ❌ 0/2  |
| Corby                          | COR      | ❌ 0/2  |
| Cottingham                     | CGM      | ❌ 0/2  |
| Coulsdon Town                  | CDN      | ❌ 0/2  |
| Coventry Arena                 | CAA      | ❌ 0/2  |
| Cranbrook (Devon)              | CBK      | ❌ 0/2  |
| Creswell (Derbys)              | CWD      | ❌ 0/2  |
| Crosskeys                      | CKY      | ❌ 0/2  |
| Croy                           | CRO      | ❌ 0/2  |
| Cynghordy                      | CYN      | ❌ 0/2  |
| Dagenham East L.T.             | ZDE      | ❌ 0/2  |
| Dereham Market Place           | DEB      | ❌ 0/2  |
| Dinas Rhondda                  | DMG      | ❌ 0/2  |
| Drayton Manor                  | DRY      | ❌ 0/2  |
| Dunfermline Queen Margaret     | DFL      | ❌ 0/2  |
| Dunfermline City               | DFE      | ❌ 0/2  |
| Dunoon                         | DUO      | ❌ 0/2  |
| Duns                           | DUU      | ❌ 0/2  |
| Ealing Common                  | ZEC      | ❌ 0/2  |
| Earl's Court L.T.              | ZET      | ❌ 0/2  |
| East Linton                    | ELT      | ❌ 0/2  |
| Eastrington                    | EGN      | ❌ 0/2  |
| Ebbsfleet International        | EBD      | ❌ 0/2  |
| Ebbw Vale Parkway              | EBV      | ❌ 0/2  |
| Ebbw Vale Town                 | EBB      | ❌ 0/2  |
| Edinburgh Gateway              | EGY      | ❌ 0/2  |
| Edinburgh Park                 | EDP      | ❌ 0/2  |
| Energlyn & Churchill Park      | ECP      | ❌ 0/2  |
| Eskbank                        | EKB      | ❌ 0/2  |
| Exhibition Centre              | EXG      | ❌ 0/2  |
| Falkirk Grahamston             | FKG      | ❌ 0/2  |
| Fellgate                       | FEG      | ❌ 0/2  |
| Fishguard & Goodwick           | FGW      | ❌ 0/2  |
| Frinton-On-Sea                 | FRI      | ❌ 0/2  |
| Gartcosh                       | GRH      | ❌ 0/2  |
| Garve                          | GVE      | ❌ 0/2  |
| Gathurst                       | GST      | ❌ 0/2  |
| Gatley                         | GTY      | ❌ 0/2  |
| Giggleswick                    | GIG      | ❌ 0/2  |
| Gilberdyke                     | GBD      | ❌ 0/2  |
| Gilshochill                    | GSC      | ❌ 0/2  |
| Glasshoughton                  | GLH      | ❌ 0/2  |
| Golf Street                    | GOF      | ❌ 0/2  |
| Gorebridge                     | GBG      | ❌ 0/2  |
| Gourock Pier                   | GXX      | ❌ 0/2  |
| Haltwhistle                    | HWH      | ❌ 0/2  |
| Hayle                          | HYL      | ❌ 0/2  |
| Headbolt Lane                  | HBL      | ❌ 0/2  |
| Heathrow Terminal 4 Rail       | HAF      | ❌ 0/2  |
| Heathrow Terminal 5 Rail       | HWV      | ❌ 0/2  |
| Heathrow Terminals 1-2-3 Rail  | HXX      | ❌ 0/2  |
| Horden                         | HRE      | ❌ 0/2  |
| Ilkeston                       | ILN      | ❌ 0/2  |
| Imperial Wharf                 | IMW      | ❌ 0/2  |
| Inverness Airport              | IVA      | ❌ 0/2  |
| James Cook University Hospital | JCH      | ❌ 0/2  |
| Kelvindale                     | KVD      | ❌ 0/2  |
| Kenilworth                     | KNW      | ❌ 0/2  |
| Kingsknowe                     | KGE      | ❌ 0/2  |
| Kingussie                      | KIN      | ❌ 0/2  |
| Kintore                        | KTR      | ❌ 0/2  |
| Kirk Sandall                   | KKS      | ❌ 0/2  |
| Kirkby                         | KIR      | ❌ 0/2  |
| Kirkstall Forge                | KLF      | ❌ 0/2  |
| Langwith - Whaley Thorns       | LAG      | ❌ 0/2  |
| Larkhall                       | LRH      | ❌ 0/2  |
| Laurencekirk                   | LAU      | ❌ 0/2  |
| Layton                         | LAY      | ❌ 0/2  |
| Lea Bridge                     | LEB      | ❌ 0/2  |
| Lea Green                      | LEG      | ❌ 0/2  |
| Llanharan                      | LLR      | ❌ 0/2  |
| Llanhilleth                    | LTH      | ❌ 0/2  |
| Llantwit Major                 | LWM      | ❌ 0/2  |
| Lockwood                       | LCK      | ❌ 0/2  |
| Maghull North                  | MNS      | ❌ 0/2  |
| Marsh Barton                   | MBT      | ❌ 0/2  |
| Meridian Water                 | MRW      | ❌ 0/2  |
| Merryton                       | MEY      | ❌ 0/2  |
| Milngavie                      | MLN      | ❌ 0/2  |
| Newbridge                      | NBE      | ❌ 0/2  |
| Newbury Park                   | ZNP      | ❌ 0/2  |
| Newcastle Airport              | APN      | ❌ 0/2  |
| Newcastle Central (Metro)      | NCZ      | ❌ 0/2  |
| Newcourt                       | NCO      | ❌ 0/2  |
| Newcraighall                   | NEW      | ❌ 0/2  |
| Newton Heath and Moston        | NMM      | ❌ 0/2  |
| Newtongrange                   | NEG      | ❌ 0/2  |
| North Fambridge                | NFA      | ❌ 0/2  |
| Outwood                        | OUT      | ❌ 0/2  |
| Oxford Parkway                 | OXP      | ❌ 0/2  |
| Pickering Eastgate             | PIZ      | ❌ 0/2  |
| Portway Park & Ride            | PRI      | ❌ 0/2  |
| Pye Corner                     | PYE      | ❌ 0/2  |
| Reading Green Park             | RGP      | ❌ 0/2  |
| Reston                         | RSN      | ❌ 0/2  |
| Rhoose Cardiff Airport         | RIA      | ❌ 0/2  |
| Ribblehead                     | RHD      | ❌ 0/2  |
| Risca & Pontymister            | RCA      | ❌ 0/2  |
| Robroyston                     | RRN      | ❌ 0/2  |
| Rogerstone                     | ROR      | ❌ 0/2  |
| Selkirk                        | SKK      | ❌ 0/2  |
| Shawfair                       | SFI      | ❌ 0/2  |
| Shepley                        | SPY      | ❌ 0/2  |
| Shirebrook                     | SHB      | ❌ 0/2  |
| Shoreditch High Street         | SDC      | ❌ 0/2  |
| Snaith                         | SNI      | ❌ 0/2  |
| Soham                          | SOJ      | ❌ 0/2  |
| South Woodham Ferrers          | SOF      | ❌ 0/2  |
| Southampton Town Quay          | STQ      | ❌ 0/2  |
| St Peters                      | STZ      | ❌ 0/2  |
| Stadium of Light               | STI      | ❌ 0/2  |
| Stow                           | SOI      | ❌ 0/2  |
| Stratford-upon-Avon Parkway    | STY      | ❌ 0/2  |
| Tan-Y-Bwlch                    | TYB      | ❌ 0/2  |
| Thanet Parkway                 | THP      | ❌ 0/2  |
| Tottenham Court Road           | TCR      | ❌ 0/2  |
| Tweedbank                      | TWB      | ❌ 0/2  |
| Warrington West                | WAW      | ❌ 0/2  |
| Waterloo (Merseyside)          | WLO      | ❌ 0/2  |
| Wavertree Technology Park      | WAV      | ❌ 0/2  |
| Wedgwood Lane                  | WER      | ❌ 0/2  |
| Wells Next The Sea             | WEN      | ❌ 0/2  |
| Westcliff                      | WCF      | ❌ 0/2  |
| Whitwell                       | WWL      | ❌ 0/2  |
| Woolwich                       | WWC      | ❌ 0/2  |
| Worcestershire Parkway         | WOP      | ❌ 0/2  |
