# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д    
list_nums = [3, 2, 4 , 5]

print(list(map(lambda i: list_nums[i] * list_nums[len(list_nums) - i - 1], range(len(list_nums) // 2 + len(list_nums) % 2))))