import os

base_path = "C:\\Users\\Acer\\PycharmProjects\\PythonProject"

full_path = os.path.join(base_path, "src", "processing.py")

with open(full_path, "r") as file:
    print(file.read())


def filter_by_state(dictionary: list) -> list:
    """Выход функции со статусом по умолчанию 'EXECUTED'"""
    new_dictionary = []
    for i in dictionary:
        if i["state"] == "EXECUTED":
            new_dictionary.append(i)
    return new_dictionary


def sort_by_date(base_idtime: list, reverse: bool = True) -> list:
    """Функция сортирует список по дате на убывание"""
    sort_list = sorted(base_idtime, key=lambda x: x["date"], reverse=reverse)
    return sort_list
