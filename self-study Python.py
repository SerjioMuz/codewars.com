"""_str=input("Введите текст")
cod_str=_str.encode("utf-8")
print('Тип объекта %s \nДлинна строки %s \nДлинна байтов %s' % (type(cod_str), len(_str), len(cod_str)))
decod_str=cod_str.decode("utf-8")
print('Проверка равенства строк', _str==decod_str)"""


"""file=open('C:\\PythonProject\\text7.txt', 'r', encoding='utf-8')
text=file.read()
print('Первая строка: %s \nОбщее количество символов %s \nКоличество байтов файла %s' % (text.splitlines()[0], len(text), len(text.encode("utf-8"))))
file.close()"""



"""with open('C:\\PythonProject\\text7.txt', 'r', encoding='ascii') as file:
    try:
        text=file.read()
    except:
        print('Кодировка не соответствует системной')"""



"""def normalize(data):
    if type(data)==str:
        return data
    elif type(data)==bytes:
        return data.decode("utf-8")
    else:
        raise TypeError

print(normalize('привет мир'))
print(normalize(('привет мир').encode()))
print(normalize(123))"""


class User:
    def __init__(self, name):
        object.__setattr__(self, '_name', name)

    def __getattr__(self, attr):
        if attr == 'name':
            return self._name
        print(f'Нет такого атрибута: {attr}')
        raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if attr == 'name':
            raise AttributeError('Атрибут name доступен только для чтения')
        object.__setattr__(self, attr, value)



