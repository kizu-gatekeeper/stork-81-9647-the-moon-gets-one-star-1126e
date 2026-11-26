"""Entry program for the make.fun "The Moon Gets One Star" bounty.

It writes a single funny one-star review of the Moon to entry.txt
inside the output directory make.fun hands it through
MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = "One star. Great lighting, zero Wi-Fi, and it shows up uninvited every single night. Would not orbit again."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

if __name__ == "__main__":
    main()
