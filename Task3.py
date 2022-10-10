# Найти расстояние между двумя точками пространства(числа вводятся через пробел)
import math

list_dots = list(map(lambda x: float(x), input("Введите точки через пробел:\n").split(' ')))

def sq(x2, x1): return (x2-x1)**2

print(round(math.sqrt((sq(list_dots[3], list_dots[0]) + sq(list_dots[4], list_dots[1]) + sq(list_dots[5], list_dots[2]))), 2))