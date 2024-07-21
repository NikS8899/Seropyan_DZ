import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("value, result", [("1596837868705199", "1596 83** **** 5199"),
                                           ("7158300734726758", "7158 30** **** 6758"),
                                           ("8990922113665229", "8990 92** **** 5229")])
def test_get_mask_card_number(value, result):
    assert get_mask_card_number(value) == result


@pytest.mark.parametrize("values, result", [("64686473678894779589", "**9589"),
                                            ("35383033474447895560", "**5560"),
                                            ("73654108430135874305", "**4305")])
def test_get_mask_account(values, result):
    assert get_mask_account(values) == result


def test_get_wrong_mask_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(7000792289608)
    assert str(exc_info.value) == "Введены неверные данные!"


def test_get_wrong_mask_account():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(73654108430135)
    assert str(exc_info.value) == "Введены неверные данные!"
