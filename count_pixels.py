from PIL import Image


def count_pixels(file_path: str) -> int:
    with Image.open(file_path) as img:
        width, height = img.size
    return width * height


if __name__ == "__main__":
    print(count_pixels("ukraine_sample.tif"))
