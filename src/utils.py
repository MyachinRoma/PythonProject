import json
import logging
import os
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion

base_path = os.path.abspath(os.path.dirname(__file__))
full_path = os.path.join(base_path, "utils.py")
logs_path = os.path.join(base_path, "..", "logs", "utils.log")
if not os.path.exists(os.path.dirname(logs_path)):
    os.makedirs(os.path.dirname(logs_path))

with open(full_path, "r") as file:
    print(file.read())


app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(logs_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(levelname)s: %(name)s:Request time: %(asctime)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)
app_logger.propagate = False


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding="utf-8") as financial_file:
            app_logger.info("Файл успешно открыт")
            try:
                transactions = json.load(financial_file)
                app_logger.info("Содержимое файла преобразовано в объект")
            except JSONDecodeError:
                app_logger.error("Ошибка декодирования файла")
                return []
        if not isinstance(transactions, list):
            return []
        return transactions
    except FileNotFoundError:
        app_logger.error("Ошибка декодирования файла")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = currency_conversion(trans)
    return amount
