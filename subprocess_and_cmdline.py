from asyncio import subprocess
from sys import stdout


import subprocess

FNAME = "dump.txt"

with open(FNAME, "w") as f:
    subprocess.call(['ls', '-l'], stdout=f)

print(f"Command line output written to {FNAME}.")
