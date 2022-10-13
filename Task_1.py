## Task 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#Импорт модуля math  

# x = float(input('Input a broken number: '))
# s = str(x)
# d = abs(s.find('.') - len(s)) - 1
# print('$d = ', 10 ** (-d))

# import math  

# # вывод значения PI

# print(f'π = {round(math.pi, d)}.$')

###### Решение коллег с семинара: 
# def num_precise(n_um, d_c):
#     n_um = Decimal(n_um)
#     n_um = n_um.quantize(Decimal(d_c))

#     return n_um


# num = input('Input the number: ')
# d = input('Input the necessary precision number d: ')
# print(num_precise(num, d))


