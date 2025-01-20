import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    ("number", "new_string"),
    [
        ("7823649853264236", "7823 64** **** 4236"),
        ("6518416514674498", "6518 41** **** 4498"),
        ("6546516111675164", "6546 51** **** 5164"),
        ("2525845825258525", "2525 84** **** 8525"),
    ],
)
def test_get_mask_card_number(number, new_string):
    assert get_mask_card_number(number) == new_string


@pytest.mark.parametrize(
    ("numbers", "new_strings"),
    [
        ("78236498532646378236", "**8236"),
        ("65184165146725494498", "**4498"),
        ("65465161116713485164", "**5164"),
        ("25258458252512468525", "**8525"),
    ],
)
def test_get_mask_account(numbers, new_strings):
    assert get_mask_account(numbers) == new_strings


def test_get_mask_card_number_wrong():
    assert get_mask_card_number("Привет") == "Данные не верны"

def test_get_mask_account_wrong():
    assert get_mask_account("Привет") == "Данные не верны"