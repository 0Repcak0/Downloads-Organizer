from pathlib import Path
import shutil
from config import CATEGORIES

DOWNLOADS = Path.home() / "Downloads"


def get_category(extension: str) -> str | None:
    for folder, extensions in CATEGORIES.items():
        if extension in extensions:
            return folder
    return None


def move_file(file: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True)

    destination = target_folder / file.name

    if destination.exists():
        stem = file.stem
        suffix = file.suffix
        counter = 1

        while destination.exists():
            destination = target_folder / f"{stem}_{counter}{suffix}"
            counter += 1

    shutil.move(str(file), str(destination))


def organize_downloads():
    if not DOWNLOADS.exists():
        print("Downloads folder not found.")
        return

    moved = 0

    for file in DOWNLOADS.iterdir():
        if not file.is_file():
            continue

        category = get_category(file.suffix.lower())

        if category:
            target_folder = DOWNLOADS / category
            move_file(file, target_folder)
            moved += 1

    print(f"Done! Moved {moved} files.")


if __name__ == "__main__":
    organize_downloads()
