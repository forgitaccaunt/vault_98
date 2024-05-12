import logging
import sys


format_1 = '[{asctime}][{levelname:8}] {filename}: '\
           '{lineno} - {name} - {message}'

formatter_1 = logging.Formatter(fmt=format_1, style='{')

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('logs.log', encoding='utf-8')

logger.addHandler(file_handler)

logger.warning('Это лог с прдупреждением!')
