"""Write the meeting-email entry line to /output/entry.txt."""

from pathlib import Path

ENTRY_TEXT = (
    "Nine people, one hour, zero decisions. "
    "The email it should have been is still in drafts, thriving."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry() -> None:
    """Create /output if needed and write the entry exactly, no newline added."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
