import os
from pathlib import Path

LINE = "Frustrated by earphone cords tangling in your pockets, the SnakeCord features a tiny motorized jaw that bites its own tail into an eternal reptilian hoop whenever it senses the enclosed darkness of denim."

def main():
    """Write required sentence to entry.txt in the specified output directory."""
# Entry validated: output is 1-220 chars, one sentence, deterministic.
    content = LINE + "\n"
    if not (1 <= len(content) <= 220 and content.strip()):
        raise ValueError("Invalid content")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(content, encoding="utf-8")
    print(f"{path} {len(content)}")

if __name__ == "__main__":
    main()
