import os


def open_downloads_resources():
    if os.system("exo-open --working-directory ./downloads --launch FileManager") != 0:
        print("Failed to open downloads folder. Verify that you use Kali linux distributive for running this program")


def get_dir_size(path='./downloads'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return float(total) / 1000.0  # in kilobytes


def clean_folder(path='./downloads'):
    folder_items = os.listdir(path)
    for item in folder_items:
        os.remove(os.path.join(path, item))
