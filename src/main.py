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
    print("\n������! ����� ���������� � ��������� ������ � ����������� ������������.\n\
    �������� ����������� ����� ����:\n\
    1. �������� ���������� � ����������� �� JSON-�����\n\
    2. �������� ���������� � ����������� �� CSV-�����\n\
    3. �������� ���������� � ����������� �� XLSX-�����\n")

    while True:
        choice_format_file = input("������� ����� ����: ")
        if choice_format_file == "1":
            transaction = get_transactions()

            print("��� ��������� ������ JSON-����.\n")
            break
        elif choice_format_file == "2":
            transaction = get_transactions(CSV_PATH_TO_FILE)
            print("��� ��������� ������ CSV-����.\n")
            break
        elif choice_format_file == "3":
            transaction = get_transactions(EXCEL_PATH_TO_FILE)
            print("��� ��������� ������ EXCEL-����.\n")
            break

        else:
            print("����� �����������, ��������� ����.\n")
    while True:
        print("������� ������, �� �������� ���������� ��������� ����������.\n��������� ��� ���������� "
              "�������: EXECUTED, CANCELED, PENDING\n")
        state = input("������� ������: ")

        states_list = ["EXECUTED", "CANCELED", "PENDING"]

        if state.upper() in states_list:
            transaction = filter_by_state(transaction, state.upper())
            if transaction == []:
                print(f"�� ������� '{state.upper()}' �������� �����������, �������� ������ ������.")
                continue
            break
        else:
            print(f"������ �������� '{state}' ����������.\n")

    print("\n������������� �������� �� ����?\n")
    sort_answer = input("��/���: ")
    if sort_answer.lower() == "��":
        print("������������� �� �����������(1) ��� �� ��������(2)?")
        while True:
            sequence_answer = input("\n������� ����� 1 / 2: ")
            if sequence_answer.lower() == "1":
                transaction = sort_by_date(transaction, False)
                break
            elif sequence_answer.lower() == "2":
                transaction = sort_by_date(transaction)
                break
            else:
                print("������ �������� ������!\n��� ���������� �� ����������� ������� ����� '1' "
                      "��� ���������� �� �������� ������� ����� '2'\n")

    sort_by_ruble_answer = input("\n�������� ������ �������� ����������? ��/���: ")
    if sort_by_ruble_answer.lower() == "��":
        sort_by_ruble_list = [x for x in transaction if
                              x.get("operationAmount", {}).get("currency", {}).get("code") == "RUB" or x.get(
                                  "currency_code") == "RUB"]
        transaction = sort_by_ruble_list

    description_answer = input("\n������������� ������ ���������� �� ������������� ����� � ��������? ��/���: ")
    if description_answer.lower() == "��":
        string_for_search = input("\n������� ����� ��� ������ � �������� ��������: ")
        sort_by_string_description = find_str_description(transaction, string_for_search)
        transaction = sort_by_string_description

    print("������������ �������� ������ ����������...\n")
    print(f"����� ���������� �������� � �������: {len(transaction)}\n")

    for item in transaction:
        if item.get("operationAmount", {}).get("currency", {}).get("code") != None:
            currency = item.get("operationAmount", {}).get("currency", {}).get("code")
        else:
            currency = item.get("currency_code")
        print(f"{get_data(item.get("date"))} {item.get("description")}\n\
{mask_account_card(item.get("from"))} -> {mask_account_card(item.get("to"))}\n\
�����: {item.get("operationAmount", {}).get("amount")} {currency}\n")


if __name__ == "__main__":
    main()
