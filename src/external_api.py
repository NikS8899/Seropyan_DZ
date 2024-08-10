# coding: Windows-1251
import os
from dotenv import load_dotenv
import requests


def transaction_amount(transaction):
    """
    Функция конвертации валюты в рубли
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        load_dotenv()
        token = os.getenv("API-KEY")
        url = "https://api.apilayer.com/exchangerates_data/convert"
        amount = str(transaction["operationAmount"]["amount"])
        from_ = transaction["operationAmount"]["currency"]["code"]
        payload = {"amount": amount, "from": from_, "to": "RUB"}
        headers = {"apikey": token}

        response = requests.get(url, headers=headers, params=payload)

        result = response.json()

        return result["result"]


