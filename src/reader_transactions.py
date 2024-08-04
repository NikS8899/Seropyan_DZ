# coding: utf-8
import pandas as pd


def get_transaction(path):
    """
    Функция чтения файла с транзакциями
    """
    if "xlsx" in path:
        trans_excel = pd.read_excel(path)
        return trans_excel
    elif "csv" in path:
        trans_csv = pd.read_csv(path)
        return trans_csv
    else:
        raise ValueError("Неверное расширение или файл отсутствует")


print(get_transaction(r"C:\My_study\Seropyan_DZ\transactions.csv"))
