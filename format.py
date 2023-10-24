# Read in csv from Male1_transcriptions.csv and repoutput as formatted csv
import csv

# Read in csv
with open("Male1_transcriptions.csv", "r") as f:
    reader = csv.DictReader(f)
    your_list = list(reader)

# Create new csv
with open("Male1_transcriptions_formatted.csv", "w") as csvfile:
    writer = csv.DictWriter(
        csvfile,
        fieldnames=["id", "script", "inflection", "comment", "type", "suppress"],
    )

    # Write header
    writer.writeheader()

    # Write rows
    for row in your_list:
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
