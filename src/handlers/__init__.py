from .commands import CommandHandlers
from .images import ImageHandlers
from src.services.image_service import ImageService
from src.utils.config import Config


def register_handlers(bot: 'TeleBot'):
    """Регистрация всех обработчиков команд и сообщений"""
    config = Config()
    image_service = ImageService(images_folder=config.IMAGES_FOLDER)

    # Инициализация и регистрация обработчиков
    CommandHandlers(bot, image_service).register_commands()
    ImageHandlers(bot, image_service).register_handlers()