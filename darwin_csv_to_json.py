import csv
import json

with open("./DarwinDelayCodes.csv", "r") as f:
    reader = csv.DictReader(f)
    your_list = list(reader)

male1 = {}
female1 = {}

for row in your_list:
    if row["Male1(e)"] != "":
        male1[row["delayCode"]] = {
            "e": row["Male1(e)"],
            "m": row["Male1(m)"],
        }

    if row["Female1(e)"] != "":
        female1[row["delayCode"]] = {
            "e": row["Female1(e)"],
            "m": row["Female1(m)"],
        }

with open("./DarwinDelayCodes_Male1.json", "w") as f:
    json.dump(male1, f, indent=4)

with open("./DarwinDelayCodes_Female1.json", "w") as f:
    json.dump(female1, f, indent=4)
