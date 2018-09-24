class Person:
    def __init__(self, string):
        self._full_name = {
            'name': string.split()[0],
            'last_name': string.split()[1]
        }

    @property
    def get_full_name(self):
        return self._full_name['name'] + ' ' + self._full_name['last_name']


class Person_Card(Person):
    def __init__(self, string):
        Person.__init__(self, string)
        self._data = {
            'cash': string.split()[2],
            'job': string.split()[3],
            'norm': string.split()[4],
            'real_cash': None
        }

    @property
    def get_card(self):
        return self._data

    def get_real_cash(self):
        return self._data['real_cash']


class Person_Work(Person):
    def __init__(self, string):
        Person.__init__(self, string)
        self._fact_work = {
            'worked': string.split()[2]
            }

    @property
    def get_fact_work(self):
        return self._fact_work


def parse_file(file, obj):
    '''
    Возвращает список из объектов,
    из каждой строки файла
    '''
    with open(file, encoding='UTF-8') as lister:
        elems = [obj(elem) for elem in lister][1:]
        return elems


def join_tab(elems1, elems2):
    '''
    Возвращает общий объект из соответсвующих
    друг другу объектов из двух списков
    '''
    join_obj = [elems for elems in elems1]
    for elem in join_obj:
        for el in elems2:
            if elem.get_full_name == el.get_full_name:
                elem.get_card.update(el.get_fact_work)
    return join_obj
