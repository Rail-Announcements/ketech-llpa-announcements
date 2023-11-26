# Read in csv and reoutput as formatted csv
import csv

csvs = [
    "Male1_transcriptions",
    "Male3_transcriptions",
    "Female1_transcriptions",
    "Female2_transcriptions",
    "default_transcriptions",
]

defaultKeys = [
    "id",
    "script",
    "inflection",
    "comment",
    "type",
    "suppress",
]


def format(path: str, keys: list):
    print(f"Formatting {path}.csv")

    # Read in csv
    with open(f"{path}.csv", "r") as f:
        reader = csv.DictReader(f)
        your_list = list(reader)

    # Create new csv
    with open(f"{path}_formatted.csv", "w") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=keys,
        )

        # Write header
        writer.writeheader()

        # Write rows
        for row in your_list:
            try:
                writer.writerow({k: row[k] for k in keys})
            except KeyError as e:
                print(f"KeyError in {path}.csv")
                print(row)
                print(e)
                break


for c in csvs:
    format(c, defaultKeys)

format("DarwinDelayCodes", ["delayCode", "description", "Male1", "Female1"])
