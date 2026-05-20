from pathlib import Path

from PIL import Image, ImageOps


SOURCES = [
    ("range-rover-velar-raynes-park-01.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=10DAA2D7-3F04-4E85-A2F3-EBE90E3B8A2F&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2475.jpeg"),
    ("range-rover-velar-raynes-park-02.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=B6B75218-5748-42D3-977F-05155B91F6E1&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2478.jpeg"),
    ("range-rover-velar-raynes-park-03.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=5B99634D-AF92-4908-8488-466C1BA85CB6&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2486.jpeg"),
    ("range-rover-velar-raynes-park-04.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=FA0B4460-F324-461E-A466-0BF4A963E841&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2484.jpeg"),
    ("range-rover-velar-raynes-park-05.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=5CDAA836-5E83-4FBD-8D39-BC8D59E4495E&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2483.jpeg"),
    ("range-rover-velar-raynes-park-06.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=A3305696-DEA8-494E-AAD1-AF067624E71D&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2489.jpeg"),
    ("range-rover-velar-raynes-park-07.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=D245F9E0-7E1F-4765-9D77-EC39F3CFF6CE&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2471.jpeg"),
]


def main() -> None:
    out_dir = Path("assets/gallery/range-rover-velar-raynes-park")
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
