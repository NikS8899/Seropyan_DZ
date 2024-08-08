# coding: Windows-1251
import pandas as pd
import os
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=r"C:\My_study\Seropyan_DZ\logs\utils.log",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске
logger = logging.getLogger("utils")


JSON_PATH_TO_FILE = os.path.join(os.path.dirname(os.getcwd()), "data", "operations.json")
EXCEL_PATH_TO_FILE = os.path.join(os.path.dirname(os.getcwd()), "data", "transaction_excel.xlsx")
CSV_PATH_TO_FILE = os.path.join(os.path.dirname(os.getcwd()), "data", "transaction.csv")

def get_transactions(path=JSON_PATH_TO_FILE) -> list[dict]:
    """
    Функция возвращающая список транзакций
    """
    try:
        if "xlsx" in path:
            logger.info("Запуск функции вывода списка транзакций из excel файла")
            trans_excel = pd.read_excel(path)
            return trans_excel.to_dict(orient='records')
        elif "csv" in path:
            logger.info("Запуск функции вывода списка транзакций из csv файла")
            trans_csv = pd.read_csv(path, delimiter=";")
            return trans_csv.to_dict(orient='records')
        elif "json" in path:
            logger.info("Запуск функции вывода списка транзакций из json файла")
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
                return data
    except Exception:
        logger.error(f"Ошибка файла по пути: {path}")
        return []


if __name__ == "__main__":
    print(get_transactions())
