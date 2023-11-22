# Read in csv and reoutput as formatted csv
import csv

csvs = [
    "Male1_transcriptions",
    "Male3_transcriptions",
    "Female1_transcriptions",
    "Female2_transcriptions",
    "default_transcriptions",
]

for c in csvs:
    print(f"Formatting {c}.csv")
    
    # Read in csv
    with open(f"{c}.csv", "r") as f:
        reader = csv.DictReader(f)
        your_list = list(reader)

    # Create new csv
    with open(f"{c}_formatted.csv", "w") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=["id", "script", "inflection", "comment", "type", "suppress"],
        )

        # Write header
        writer.writeheader()

        # Write rows
        for row in your_list:
            try:
                writer.writerow(
                    {
                        "id": row["id"],
                        "script": row["script"],
                        "inflection": row["inflection"],
                        "comment": row["comment"],
                        "type": row["type"],
                        "suppress": row["suppress"],
                    }
                )
            except KeyError:
                print(f"KeyError in {c}.csv")
                print(row)
                break
