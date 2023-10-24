import csv
import os

# Config
names = ["Male1"]
output_dir = "renamed/"

# Globals
root = os.path.dirname(os.path.realpath(__file__))
full_out_dir = os.path.join(root, output_dir)

renamed = {}

if not os.path.exists(full_out_dir):
    os.mkdir(full_out_dir)


############################################################


def get_path_to_snippet(voice: str, snippet: str) -> str:
    return os.path.join(root, "mp3s", voice, f"{snippet}.mp3")


def get_path_to_csv(voice: str) -> str:
    return os.path.join(root, f"{voice}_transcriptions.csv")


def read_csv(path: str):
    with open(path) as f:
        input_file = csv.DictReader(f)

        for l in input_file:
            yield l


def copy(old, new):
    if os.path.exists(new):
        print(f"[WARN] {os.path.basename(old)} File already exists, skipping:", new)

    open(new, "wb").write(open(old, "rb").read())


def process_name(name: str) -> list[str]:
    """
    Process the name to remove any special characters, and to split
    multi-station files into individual files.
    """

    if "/" in name:
        # Split multi-station files into individual files
        return [x for x in process_name(n.strip()) for n in name.split("/")]

    return [name.replace("'", "").replace("?", "")]


############################################################


for name in names:
    print(f"Processing {name}")

    renamed[name] = {}

    for entry in read_csv(get_path_to_csv(name)):
        # Get every record in the CSV
        for inflection in entry["inflection"].split(","):
            base = os.path.join(full_out_dir, inflection)

            if not os.path.exists(base):
                # Make path to snippet if not exists
                os.mkdir(base)

            for n in process_name(entry["script"]):
                if n not in renamed[name]:
                    renamed[name][n] = {}

                if inflection not in renamed[name][n]:
                    renamed[name][n][inflection] = 1
                else:
                    renamed[name][n][inflection] += 1

                count = renamed[name][n][inflection]

                # Copy the snippet to the new location
                copy(
                    get_path_to_snippet(name, entry["id"]),
                    os.path.join(base, f"{n}{f'-{count}' if count > 1 else ''}.mp3"),
                )
