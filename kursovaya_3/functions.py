import json
from datetime import datetime

def get_file_data(file_name):
    """
    Эта функция принимает файл и извлекает данные в удобном формате
    :param file_name: файл
    :return: список
    """
    with open(file_name, "rt") as file:
        data = file.read()
    data = json.loads(data)
    return data


def do_sort_by_approv(data):
    """
    Эта функция принимает информацию об операциях и сортирует её по
    исполнено - остальное
    :param data: информ. о операциях
    :return: список
    """

    list = []

    for i in data:
        item = i.get('state', 'no info')

        if item == 'EXECUTED':
            list.append(i)
    return list


def buble_sort(data_list):
    """
    Эта функция на основе пузырьковой сортировки сортирует операции по дате
    :param data_list: список операций
    :return: список
    """

    lenght = len(data_list)

    for i in range(lenght - 1):
        for j in range(lenght - i - 1):
            if datetime.fromisoformat(data_list[j]['date']) > datetime.fromisoformat(data_list[j + 1]['date']):
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    return data_list











