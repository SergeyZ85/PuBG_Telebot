# src/utils/logger.py
import logging
import sys
from pathlib import Path
from typing import Optional


def get_logger(
        name: str,
        log_file: Optional[str] = "bot.log",
        log_dir: str = "logs",
        level: int = logging.INFO,
        console: bool = True
) -> logging.Logger:
    """
    Создает и настраивает логгер с выводом в файл и консоль.

    Параметры:
        name (str): Имя логгера (обычно __name__)
        log_file (str, optional): Имя файла для логов. По умолчанию "bot.log"
        log_dir (str): Директория для хранения логов. По умолчанию "logs"
        level (int): Уровень логирования. По умолчанию logging.INFO
        console (bool): Вывод в консоль. По умолчанию True

    Возвращает:
        logging.Logger: Настроенный экземпляр логгера
    """
    # Создаем директорию для логов, если ее нет
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)

    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Формат сообщений
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Обработчик для записи в файл
    file_handler = logging.FileHandler(log_path / log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Обработчик для вывода в консоль (если требуется)
    if console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # Запрещаем передачу логов родительским логгерам
    logger.propagate = False

    return logger