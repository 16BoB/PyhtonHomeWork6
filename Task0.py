# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;

# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
import re

OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def verification_str (line):
    count = 0
    length_line = len(line)
    for i in line:
        if count == length_line - 1 and i in OPERATORS:
            print('недостаточно числовых данных')
            raise SystemExit 

        count +=1



def parse(line):
    num = ''
    for i in line:
        if i in '1234567890.':
            num += i
        elif num:
            yield float(num)
            num = ''
        if i in OPERATORS or i in '()':
            yield i
    if num:
        yield float(num)
 
def sort(parsed):
    tmp = []
    for i in parsed:
        if i in OPERATORS:
            while tmp and tmp[-1] != '(' and OPERATORS[i][0] <= OPERATORS[tmp[-1]][0]:
                yield tmp.pop()
            tmp.append(i)
        elif i == ')':
            while tmp:
                x = tmp.pop()
                if x == '(':
                    break
                yield x
        elif i == '(':
            tmp.append(i)
        else:
            yield i
    while tmp:
        yield tmp.pop()
 
def calc(sort):
    tmp = []
    for i in sort:
        if i in OPERATORS:
            y = tmp.pop()
            x = tmp.pop()
            tmp.append(OPERATORS[i][1](x, y))
        else:
            tmp.append(i)
    return tmp[0]
 
a = '10 * 5 +'

nums = re.findall(r'\d+', a)

if len(nums) <= 1:
    print('неправильный ввод: нужны числа')
    raise SystemExit 

verification_str(a)

result = calc(sort(parse(a)))

print(result)