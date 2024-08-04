# coding: utf-8
import pandas as pd


def get_transaction(path):
    """
    The function of reading a file with transactions
    param 1: path to file
    return: list of dict
    """
    if "xlsx" in path:
        trans_excel = pd.read_excel(path)
        return trans_excel.to_dict(orient='records')
    elif "csv" in path:
        trans_csv = pd.read_csv(path)
        return trans_csv.to_dict(orient='records')
    else:
        raise ValueError("Неверное расширение или файл отсутствует")
