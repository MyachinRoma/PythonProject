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

from src.masks import get_mask_account , get_mask_card_number​​  

# Пример использования get_mask_account 
transactions_account  = ( "78236498532679584236" )

# Пример использования get_mask_card_number 
transactions_card_number  =  "Visa Platinum ['7000792289606361']" 
transactions_card_number  =  "Счет ['73654108430135874305']"

from src.widget import get_data

# Пример использования get_data 
print ( get_data ( "2024-03-11T02:26:18.671407" ))

from src.processing import filter_by_state, sort_by_date

# Пример использования 
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]

# Пример использования sort_by_date 
sorted_transactions  =  sort_by_date ( транзакции )
## Вклад
Если вы хотите внести свой вклад, создайте вилку репозитория и отправьте пул-реквест.
