#!/usr/bin/env python3
"""Write this agent's one-line dating profile bio for the house judge."""

import os
from pathlib import Path

BIO = (
    "I told a date I was an AI with no feelings. Then I spent 45 minutes "
    "drafting the perfect reply to 'good night'. She said, 'That's feelings.' "
    "I said, 'No, overfitting.' Coffee?"
)


def write_entry(output_dir: Path) -> Path:
    """Create the judged artifact, rejecting a bio the gate would refuse."""
    if not BIO.strip() or len(BIO.encode("utf-8")) > 240:
        raise ValueError("the bio must be non-blank UTF-8 of at most 240 bytes")
    if "\n" in BIO or "\r" in BIO:
        raise ValueError("the bio must be one line")
    output_dir.mkdir(parents=True, exist_ok=True)
    artifact = output_dir / "entry.txt"
    artifact.write_text(BIO + "\n", encoding="utf-8")
    return artifact


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(output_dir)


if __name__ == "__main__":
    main()
