from pathlib import Path
import sys

from PIL import Image


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: remove_black_background.py input output", file=sys.stderr)
        return 2

    source = Image.open(sys.argv[1]).convert("RGBA")
    pixels = source.load()
    width, height = source.size

    for y in range(height):
        for x in range(width):
            r, g, b, _ = pixels[x, y]
            max_channel = max(r, g, b)

            if max_channel <= 18:
                alpha = 0
            elif max_channel >= 58:
                alpha = 255
            else:
                alpha = round((max_channel - 18) / 40 * 255)

            pixels[x, y] = (r, g, b, alpha)

    bbox = source.getbbox()
    if not bbox:
        print("No logo pixels found", file=sys.stderr)
        return 1

    padding = 24
    left, top, right, bottom = bbox
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(width, right + padding)
    bottom = min(height, bottom + padding)

    output = source.crop((left, top, right, bottom))
    output_path = Path(sys.argv[2])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.save(output_path)

    print(f"{output.size[0]}x{output.size[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
