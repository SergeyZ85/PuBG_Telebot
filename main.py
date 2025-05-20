import os
import sys
from pathlib import Path

# Добавляем src в путь для импортов
sys.path.append(str(Path(__file__).parent))

from src.utils.config import Config
from src.handlers import register_handlers
from telebot import TeleBot

def setup_bot() -> TeleBot:
    """Инициализация и настройка бота"""
    config = Config()
    bot = TeleBot(config.TELEGRAM_TOKEN)
    register_handlers(bot)
    return bot

def main():
    try:
        bot = setup_bot()
        print("Бот запущен. Остановите сочетанием Ctrl+C")
        bot.infinity_polling()
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()