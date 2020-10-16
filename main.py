from os import listdir
from os.path import isfile

from PIL import Image


def get_png_list() -> list:
    file_list: list = []

    for entity in listdir("."):
        if isfile(entity) and entity.split(".")[1] == "PNG" and entity != "iPhoneX.png":
            file_list.append(entity)

    print("Trovati: ", file_list)
    return file_list


def load_iphone_mockup() -> Image:
    main_mockup: Image = Image.open("iPhoneX.png")

    return main_mockup


# Ci serve che vada da 623 a 1388 e da 180 a 1813.
def resize_screenshot(screenshot: Image) -> Image:
    return screenshot.resize((765, 1633))


def main():
    get_png_list()
    iphone_mockup: Image = load_iphone_mockup()

    for screenshot_path in get_png_list():
        print("Processo ", screenshot_path)

        final: Image = Image.new("RGBA", (2000, 2000))
        screenshot: Image = resize_screenshot(Image.open(screenshot_path))

        final.alpha_composite(screenshot, dest=(623, 180))
        final.alpha_composite(iphone_mockup)

        final.save("result/" + screenshot_path.split()[0] + "-N.png")


main()
