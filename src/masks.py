import os
from typing import Union

base_path = os.path.abspath(os.path.dirname(__file__))
full_path = os.path.join(base_path, "masks.py")

with open(full_path, "r") as file:
    print(file.read())


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер карты"""
    if len(card_num) == 16:
        return f"{card_num[:4]}" " " f"{card_num[4:6]}** ****" " " f"{card_num[-4:]}"
    else:
        return "Данные не верны"


def get_mask_account(accounts_num: Union[str]) -> Union[str]:
    """Функуия возвращает замаскированные номера счета"""
    if len(accounts_num) == 20:
        return f"**{accounts_num[-4:]}"
    else:
        return "Данные не верны"
