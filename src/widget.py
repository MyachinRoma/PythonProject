import os

from src.masks import get_mask_account, get_mask_card_number

base_path = os.path.abspath(os.path.dirname(__file__))
full_path = os.path.join(base_path, "widget.py")

with open(full_path, "r") as file:
    print(file.read())


def get_mask_account_card(string: str) -> str:
    """Функция возвращает маскирующие счета и карты"""

    if "Счет" in string:
        account = string[-20:]
        return string[:-20] + get_mask_account(account)
    else:
        cardnumber = " ".join(string[-16:].split())
        return string[:-16] + get_mask_card_number(cardnumber)


def get_data(user_date: str) -> str:
    """Функция возвращает преобразованную дату, формат даты"""
    new_date = user_date.split("T")
    date = new_date[0].split("-")
    return f"{date[-1]}.{date[-2]}.{date[-3]}"
