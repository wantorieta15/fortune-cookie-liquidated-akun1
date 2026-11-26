"""Fortune Cookie for the Liquidated Trader — Make Fun entry (Akun 1).

Reviser rewrite: builds the single-line fortune cookie entry, validates
it (one line, no newline, exact sha256), and writes it directly to
<out_dir>/entry.txt with mode 0644. Pure standard library only.

Entry (103 bytes, sha256 87b49211b7c1c88550e73772b3f8e06c8788f96088dfa2ffce92eb2e50b3de3c):
    Your bags will find an owner at the bottom. He is you, three
    liquidations from now, and he says thanks.
"""

import hashlib
import os

EXPECTED_SHA256 = (
    "87b49211b7c1c88550e73772b3f8e06c8788f96088dfa2ffce92eb2e50b3de3c"
)
EXPECTED_BYTES = 103

ENTRY = (
    "Your bags will find an owner at the bottom. "
    "He is you, three liquidations from now, and he says thanks."
)


def build_entry():
    """Return the entry text exactly as submitted."""
    return ENTRY


def validate_entry(text):
    """Check the entry is a single line without a trailing newline and
    matches the expected byte length and sha256. Raises ValueError on
    any mismatch so a wrong entry can never be written silently."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be a non-empty string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line (no newline)")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    raw = text.encode("utf-8")
    if len(raw) != EXPECTED_BYTES:
        raise ValueError(
            "entry must be %d bytes, got %d" % (EXPECTED_BYTES, len(raw))
        )
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError("entry sha256 mismatch: got %s" % digest)
    return raw


def write_entry(out_dir=None):
    """Write the validated entry directly to <out_dir>/entry.txt via
    open() + explicit os.chmod(path, 0o644). No temp files, no rename."""
    if out_dir is None:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    raw = validate_entry(build_entry())
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(raw)
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry()
    print("wrote %s (%d bytes, sha256 %s)" % (path, EXPECTED_BYTES, EXPECTED_SHA256))


if __name__ == "__main__":
    main()
