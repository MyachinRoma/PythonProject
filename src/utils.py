import os
import json
import logging
from json import JSONDecodeError
from typing import Any
from src.external_api import currency_conversion

base_path = os.path.abspath(os.path.dirname(__file__))
full_path = os.path.join(base_path, "utils.py")
logs_path = os.path.join(base_path, "logs/utils.log")

with open(full_path, "r") as file:
    print(file.read())

app_logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8", mode='w')
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


app_logger.debug('Debug message')
app_logger.info('Info message')
app_logger.warning('Warning message')
app_logger.error('Error message')
app_logger.critical('Critical message')


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    app_logger.info("Initialization")
    try:
        app_logger.info("Initialization")
        with open(path, encoding="utf-8") as financial_file:
            app_logger.info("Initialization")
            try:
                transactions = json.load(financial_file)
                app_logger.info("Initialization")
            except JSONDecodeError:
                app_logger.info("Finish")
                return []
        app_logger.info("Initialization")
        if not isinstance(transactions, list):
            app_logger.info("Finish")
            return []
        app_logger.info("Finish")
        return transactions
        app_logger.critical("FileNotFoundError")
    except FileNotFoundError:
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    app_logger.info("Initialization")
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        app_logger.info("Initialization")
    else:
        amount = currency_conversion(trans)
        app_logger.info("Finish")
    return amount
