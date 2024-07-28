# coding: Windows-1251
import os
from dotenv import load_dotenv
import requests


def transaction_amount(transaction):
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        load_dotenv()
        token = os.getenv("API-KEY")
        url = "https://api.apilayer.com/exchangerates_data/convert"
        amount = str(transaction["operationAmount"]["amount"])
        from_ = transaction["operationAmount"]["currency"]["code"]
        payload = {
            "amount": amount,
            "from": from_,
            "to": "RUB"
        }
        headers = {
            "apikey": token
        }

        response = requests.get(url, headers=headers, params=payload)

        result = response.json()

        return result["result"]


print(transaction_amount({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
}))
