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


def sort_by_date(
        my_list: list[dict[str, int | str]], sequence: bool = True
) -> list[dict[str, int | str]]:
    """Функция сортировки по дате"""

    def return_split_date(date: str) -> tuple[int, int, int]:
        """Возвращает дату в виде кортежа для ключа сортировки"""
        new_format = date.split(".")
        day = int(new_format[0])
        month = int(new_format[1])
        year = int(new_format[2])
        return year, month, day

    sorted_by_date = sorted(
        my_list,
        key=lambda x: return_split_date(get_data(x.get("date"))),
        reverse=sequence,
    )

    return sorted_by_date
