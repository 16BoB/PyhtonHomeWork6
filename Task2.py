# Найти сумму чисел списка стоящих на нечетной позиции
from functools import reduce

list_num = [1, 3, 4, 5]

print(reduce(lambda x, i: x+list_num[i] if i % 2 else x, range(len(list_num)), 0))
