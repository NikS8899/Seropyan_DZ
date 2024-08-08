import re
from src.utils import get_transactions


def find_str_description(my_list: list[dict], search_string) -> list[dict] | str:
    """
    The function of searching for a string in the description
    """
    result_list = []

    for transaction in my_list:
        if re.findall(search_string, str(transaction.get("description")), flags=re.IGNORECASE):
            result_list.append(transaction)
    if result_list == []:
        return f"Строка '{search_string}' не найдена!"
    else:
        return result_list


if __name__ == "__main__":
    new_list = get_transactions(r"C:\My_study\Seropyan_DZ\data\transactions.csv")
    print(find_str_description(new_list, "открытие"))

def counter_of_description(my_list: list[dict]) -> dict:
    new_list = []
    result = {}
    for transaction in my_list:
        new_list.append(transaction.get("state"))
    for item in new_list:
        if item not in result:
            result[item] = 0
        else:
            result[item] += 1
    return result

if __name__ == "__main__":
    new_list = get_transactions(r"C:\My_study\Seropyan_DZ\data\transactions_excel.xlsx")
    print(counter_of_description(new_list))