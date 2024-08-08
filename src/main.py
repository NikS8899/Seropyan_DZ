# coding: Windows-1251
from src.find_description import find_str_description
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transactions
from src.widget import get_data, mask_account_card
import os

JSON_PATH_TO_FILE = os.path.join(os.path.dirname(os.getcwd()), "data", "operations.json")
EXCEL_PATH_TO_FILE = os.path.join(os.path.dirname(os.getcwd()), "data", "transactions_excel.xlsx")
CSV_PATH_TO_FILE = os.path.join(os.path.dirname(os.getcwd()), "data", "transactions.csv")


def main():
    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.\n\
    Выберите необходимый пункт меню:\n\
    1. Получить информацию о транзакциях из JSON-файла\n\
    2. Получить информацию о транзакциях из CSV-файла\n\
    3. Получить информацию о транзакциях из XLSX-файла\n")

    while True:
        choice_format_file = input("Введите пункт меню: ")
        if choice_format_file == "1":
            transaction = get_transactions()

            print("Для обработки выбран JSON-файл.\n")
            break
        elif choice_format_file == "2":
            transaction = get_transactions(CSV_PATH_TO_FILE)
            print("Для обработки выбран CSV-файл.\n")
            break
        elif choice_format_file == "3":
            transaction = get_transactions(EXCEL_PATH_TO_FILE)
            print("Для обработки выбран EXCEL-файл.\n")
            break

        else:
            print("Пункт отсутствует, повторите ввод.\n")
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки "
              "статусы: EXECUTED, CANCELED, PENDING\n")
        state = input("Введите статус: ")

        states_list = ["EXECUTED", "CANCELED", "PENDING"]

        if state.upper() in states_list:
            transaction = filter_by_state(transaction, state.upper())
            if transaction == []:
                print(f"По статусу '{state.upper()}' операции отсутствуют, выберите другой статус.")
                continue
            break
        else:
            print(f"Статус операции '{state}' недоступен.\n")

    print("\nОтсортировать операции по дате?\n")
    sort_answer = input("Да/Нет: ")
    if sort_answer.lower() == "да":
        print("Отсортировать по возрастанию(1) или по убыванию(2)?")
        while True:
            sequence_answer = input("\nВведите ответ 1 / 2: ")
            if sequence_answer.lower() == "1":
                transaction = sort_by_date(transaction, False)
                break
            elif sequence_answer.lower() == "2":
                transaction = sort_by_date(transaction)
                break
            else:
                print("Введен неверный индекс!\nДля сортировки по возрастанию введите цифру '1' "
                      "для сортировки по убыванию введите цифру '2'\n")

    sort_by_ruble_answer = input("\nВыводить только рублевые транзакции? Да/Нет: ")
    if sort_by_ruble_answer.lower() == "да":
        sort_by_ruble_list = [x for x in transaction if
                              x.get("operationAmount", {}).get("currency", {}).get("code") == "RUB" or x.get(
                                  "currency_code") == "RUB"]
        transaction = sort_by_ruble_list

    description_answer = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ")
    if description_answer.lower() == "да":
        string_for_search = input("\nВведите слово для поиска в описании операции: ")
        sort_by_string_description = find_str_description(transaction, string_for_search)
        transaction = sort_by_string_description

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(transaction)}\n")

    for item in transaction:
        if item.get("operationAmount", {}).get("currency", {}).get("code") != None:
            currency = item.get("operationAmount", {}).get("currency", {}).get("code")
        else:
            currency = item.get("currency_code")
        print(f"{get_data(item.get("date"))} {item.get("description")}\n\
{mask_account_card(item.get("from"))} -> {mask_account_card(item.get("to"))}\n\
Сумма: {item.get("operationAmount", {}).get("amount")} {currency}\n")


if __name__ == "__main__":
    main()
