# Обзор сторонних библиотек Python

import numpy as np
import pandas as pd
from PIL import Image
import pprint

print('Использование библиотеки numpy:')
a1 = np.array([99, 101, 103])
a2 = np.array([110, 108, 105])
a3 = np.array([90, 88, 85])
a4 = np.vstack((a1, a2, a3))        # объединение массивов
pprint.pprint(a1)
pprint.pprint(a2)
pprint.pprint(a3)
pprint.pprint(a4)
print(a1.sum())             # сумма
print(a2.min())             # минимум
print(a3.max())             # максимум
print(a1 + a2)              # сложение
print((a2 * a3))            # умножение
prod4 = a4.prod(axis=0)     # произведение по оси х
pprint.pprint(prod4)

print(f'\nИспользование библиотеки pandas:')
pd1 = pd.read_csv('nvidia.csv')
# print(pd1)
print(pd1.head(15))              # первые 15 строк
print(pd1.sort_values('Date'))   # сортировка по дате
pd1.drop('Open', axis=1, inplace=True)  # удаление столб
print(pd1.head(15))
pd_new = pd.read_csv('nvidia.csv')      # новый датафрейм
print(f' \nНовый список с датой позднее 27-02-2023:')
print(pd_new[pd_new['Date'] > '2023-02-27'])

print(f'\nИспользование библиотеки pillow:')
img = Image.open('Сияние.jpg')
img_new = img.crop((100, 100, 600, 400))   # обрезка изображения
img_new = img_new.rotate(180)              # поворот изображения
img_new = img_new.convert('L')             # преобразование изображения в черно-белое
img_new.show()                             # отображение изображения
img_new.save('Сияни_New.jpg')              # сохранение изображения
