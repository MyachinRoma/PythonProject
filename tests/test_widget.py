import pytest

from src.widget import get_data, get_mask_account_card


@pytest.mark.parametrize(
    ("number", "new_string"),
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ],
)
def test_get_mask_account_card(number, new_string):
    assert get_mask_account_card(number) == new_string


@pytest.mark.parametrize(("data", "new_data"), [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_data(data, new_data):
    assert get_data(data) == new_data
