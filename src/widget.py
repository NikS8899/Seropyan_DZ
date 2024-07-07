from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(my_string: str) -> str:
    """Функция скрывающая номер карты или счета"""
    product_name = [i for i in my_string.split() if i.isalpha()]
    product_number = [i for i in my_string.split() if i.isdigit()]
    mask = None
    if len(product_number) > 0:
        if len(product_number[0]) > 16:
            mask = get_mask_account(product_number[0])
        else:
            mask = get_mask_card_number(product_number[0])
        return " ".join(product_name) + " " + mask
    raise ValueError("Номер отсутствует!")


def get_data(date_string: str) -> str:
    """Функция возвращающая дату в корректном формате"""
    if len(date_string) >= 26 and "-" in date_string:
        get_date = date_string[:10].split("-")
        flag = True
        for digit in get_date:
            for char in digit:
                if char.isalpha():
                    flag = False
        if flag:
            return ".".join(get_date[::-1])
    raise ValueError("Неверный формат даты!")
