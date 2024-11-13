# Интроспекция

from pprint import pprint


# КЛАСС и 2 ФУНКЦИИ созданы для примера
class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        if 0 < self.age < 7:
            return f'{self.name} ребенок'
        elif 7 <= self.age < 18:
            return f'{self.name} учащийся'
        elif 18 <= self.age < 65:
            return f'{self.name} рабочий'
        else:
            return f'{self.name} пенсионер'

def name_string(name='alex'):
    return str(name)

def name_age(age=25):
    return age

input_name = name_string(input('Введите имя: '))
input_age = name_age(input('Введите возраст: '))
human = Human(input_name, input_age)


# ОСНОВНОЕ ЗАДАНИЕ

def introspection_info(object):
    dict_info = {}
    try:
        dict_info['ID'] = id(object)
        dict_info['type'] = type(object)
        dict_info['attributes'] = vars(object)
        dict_info['methods'] = [element for element in dir(object.__getattribute__) if callable(element) == False]
        if hasattr(object, '__module__'):
            dict_info['module'] = object.__module__
    except (TypeError, AttributeError):
        pass
    return dict_info

str_info = introspection_info(input_name)
pprint(str_info)
func_info = introspection_info(name_string)
pprint(func_info)
func_class_info = introspection_info(human.__str__)
pprint(func_class_info)
class_info = introspection_info(human)
pprint(class_info)
