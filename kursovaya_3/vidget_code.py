
from datetime import datetime
import functions


content = functions.get_file_data("operations.json")

executed_operations_list = functions.do_sort_by_approv(content)
#print(executed_operations_list)
functions.buble_sort(executed_operations_list)

#Код ниже запускает иттерацию по пяти последним операциям

for i in executed_operations_list[:-6:-1]:

    # Эта срочка будет использоваться ниже для вывода даты по порядку
    dates = datetime.fromisoformat(i['date'])

    # Эта часть кода подстраивает номер карты под требования
    card_number = i.get('from', 'no info')
    number = []
    if len(card_number)>7:
        card_number=card_number.split()
        number = [i for i in card_number[-1]]
        for k in [-5,-6,-7,-8,-9,-10]:
            number[k] = "*"
        number.insert(-4, " ")
        number.insert(-9, " ")
        number.insert(-14, " ")
        number.insert(-19, " ")
        number = "".join(number)
        #print(number)
        if len(list(card_number)[-1])>7:
            card_number = list(card_number)
            card_number.pop(-1)
            card_number.append(number)
            card_number = " ".join(card_number)

    #Эта часть кода подстраивает номер СЧЁТА под требования
    account_number = i['to']
    acc_number = ['*','*']
    account_number = [i for i in account_number]
    for z in [-4,-3,-2,-1]:
        acc_number.append(account_number[z])
    acc_number = "".join(acc_number)


    # Здесь вывод всей информации
    print(f"{dates.day}.{dates.month}.{dates.year} {i['description']}")
    print(f"{card_number} -> {acc_number}")
    print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
    print()


























