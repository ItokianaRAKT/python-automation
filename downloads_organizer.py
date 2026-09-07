from pathlib import Path
from watchfiles import watch

DOWNLOADS = Path.home() / "Téléchargements"
CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".odt"},
    "Archives": {".zip", ".tar", ".gz", ".7z", ".rar"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".webm"},
    "Music": {".mp3", ".wav", ".flac", ".ogg"},
    "Programs": {".exe", ".deb", ".rpm", ".AppImage"},
    "Ebooks": {".epub"}
}

def get_category(file: Path ) -> str:
    for category, extension in CATEGORIES.items():
        if file.suffix.lower() in extension:
            return category
    return "Others"

def organize_file (file: Path):
    if not file.is_file():
        return
    category = get_category(file)
    destination = DOWNLOADS / category
    destination.mkdir(exist_ok=True)
    new_path = destination / file.name
    file.rename(new_path)
    print(f"{file.name} → {category}/")

def main():
    print(f"Watching: {DOWNLOADS}")

    for file in DOWNLOADS.iterdir():
        organize_file(file)

    for changes in watch(DOWNLOADS):
        for change, path in changes:
            file = Path(path)

            if file.parent == DOWNLOADS:
                organize_file(file)


if __name__ == "__main__":
    main()
