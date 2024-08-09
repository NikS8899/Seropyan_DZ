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
            continue

    while True:
        sort_answer = input("\n������������� �������� �� ����? ��/���: ")
        if sort_answer.lower() == "��":
            print("\n������������� �� �����������(1) ��� �� ��������(2)?")
            while True:
                sequence_answer = input("������� 1 / 2: ")
                if sequence_answer == "1":
                    transaction = sort_by_date(transaction, False)
                    break
                elif sequence_answer == "2":
                    transaction = sort_by_date(transaction)
                    break
                else:
                    print(
                        f"������ �������� ������ '{sequence_answer}'!\n��� ���������� �� ����������� ������� ����� '1' "
                        "��� ���������� �� �������� ������� ����� '2'\n")
                    continue
            break
        elif sort_answer.lower() == "���":
            break
        else:
            print(f"����� '{sort_answer}' �� ���������, ������� �� ��� ���")
            continue

    while True:
        sort_by_ruble_answer = input("\n�������� ������ �������� ����������? ��/���: ")
        if sort_by_ruble_answer.lower() == "��":
            sort_by_ruble_list = [x for x in transaction if
                                  x.get("operationAmount", {}).get("currency", {}).get("code") == "RUB" or x.get(
                                      "currency_code") == "RUB"]
            transaction = sort_by_ruble_list
            break
        elif sort_by_ruble_answer.lower() == "���":
            break
        else:
            print(f"����� '{sort_by_ruble_answer}' �� ���������, ������� �� ��� ���")
            continue

    while True:
        description_answer = input("\n������������� ������ ���������� �� ������������� ����� � ��������? ��/���: ")
        if description_answer.lower() == "��":
            string_for_search = input("\n������� ����� ��� ������ � �������� ��������: ")
            sort_by_string_description = find_str_description(transaction, string_for_search)
            transaction = sort_by_string_description
            break
        elif description_answer.lower() == "���":
            break
        else:
            print(f"����� '{description_answer}' �� ���������, ������� �� ��� ���")
            continue

    print("������������ �������� ������ ����������...\n")
    print(f"����� ���������� �������� � �������: {len(transaction)}\n")

    for item in transaction:
        if choice_format_file == "1":
            currency = item.get("operationAmount", {}).get("currency", {}).get("code")
            amount = item.get("operationAmount", {}).get("amount")
        else:
            currency = item.get("currency_code")
            amount = item.get("amount")
        print(f"{get_data(item.get("date"))} {item.get("description")}\n\
{mask_account_card(item.get("from"))} -> {mask_account_card(item.get("to"))}\n\
�����: {amount} {currency}\n")


if __name__ == "__main__":
    main()
