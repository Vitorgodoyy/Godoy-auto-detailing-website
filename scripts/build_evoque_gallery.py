from pathlib import Path

from PIL import Image, ImageOps


SOURCES = [
    ("range-rover-evoque-full-deep-clean-01.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=604A1791-EB2B-4A3E-B199-A72639300892&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2123.jpeg"),
    ("range-rover-evoque-full-deep-clean-02.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=A6AF84F6-FE9C-4F80-8126-A2B12706C961&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2122.jpeg"),
    ("range-rover-evoque-full-deep-clean-03.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=046D3B6C-9760-4C5C-8D0C-EF3C98593BF3&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2114.jpeg"),
    ("range-rover-evoque-full-deep-clean-04.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=B57F46A5-939D-4EA8-903A-76C969BFCEA9&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2116.jpeg"),
    ("range-rover-evoque-full-deep-clean-05.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=3E532800-E3C7-456B-A354-61428DAA0B8A&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2099.jpeg"),
    ("range-rover-evoque-full-deep-clean-06.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=9F7377E1-B61C-4174-BD78-CB3D8602195D&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2106.jpeg"),
]


def main() -> None:
    out_dir = Path("assets/gallery/range-rover-evoque-full-deep-clean")
    out_dir.mkdir(parents=True, exist_ok=True)

    for filename, source_path in SOURCES:
        image = Image.open(source_path)
        image = ImageOps.exif_transpose(image).convert("RGB")
        image.thumbnail((1800, 1800), Image.Resampling.LANCZOS)
        output = out_dir / filename
        image.save(output, "JPEG", quality=82, optimize=True, progressive=True)
        print(f"{output} {image.size[0]}x{image.size[1]}")


if __name__ == "__main__":
    main()
