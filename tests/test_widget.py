import pytest

from src.widget import get_data, mask_account_card


def test_mask_wrong_account_card():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Master Card 73654108430135")
    assert str(exc_info.value) == "Введены неверные данные!"


def test_mask_account_card_without_number():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Счет ")
    assert str(exc_info.value) == "Номер отсутствует!"


@pytest.mark.parametrize("values, result", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                            ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                            ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229")])
def test_mask_account_card_with_card(values, result):
    assert mask_account_card(values) == result


@pytest.mark.parametrize("values, result", [("Счет 64686473678894779589", "Счет **9589"),
                                            ("Счет 35383033474447895560", "Счет **5560"),
                                            ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card_with_account(values, result):
    assert mask_account_card(values) == result


def test_get_data():
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_wrong_data():
    with pytest.raises(ValueError) as exc_info:
        get_data("202403T02:26:18.671407")
    assert str(exc_info.value) == "Неверный формат даты!"


def test_get_wrong_data2():
    with pytest.raises(ValueError) as exc_info:
        get_data("")
    assert str(exc_info.value) == "Неверный формат даты!"
