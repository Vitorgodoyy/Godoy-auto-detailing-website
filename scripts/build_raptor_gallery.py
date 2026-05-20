from pathlib import Path

from PIL import Image, ImageOps


SOURCES = [
    ("ford-raptor-ceramic-coating-01.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=D1065C91-3532-471F-A2E8-CCF4F6B2A0E3&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_1984.jpeg"),
    ("ford-raptor-ceramic-coating-02.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=ABED4214-116A-41E9-B629-1EB197670AA3&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_1985.jpeg"),
    ("ford-raptor-ceramic-coating-03.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=35B163B5-9132-492C-9E1E-D5F586C3CEA0&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_1986.jpeg"),
]


def main() -> None:
    out_dir = Path("assets/gallery/ford-raptor-ceramic-coating")
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
