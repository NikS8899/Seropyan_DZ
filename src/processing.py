from typing import Any


def filter_by_state(
        my_list: list[dict[str, int | str]], state: str = "EXECUTED"
) -> list[dict[str, int | str]]:
    """Возвращает список словарей по ключу state"""
    new_list = []
    for element in my_list:
        if element.get("state") == state:
            new_list.append(element)
    return new_list


def sort_by_date(my_list: Any, sequence: bool = True) -> list[dict[str, int | str]]:
    """Функция сортировки по дате"""

    sorted_by_date = sorted(
        my_list, key=lambda x: (x.get("date")[:10]).split("-"), reverse=sequence
    )

    return sorted_by_date
