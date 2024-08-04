# coding: Windows-1251

import os
import json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=r'C:\My_study\Seropyan_DZ\logs\utils.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске
logger = logging.getLogger("utils")


PATH_TO_FILE = os.path.join(os.path.dirname(os.getcwd()), "data", "operations.json")


def transactions(path=PATH_TO_FILE) -> list[dict]:
    """
    Функция возвращающая список транзакций
    """
    try:
        logger.info("Запуск функции вывода списка транзакций")
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception:
        logger.error(f"Ошибка файла по пути: {path}")
        return []


print(transactions())
