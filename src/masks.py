import os
import logging
from typing import Union

base_path = os.path.abspath(os.path.dirname(__file__))
full_path = os.path.join(base_path, "masks.py")
logs_path = os.path.join(base_path, "logs/masks.log")

with open(full_path, "r") as file:
    print(file.read())


app_logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode='w')
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


app_logger.debug('Debug message')
app_logger.info('Info message')
app_logger.warning('Warning message')
app_logger.error('Error message')
app_logger.critical('Critical message')


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер карты"""
    app_logger.info("Initialization")
    if len(card_num) == 16:
        app_logger.info("Finish")
        return f"{card_num[:4]}" " " f"{card_num[4:6]}** ****" " " f"{card_num[-4:]}"
    else:
        app_logger.critical("Данные не верны")
        return "Данные не верны"


def get_mask_account(accounts_num: Union[str]) -> Union[str]:
    """Функуия возвращает замаскированные номера счета"""
    app_logger.info("Initialization")
    if len(accounts_num) == 20:
        app_logger.info("Finish")
        return f"**{accounts_num[-4:]}"
    else:
        app_logger.critical("Данные не верны")
        return "Данные не верны"

if __name__ == "__main__":
    print(get_mask_card_number("7000561278963206"))
    print(get_mask_account("15369785463259863240"))
