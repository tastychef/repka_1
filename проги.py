#ГЕНЕРАТОР СЛУЧАЙНЫХ ЧИСЕЛ
from random import randint
num = 10
array = list()
for i in range(num):
    array.append(randint(0, 100))
print(array)

