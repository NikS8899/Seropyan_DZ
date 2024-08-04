import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=r'C:\My_study\Seropyan_DZ\logs\masks.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске
logger = logging.getLogger("masks")


def get_mask_card_number(number: int | str) -> str:
    """Функция возвращающая маску номера карты"""
    logger.info("Запуск функции маскировки карты")
    if len(str(number)) == 16:
        list_card_number = list(str(number))
        for digit in range(6, 12):
            list_card_number[digit] = "*"
        mask = "".join(list_card_number)
        return str(" ".join(mask[i: i + 4] for i in range(0, len(mask), 4)))
    logger.error(f"Ошибка ввода! Введено: {number}")
    raise ValueError("Введены неверные данные!")


def get_mask_account(account: int | str) -> str:
    """Функция возвращающая маску номера счета"""
    logger.info("Запуск функции маскировки счета")
    if len(str(account)) == 20:
        return "**" + str(account)[-4:]
    logger.error(f"Ошибка ввода! Введено: {account}")
    raise ValueError("Введены неверные данные!")
