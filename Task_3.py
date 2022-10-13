## Task 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

numbers = input("Input a list of numbers separated by a space: ").split()
temp = [] 
for x in numbers: 
    if x not in temp: 
        temp.append(x) 
numbers = temp 
print(f'Updated List after removing duplicates = {temp}')


#### Через функцию set

# numbers = input("Input a list of numbers separated by a space: ").split()

# numbers_1 = list(set(numbers)) 
# print(numbers_1) 


#### Как ключи словаря

# numbers = input("Input a list of numbers separated by a space: ").split()

# numbers_1 = list(dict.fromkeys(numbers)) 
# print(numbers_1) 


##### Через count

# numbers = input("Input a list of numbers separated by a space: ").split()
# for x in numbers: 
#     if numbers.count(x) > 1: 
#         numbers.remove(x) 
# print(numbers)

################### С семинара
### используем словарь

# import numpy 

# dict_new = {} # создали пустой словарь

# items = numpy.random.randint(10, size = 10)
# items_set = list(items[:10])
# print(*items_set) # со * печатает без скобок и запятых

# for i in items_set:
#     if not i in dict_new:
#         dict_new[i] = 0 # создали новый ключ - dict_new[i] - и начали отсчет с нуля, поэтому присвоили 0 
#     dict_new[i] += 1 # посчитаем, сколько раз встретиться элемент с таким ключом

# res_list = []
# for i in dict_new:
#     if dict_new[i] == 1:
#         res_list.append(i)

# print(*res_list)

######## с семинара еще один вариант. с помощью функци Counter

# from collections import Counter
# import numpy 

# items = numpy.random.randint(10, size = 10)
# items_set = list(items[:10])
# print(*items_set) # со * печатает без скобок и запятых

# dict_new = Counter(items_set)
# res_list = [i for i in dict_new if dict_new[i] ==1]

# print(*res_list)

#### еще один вариант решения 

# from collections import Counter
# from random import randint

# def create_list(k, m, n): # создание списка случайных чисел указанного диапазона в соответствии с указанным количеством элементов
#     return [randint(m, n) for i in range(k)]

# k = int(input("Введите количество чисел в списке: "))
# m = int(input("Введите нижнюю границу чисел: "))
# n = int(input("Введите верхнюю границу чисел: "))
# input_list = create_list(k, m, n)
# output_list = [k for k, v in Counter(input_list).items() if v == 1]
# print("Исходная последовательность чисел: ", input_list)
# print("Неповторяющиеся числа: ", output_list)


