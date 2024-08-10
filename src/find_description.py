import re
from collections import Counter
from typing import Any


def find_str_description(my_list: list[dict], search_string) -> list[dict] | str:
    """
    The function of searching for a string in the description
    """
    result_list = []

    for transaction in my_list:
        if re.findall(search_string, str(transaction.get("description")), flags=re.IGNORECASE):
            result_list.append(transaction)
        return result_list


def counter_of_description(my_list: list[Any]) -> dict:
    new_list = []
    for transaction in my_list:
        new_list.append(transaction.get("description"))
    counted = Counter(new_list)
    return counted

