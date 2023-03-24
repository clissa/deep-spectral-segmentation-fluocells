"""Scrit for getting list of filenames."""
from pathlib import Path

IMAGE_PATH = Path().cwd() / 'data' / 'CTB' / 'test' / 'images'

def get_file_list():
    """Write list of all filenames present in `IMAGE_PATH`.
    """
    names_list = [fp.name for fp in IMAGE_PATH.iterdir()]

    outpath = IMAGE_PATH.parent / 'lists'
    outpath.mkdir(exist_ok=True, parents=True)

    with open(outpath / 'images.txt', 'w', encoding='utf-8') as file:
        for filename in names_list:
            file.write(f"{filename}\n")

if __name__=='__main__':
    get_file_list()
