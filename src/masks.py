def get_mask_card_number(number: int | str) -> str:
    """Функция возвращающая маску номера карты"""
    list_card_number = list(str(number))
    for digit in range(6, 12):
        list_card_number[digit] = "*"
    mask = "".join(list_card_number)
    return " ".join(mask[i: i + 4] for i in range(0, len(mask), 4))


def get_mask_account(account: int | str) -> str:
    """Функция возвращающая маску номера счета"""
    return "**" + str(account)[-4:]
