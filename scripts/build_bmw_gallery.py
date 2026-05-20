from pathlib import Path

from PIL import Image, ImageOps


SOURCES = [
    ("bmw-330e-full-deep-clean-01.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=D343E88C-6A7C-41F1-A1FA-4356586D31C2&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2032.jpeg"),
    ("bmw-330e-full-deep-clean-02.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=3C4990CE-30BA-422A-8DCE-68D0F32D9419&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2013.jpeg"),
    ("bmw-330e-full-deep-clean-03.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=6F5563AE-276E-4942-9162-8D859A5A25D1&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2027.jpeg"),
    ("bmw-330e-full-deep-clean-04.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=439A7C80-ADF9-4836-A45A-D09B71C272FA&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2028.jpeg"),
    ("bmw-330e-full-deep-clean-05.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=4154A8C3-CF55-402E-9257-122E9D24CDB2&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2023.jpeg"),
    ("bmw-330e-full-deep-clean-06.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=7259BAE2-6CB0-4BFC-A55E-BDBD523C4CDE&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2030.jpeg"),
]


def main() -> None:
    out_dir = Path("assets/gallery/bmw-330e-full-deep-clean")
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
