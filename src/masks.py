import logging
import os
from typing import Union

base_path = os.path.abspath(os.path.dirname(__file__))
full_path = os.path.join(base_path, "masks.py")
logs_path = os.path.join(base_path, "..", "logs", "masks.log")
if not os.path.exists(os.path.dirname(logs_path)):
    os.makedirs(os.path.dirname(logs_path))

# with open(full_path, "r") as file:
# print(file.read())


app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(logs_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(levelname)s: %(name)s:Request time: %(asctime)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)
app_logger.propagate = False


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер карты"""
    app_logger.info("Идет проверка количества заданных символов")
    if len(card_num) == 16:
        app_logger.info("Выполняется маскировка номера карты")
        return f"{card_num[:4]}" " " f"{card_num[4:6]}** ****" " " f"{card_num[-4:]}"
    else:
        app_logger.error("Данные не верны")
        return "Данные не верны"


def get_mask_account(accounts_num: Union[str]) -> Union[str]:
    """Функуия возвращает замаскированные номера счета"""
    app_logger.info("Идет проверка количества заданных символов")
    if len(accounts_num) == 20:
        app_logger.info("Выполняется маскировка номера счета")
        return f"**{accounts_num[-4:]}"
    else:
        app_logger.error("Данные не верны")
        return "Данные не верны"
