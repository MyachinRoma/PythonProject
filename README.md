# Виджет банковских операций клиента
Краткое описание проекта, его цели и задачи.

## Установка
# Клонируйте репозитории:
git clone https://github.com/MyachinRoma/Homework10.1.git
# Перейдите в каталог проекта:
cd PythonProject
# Установить необходимое в зависимости:
pip install -r requirements.txt

## Использование
# Примеры использования функций:

# Пример использования get_mask_account 
print(get_mask_account("78236498532679584236"))

# Пример использования get_mask_card_number 
print(get_mask_account_card("Счет 12345678901234567890"))
print(get_mask_account_card("Visa 1234567890123456"))

# Пример использования get_data 
print(get_data("2024-03-11T02:26:18.671407"))

# Пример использования filter_by_state
filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

# Пример использования sort_by_date 
print(sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},]))

# Примеры тестирования функций, производится в соответствующих модулях по названиям этих модулей:
# Соответственно get_mask_account и get_mask_card_number из модуля masks.py,
# тестируется в модуле tests_masks.
def test_get_mask_card_number(number, new_string):
    assert get_mask_card_number(number) == new_string
def test_get_mask_account(numbers, new_strings):
    assert get_mask_account(numbers) == new_strings
# get_mask_account_card и get_data из модуля widget.py,
# тестируется в модуле tests_widget.
def test_get_mask_account_card(number, new_string):
    assert get_mask_account_card(number) == new_string
def test_get_data(data, new_data):
    assert get_data(data) == new_data
# filter_by_state и sort_by_date из модуля processing.py,
# тестируется в модуле tests_processing.



## Вклад
Если вы хотите внести свой вклад, создайте вилку репозитория и отправьте пул-реквест.
