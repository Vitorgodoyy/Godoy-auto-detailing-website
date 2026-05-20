from pathlib import Path

from PIL import Image, ImageOps


SOURCES = [
    ("porsche-macan-s-enhancement-01.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=94338510-3873-4448-A83C-63A940A832D7&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2184.jpeg"),
    ("porsche-macan-s-enhancement-02.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=A5FFFD24-8E0E-4C43-85E0-C76C8402BA90&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2185.jpeg"),
    ("porsche-macan-s-enhancement-03.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=4EFB85D2-003B-45CA-A7B8-06A1CD8709CB&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2178.jpeg"),
    ("porsche-macan-s-enhancement-04.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=3918C841-2636-4087-A609-4678328EC4BC&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2188.jpeg"),
    ("porsche-macan-s-enhancement-05.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=B6CC77BD-EC28-4283-8932-B2D4176C4146&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2190.jpeg"),
    ("porsche-macan-s-enhancement-06.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=FB823282-37A6-4E3B-ABE0-672D12309FF5&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2195.jpeg"),
    ("porsche-macan-s-enhancement-07.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=87554B10-CF3B-41F5-A89B-52D3D98E9A76&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2201.jpeg"),
    ("porsche-macan-s-enhancement-08.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=F232416B-F201-4D1F-84E8-4AE1037AAF09&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2170.jpeg"),
    ("porsche-macan-s-enhancement-09.jpg", "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=CE624DB0-88CF-416D-840E-26609E17483D&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_2186.jpeg"),
]


def main() -> None:
    out_dir = Path("assets/gallery/porsche-macan-s-enhancement")
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
