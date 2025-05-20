import os
from pathlib import Path
from typing import Optional, List


class ImageStorage:
    def __init__(self, images_folder: str):
        self.images_folder = Path(images_folder)
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        self.images_folder.mkdir(exist_ok=True)

    def find_image(self, query: str) -> Optional[str]:
        print(self.images_folder)
        for file in self.images_folder.iterdir():
            query=query[1:]
            if query in file.stem.lower() and file.suffix.lower() in ['.jpg', '.png', '.jpeg']:

                return str(file)
        return None

    def get_available_images(self) -> List[str]:
        return [file.stem for file in self.images_folder.iterdir()
                if file.suffix.lower() in ['.jpg', '.png', '.jpeg']]