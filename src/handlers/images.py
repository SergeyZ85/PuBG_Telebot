from telebot import TeleBot
from telebot.types import Message
from src.services.image_service import ImageService


class ImageHandlers:
    def __init__(self, bot: TeleBot, image_service: ImageService):
        self.bot = bot
        self.image_service = image_service

    def register_handlers(self):
        @self.bot.message_handler(content_types=['text'])
        def handle_text(message: Message):
            search_query = message.text.lower().strip()
            image_path = self.image_service.find_image(search_query)

            if image_path:
                with open(image_path, 'rb') as photo:
                    self.bot.send_photo(
                        message.chat.id,
                        photo,
                        caption=f"Изображение по запросу '{search_query}'"
                    )
            else:
                self.bot.reply_to(
                    message,
                    f"Изображение не найдено. Доступные: {', '.join(self.image_service.get_available_images())}"
                )