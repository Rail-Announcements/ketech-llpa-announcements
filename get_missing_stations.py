import os
import json

stations = [
    {"crs": x["crsCode"], "name": x["stationName"]}
    for x in json.load(open("stations.json", "r"))
]


def getMp3InDir(path: str) -> list[str]:
    """Returns a list of all mp3 files in a directory"""
    return [f for f in os.listdir(path) if f.endswith(".mp3")]


def getMissingStations(voice: str) -> list[str]:
    stationsE = [
        x.replace(".mp3", "") for x in getMp3InDir(f"./renamed/{voice}/station/e")
    ]
    stationsM = [
        x.replace(".mp3", "") for x in getMp3InDir(f"./renamed/{voice}/station/m")
    ]
    stationsE = [x for x in stationsE if len(x) == 3]
    stationsM = [x for x in stationsM if len(x) == 3]

    stationsBodgeE = [
        x.replace(".mp3", "") for x in getMp3InDir(f"./custom/{voice}/station/e")
    ]
    stationsBodgeM = [
        x.replace(".mp3", "") for x in getMp3InDir(f"./custom/{voice}/station/m")
    ]
    stationsBodgeE = [x for x in stationsBodgeE if len(x) == 3]
    stationsBodgeM = [x for x in stationsBodgeM if len(x) == 3]

    # Get files in both folders
    stationAudios = set(stationsE) & set(stationsM)

    missingStations = []

    bodgeMax = 2

    for station in stations:
        if station["crs"] not in stationAudios:
            bodgeCount = 0

            if station["crs"] in stationsBodgeE:
                bodgeCount += 1
            if station["crs"] in stationsBodgeM:
                bodgeCount += 1

            bodgeEmoji = "❌"

            if bodgeCount == bodgeMax:
                bodgeEmoji = "✅"
            elif bodgeCount > 0:
                bodgeEmoji = "⚠️"

            missingStations.append(
                f'|{station["name"]}|{station["crs"]}|{bodgeEmoji} {bodgeCount}/{bodgeMax}'
            )

    return missingStations


for voice in ["Male1", "Female1"]:
    miss = getMissingStations(voice)
    print(f"### Missing stations for {voice} ({len(miss)})")
    print("\n|Station name|CRS code|Bodged?|")
    print("|---|---|---|")
    print("\n".join(miss))
    print()
