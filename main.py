from os import remove, getcwd, listdir, mkdir
from os.path import isfile, isdir

from PIL import Image


result_path: str = getcwd() + "/result/"


def ensure_result_folder_exists():
    path = getcwd() + "/result/"

    if not isdir(path):
        mkdir(path)
        print(f"Creata la cartella {path}")


def get_png_list() -> list:
    file_list: list = []

    for entity in listdir("."):
        if isfile(entity) and entity.split(".")[1].upper() == "PNG" and entity != "iPhoneX.png":
            file_list.append(entity)

    file_list.sort(key=lambda file: int(file.split("_")[1].split(".")[0]))

    print("Trovati: ", file_list)
    return file_list


def delete_files():
    print("Inizio ad eliminare i file...")
    for entity in listdir(result_path):
        if isfile(result_path + entity):
            print("Rimuovo ", entity, ".")
            remove(result_path + entity)


def load_iphone_mockup() -> Image:
    main_mockup: Image = Image.open("iPhoneX.png")

    return main_mockup


# Ci serve che vada da 623 a 1388 e da 180 a 1813.
def resize_screenshot(screenshot: Image) -> Image:
    return screenshot.resize((765, 1633))


def main():
    ensure_result_folder_exists()

    project_name: str = input("Inserisci nome progetto: ")
    delete: str = input("Eliminare i files esistenti? [Y/n]: ") or "Y"
    if delete.upper() == "Y":
        delete_files()

    iphone_mockup: Image = load_iphone_mockup()
    screenshot_path: list = get_png_list()

    for index in range(len(screenshot_path)):
        print("[" + str(round(index / len(screenshot_path), 4) *
                        100) + "%] " + "Processo ", screenshot_path[index])

        final: Image = Image.new("RGBA", (2000, 2000))
        screenshot: Image = resize_screenshot(
            Image.open(screenshot_path[index]))

        final.alpha_composite(screenshot, dest=(623, 180))
        final.alpha_composite(iphone_mockup)

        final.save("result/SCREENSHOT-" + project_name +
                   "-" + str(index + 1) + ".png")


main()
