from telebot import TeleBot
from telebot.types import Message
from src.utils.logger import get_logger

logger = get_logger(__name__)


class CommandHandlers:
    def __init__(self, bot: TeleBot, image_service):
        self.bot = bot
        self.image_service = image_service

    def register_commands(self):
        """Регистрирует все обработчики команд"""
        self._register_start_command()
        self._register_help_command()
        self._register_list_command()

    def _register_start_command(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message: Message):
            try:
                welcome_msg = (
                    "🖼️ Бот для поиска изображений\n\n"
                    "Доступные команды:\n"
                    "/start - Начало работы\n"
                    "/help - Помощь\n"
                    "/list - Список изображений\n\n"
                    "Просто отправьте название изображения для поиска"
                )
                self.bot.reply_to(message, welcome_msg)
                logger.info(f"User {message.from_user.id} started the bot")
            except Exception as e:
                logger.error(f"Start command error: {e}", exc_info=True)
                self.bot.reply_to(message, "⚠️ Произошла ошибка")

    def _register_help_command(self):
        @self.bot.message_handler(commands=['help'])
        def handle_help(message: Message):
            help_msg = (
                "ℹ️ Помощь по использованию бота:\n\n"
                "1. Отправьте название изображения для поиска\n"
                "2. Используйте /list для просмотра доступных\n"
                "3. Администраторы могут добавлять новые изображения"
            )
            self.bot.reply_to(message, help_msg)

    def _register_list_command(self):
        @self.bot.message_handler(commands=['list'])
        def handle_list(message: Message):
            try:
                images = self.image_service.get_available_images()
                if not images:
                    self.bot.reply_to(message, "📭 Нет доступных изображений")
                    return

                response = "📂 Доступные изображения:\n\n" + "\n".join(
                    f"• {name}" for name in sorted(images)[:20]
                )

                if len(images) > 20:
                    response += f"\n\n...и ещё {len(images) - 20} изображений"

                self.bot.reply_to(message, response)
                logger.debug(f"Sent image list to {message.from_user.id}")
            except Exception as e:
                logger.error(f"List command error: {e}", exc_info=True)
                self.bot.reply_to(message, "⚠️ Ошибка при получении списка")