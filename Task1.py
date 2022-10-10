# 1- Определить, присутствует ли в заданном списке строк, некоторое число
list_str = ['asdfa', '22', 'ada4']

number = 4

print(any(str(number) in i for i in list_str))