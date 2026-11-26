"""The Printer Apology — make.fun entry.

An office printer apologises, in a single line, to the people who keep
jamming it, feeding it cheap paper and swearing at it. Writes that line
to entry.txt inside the output directory.

Stdlib only. No network, no randomness, fully deterministic.
"""

import os

MAX_CHARS = 120
OUTPUT_NAME = "entry.txt"

def raw_apology():
    """Return the printer's apology as written, before normalisation."""
    return (
        "Sorry I jammed on deadline day — you feed me cheap paper, swear at "
        "me, and still expect miracles on empty toner."
    )


def build_apology():
    """Return the apology line, enforcing the 120-character gate."""
    line = " ".join(raw_apology().split())
    if not line:
        raise SystemExit("apology line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "apology line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(build_apology())


if __name__ == "__main__":
    main()
