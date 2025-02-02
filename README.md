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

# Пример использования filter_by_currency,
# transaction_descriptions и card_number_generator
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
> 
> descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
> 
> for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005

# Пример использования log
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

# Примеры тестирования функций, производится в соответствующих модулях по названиям этих модулей:
# Соответственно get_mask_account и get_mask_card_number из модуля masks.py,
# тестируется в модуле tests_masks.
def test_get_mask_card_number(number, new_string):
    assert get_mask_card_number(number) == new_string
def test_get_mask_account(numbers, new_strings):
    assert get_mask_account(numbers) == new_strings

# get_mask_account_card и get_data из модуля widget.py,
# тестируется в модуле test_widget.
def test_get_mask_account_card(number, new_string):
    assert get_mask_account_card(number) == new_string
def test_get_data(data, new_data):
    assert get_data(data) == new_data

# filter_by_state и sort_by_date из модуля processing.py,
# тестируется в модуле test_processing.
def test_filter_by_state(data, state, expected):
    assert filter_by_state(data, state) == expected
def test_sort_by_date(data, reverse, expected):
    assert sort_by_date(data, reverse) == expected

# filter_by_currency, transaction_descriptions и card_number_generator
# тестируется в модуле test_generator.
def test_filter_by_currency(transactions, currency):
    filtered_transactions = filter_by_currency(transactions, currency)
    assert next(filtered_transactions)["id"] == 939719570

def test_transaction_descriptions():
    """Тест функции transaction_descriptions"""
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
    ]

    descriptions = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert descriptions == expected


def test_card_number_generator():
    """Тест функции card_number_generator"""
    generator = card_number_generator(1, 7)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
    assert next(generator) == "0000 0000 0000 0006"
    assert next(generator) == "0000 0000 0000 0007"

# log тестируется в модуле test_decorators.
def test_log(capsys):
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    # Проверка корректного выполнения функции
    my_function(1, 2)
    captured = capsys.readouterr()
    assert (
        "my_function called with args: (1, 2), kwargs:{}. Result: 3\n" in captured.out
    )
    # Проверка ошибки
    try:
        my_function(0, 2)
    except TypeError:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out
