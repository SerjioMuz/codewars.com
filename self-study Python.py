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


"""class User:
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
        object.__setattr__(self, attr, value)"""



"""def tracer(func):
    def wrapper(*args, **kwargs):
        print('Вызов %s с аргументами %s' % (func.__name__, args))
        return func(*args, **kwargs)
    return wrapper


from functools import wraps

def tracer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Вызов {func.__name__} с аргументами {args}')
        return func(*args, **kwargs)
    return wrapper

@tracer
def add(a, b) :
    return (a + b)

result=add(2,3)
print(result)
print(add.__name__)"""



class RequireID(type):
    def __new__(cls, name, bases, attrs):
        if 'id' not in attrs:
            raise TypeError(f'Класс {name} должен содержать атрибут id')
        return type.__new__(cls, name, bases, attrs)

class User(metaclass=RequireID):
    id =1


