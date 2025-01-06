import os

base_path = "C:\\Users\\Acer\\PycharmProjects\\PythonProject"

full_path = os.path.join(base_path, "tests", "main.py")

with open(full_path, "r") as file:
    print(file.read())

from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import get_mask_account_card
from src.widget import get_data


print(get_mask_card_number("1259786432589632"))
print(get_mask_account("78236498532679584236"))
print(get_mask_account_card(f"Visa Platinum ['7000792289606361']"))
print(get_mask_account_card(f"Счет ['73654108430135874305']"))
print(get_data("2024-03-11T02:26:18.671407"))
#print(get_mask_account_card('Счет 12345678901234567890'))
#print(get_mask_account_card("Visa 1234567890123456"))
#print(get_mask_account_card("Visa Super 1234567890123456"))
#print(get_mask_account_card("Visa Super Puper 1234567890123456"))
