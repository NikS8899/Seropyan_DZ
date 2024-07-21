from itertools import chain
from typing import Any, Iterator


def filter_by_currency(
    list_of_transactions: list[dict], currency: str
) -> Iterator[dict]:
    """Функция фильтрации операций по коду использованной валюте"""
    for operation in list_of_transactions:
        try:
            if operation["operationAmount"]["currency"]["code"] == currency:
                yield operation
        except KeyError:
            print("Значение не найдено!")


def transaction_descriptions(list_of_transactions: list[Any]) -> Iterator[list]:
    """Функция генерации описания операций"""
    for description in list_of_transactions:
        try:
            yield description["description"]
        except KeyError:
            print("Операция не найдена!")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Функция генерации номеров карт в формате XXXX XXXX XXXX XXXX"""
    default_card_number = list("0000000000000000")
    for i in range(start, stop + 1):
        num_list = list(chain(default_card_number, list(str(i))))
        while True:
            if len(num_list) == 16:
                unity_list = "".join(num_list)
                yield " ".join(
                    [unity_list[i: i + 4] for i in range(0, len(unity_list), 4)]
                )
                break
            else:
                del num_list[0]
