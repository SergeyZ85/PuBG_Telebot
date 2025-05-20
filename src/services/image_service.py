import os
from pathlib import Path
from src.storage.image_storage import ImageStorage


class ImageService:
    def __init__(self, images_folder: str):
        self.storage = ImageStorage(images_folder)

    def find_image(self, query: str) -> str:
        return self.storage.find_image(query)

    def get_available_images(self) -> list:
        return self.storage.get_available_images()