import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
        self.IMAGES_FOLDER = os.getenv('IMAGES_FOLDER', 'images')