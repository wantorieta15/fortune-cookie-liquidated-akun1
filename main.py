"""Fortune Cookie for the Liquidated Trader — Make Fun entry (Akun 1).

Writes the single-line fortune cookie entry to <out_dir>/entry.txt.
Pure standard library only.
"""

import os

ENTRY = "Your bags will find an owner at the bottom. He is you, three liquidations from now, and he says thanks."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
