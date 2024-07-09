from typing import Any

from src.widget import get_data


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
    for dict in my_list:
        get_data(dict.get("date"))
    sorted_by_date = sorted(
        my_list, key=lambda x: (x.get("date")[:10]).split("-"), reverse=sequence
    )

    return sorted_by_date


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ],
        False,
    )
)
