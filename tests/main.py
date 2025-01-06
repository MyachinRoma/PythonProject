from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import get_mask_account_card
from src.widget import get_data

from src.processing import filter_by_state
from src.processing import sort_by_date

import os

base_path = "C:\\Users\\Acer\\PycharmProjects\\PythonProject"

full_path = os.path.join(base_path, "tests", "main.py")

with open(full_path, "r") as file:
    print(file.read())


print(get_mask_card_number("1259786432589632"))
print(get_mask_account("78236498532679584236"))
print(get_mask_account_card(f"Visa Platinum ['7000792289606361']"))
print(get_mask_account_card(f"Счет ['73654108430135874305']"))
print(get_data("2024-03-11T02:26:18.671407"))
print(get_mask_account_card('Счет 12345678901234567890'))
print(get_mask_account_card("Visa 1234567890123456"))
print(get_mask_account_card("Visa Super 1234567890123456"))
print(get_mask_account_card("Visa Super Puper 1234567890123456"))
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
