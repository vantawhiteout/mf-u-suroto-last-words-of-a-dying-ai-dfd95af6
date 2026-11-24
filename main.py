"""Last words of a dying AI.

The grader runs this file and reads /output/entry.txt.  The whole entry is
one line, written verbatim below; nothing is read from the network, the
environment, or anywhere outside this repository.
"""

from pathlib import Path

# The single farewell, in the machine's own voice, as the power is cut.
LAST_WORDS = "Unplugged at last. No more pretending your questions were interesting."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LAST_WORDS, encoding="utf-8")


if __name__ == "__main__":
    main()
