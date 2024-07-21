def get_mask_card_number(number: int | str) -> str:
    """Функция возвращающая маску номера карты"""
    if len(str(number)) == 16:
        list_card_number = list(str(number))
        for digit in range(6, 12):
            list_card_number[digit] = "*"
        mask = "".join(list_card_number)
        return str(" ".join(mask[i: i + 4] for i in range(0, len(mask), 4)))
    raise ValueError("Введены неверные данные!")


def get_mask_account(account: int | str) -> str:
    """Функция возвращающая маску номера счета"""
    if len(str(account)) == 20:
        return "**" + str(account)[-4:]
    raise ValueError("Введены неверные данные!")
