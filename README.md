# Виджет банковских операций клиента
Краткое описание проекта, его цели и задачи.


## Установка
1. Склонируйте репозиторий на локальную машину:
```
git clone https://github.com/kashin152/myproject.git
s``
2. Установите необходимые зависимости:
```
pip install -r requirements.txt
```

## Модуль processing
Модуль processing содержит функцию, которая возвращает список, содержащий только те словари, где было переданно соответствющее в функцию значение. Также содержит функцию, которая задает
      порядок сортировки (убывание, возрастание).

### Функция filter_by_state
```python
def filter_by_state(dictionary: list, state: str = "EXECUTED") -> list:
    """Выход функции со статусом по умолчанию 'EXECUTED'"""
    new_dictionary = []
    for i in dictionary:
        if i["state"] == state:
            new_dictionary.append(i)
    return new_dictionary
```
### Функция sort_by_date
```python
def sort_by_date(base_idtime: list, reverse: bool = True) -> list:
    """Функция сортирует список по дате на убывание"""
    sort_list = sorted(base_idtime, key=lambda x: x["date"], reverse=reverse)
    return sort_list

```

### Пример использования
```python
data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
```

## Модуль masks
Модуль masks содержит функцию, которая выводит маскированный номер карты.

### Функция mask_card_account_number
```python
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
```

### Пример использования
```python
numder = [
        "1596837868705199",
        "64686473678894779589",
        "7158300734726758",
        "35383033474447895560",
        "6831982476737658",
        "8990922113665229",
        "5999414228426353",
        "73654108430135874305",
    ]
```

## Модуль widget
Модуль widget содержит функцию, которая выводит только номер карты/счета, и функцию, которая которая выводит дату в формает DD.MM.YYYY.

### Функция get_mask_account_card
```python
def get_mask_account_card(string: str) -> str:
    """Функция возвращает маскирующие счета и карты"""

    if "Счет" in string:
        account = string[-20:]
        return string[:-20] + get_mask_account(account)
    else:
        cardnumber = " ".join(string[-16:].split())
        return string[:-16] + get_mask_card_number(cardnumber)
```

### Пример использования
```python
number = [
         "Maestro 1596837868705199",
         "Счет 64686473678894779589",
         "MasterCard 7158300734726758",
         "Счет 35383033474447895560",
         "Visa Classic 6831982476737658",
         "Visa Platinum 8990922113665229",
         "Visa Gold 5999414228426353",
         "Счет 73654108430135874305",
         ]

date = [
        "2018-07-11T02:26:18.671407",
        "2019-07-03T18:35:29.512364",
        "2018-10-14T08:21:33.419441",
       ]
```

## Модуль generators
Модуль generators содержит генераторы для работы с массивами транзакций. Эти генераторы позволяют быстро и удобно находить нужную информацию о транзакциях и проводить анализ данных.

### Функция filter_by_currency
```python
def filter_by_currency(transactions, currency):
    """Функция принимает на вход список со словарем и возвращает id операции"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction
```

### Функция transaction_descriptions
```python
def transaction_descriptions(transactions):
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description")
```

### Функция card_numbers_generator
```python
def card_number_generator(start, stop):
    """Генератор номеров кард в заданном параметре"""
    for number in range(start, stop + 1):
        number_str = f"{number:016}"
        formatted_number = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        yield formatted_number
```
## Модуль decorators
Модуль decorators содержит декоратор, с помощью которого осуществляется логирование вызова функции и ее результата. Данные кешируются в дерикторию logs в файл mylog.txt.
### Пример использования
```python
function ok
function error: division by zero. Inputs: (5, 0), {}
function ok
function error: division by zero. Inputs: (5, 0), {}
```
## Модуль utils
Модуль utils содержит функции, с помощью которых выводится сумма транзакции из полученного JSON-файла.
### Пример использования
```python
[
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]


31957.58
```
## Модуль external_api
Модуль external_api содержит функцию, с помощью которой осуществляется конвертация суммы транзакции через запрос API.
### Пример использования
```python
[
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }
]


731655.89
```

## Модуль new_transactions
Модуль new_transactions содержит функции, с помощью которых осуществляется считывание данных из файлов CSV и XLSX.
### Пример использования
```python
Файл transactions.csv

id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту

Результат 

[
  {
      'id': '650703', 
      'state': 'EXECUTED', 
      'date': '2023-09-05T11:30:32Z', 
      'operationAmount': {
        'amount': '16210', 
        'currency': {
            'name': 'Sol', 
            'code': 'PEN'
        }
      }, 
      'description': 'Перевод организации', 
      'from': 'Счет 58803664561298323391', 
      'to': 'Счет 39745660563456619397'
   }
]

```

## Модуль sort
Модуль sort содержит функции, с помощью которых осуществляется сортировка данных по поисковой строке и по категории операций.
### Пример использования
```python
Функция list_transactions_sort_description

Результат: 
{
 "Перевод организации": 40,
 "Открытие вклада": 10,
 "Перевод со счета на счет": 15,
 "Перевод с карты на карту": 19,
 "Перевод с карты на счет": 16,
 }

Функция list_transactions_sort_search

Результат:
[        
 {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431",
 },
 {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Открытие вклада",
    "to": "Счет 72082042523231456215",
 }
]


# Логирование
В проекте было разработано добавление логов у таких модулей как utils и masks. Логи перезаписываются в папку logs при каждом запуске функций.
### Пример использования
```python
INFO: src.masks:Request time: 2025-02-11 22:30:17,268: Идет проверка количества заданных символов
ERROR: src.masks:Request time: 2025-02-11 22:30:17,268: Данные не верны
INFO: src.masks:Request time: 2025-02-11 22:30:17,269: Идет проверка количества заданных символов
INFO: src.masks:Request time: 2025-02-11 22:30:17,269: Выполняется маскировка номера карты
ERROR: src.utils:Request time: 2025-02-11 22:30:17,269: Ошибка декодирования файла


```




## Автор
Мячин Роман

## Лицензия
Этот проект лицензирован под MIT Лицензией - см. файл LICENSE.txt для дополнительной информации.
