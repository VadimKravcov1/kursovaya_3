from kursovaya_3 import functions

def test_get_file_data():
    assert functions.get_file_data('info_test.json') == [{'hello': 'world'}]


def test_do_sort_by_approv():
    a = [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
          "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}}}]
    assert functions.do_sort_by_approv(a) == []


def test_buble_sort():
    list = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'}]
    assert functions.buble_sort(list)


