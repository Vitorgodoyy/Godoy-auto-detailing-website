from pathlib import Path

from PIL import Image, ImageOps


SOURCES = [
    ("mini-countryman-raynes-park-01.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=43A60BE9-E637-4A53-A25D-C1A0A892706A&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2437.jpeg"),
    ("mini-countryman-raynes-park-02.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=5B1C1204-589E-4F93-B562-BFA5F46A8584&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2463.jpeg"),
    ("mini-countryman-raynes-park-03.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=6603CD0B-B34E-4125-A1B7-11E57BB2774D&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2462.jpeg"),
    ("mini-countryman-raynes-park-04.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=19D9AC0A-E3D9-4410-9D2B-1CEB35EB903C&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2426.jpeg"),
    ("mini-countryman-raynes-park-05.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=A55FE8F7-7514-425E-ACB1-FF77F5BBCAC9&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2446.jpeg"),
    ("mini-countryman-raynes-park-06.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=3FD7632B-1274-4E18-B2A9-F74021568F45&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2429.jpeg"),
    ("mini-countryman-raynes-park-07.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=D20EA081-8771-4235-99EF-1EBA17F5FBD0&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2448.jpeg"),
    ("mini-countryman-raynes-park-08.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=267C9008-340E-4672-8F52-C6680392033A&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2432.jpeg"),
    ("mini-countryman-raynes-park-09.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=89037DF7-B89A-4CA7-93EE-6AB178D0225D&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2440.jpeg"),
    ("mini-countryman-raynes-park-10.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=134BDFB5-4FD3-431E-A4AC-C7447EE490F1&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2435.jpeg"),
]


def main() -> None:
    out_dir = Path("assets/gallery/mini-countryman-raynes-park")
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
