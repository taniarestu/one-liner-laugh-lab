"""Entry for make.fun: One-Liner Laugh Lab.

Writes the single entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "I did not eat your sock. I merely relocated it to a secure facility under the couch, where it will be processed indefinitely."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

# ENTRY is 125 characters, inside the 200-character gate.
