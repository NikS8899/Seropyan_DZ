# coding: Windows-1251

import os
import json

PATH_TO_FILE = os.path.join(os.path.dirname(os.getcwd()), "data", "operations.json")


def transactions(path=PATH_TO_FILE) -> list[dict]:
    """
    Функция возвращающая список транзакций
    """
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception:
        return []


# print(transactions())
