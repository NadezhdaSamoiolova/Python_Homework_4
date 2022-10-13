## Task 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# from os import remove


# N = int(input('Input N: '))
# list = []
# a = 2

# if (N % a) == 0:
#     b = N / a
#     while b % a == 0:
#         b = int(b / a)
#     list.append(b)
    
# c = N / b
# if (c % a == 0):
#     c = N / b
#     while c > a:
#         c = int(c / a)
#     list.append(c)
#     list.append(a)
#     print(list)

# while a < N:
#     if N % a == 0:
#         b = int(N / a)
#         list.append(b)
#     a += 1

# list2 = []

# for i in range(len(list)):
#     for j in range(len(list)):
#         if (list[i] != list[j]) and (list[i] % list[j] == 0):
#             list2.append(list[i] / list[j])
        

# print(list)
# print(list2)
# print(22 % 2 != 0)

######## Решение коллег с семинара: 
# import math

# def prime_factors(n):
#     l_ist = []
#     while n % 2 == 0:
#         l_ist.append(2)
#     n = n / 2

# for i in range(3, int(math.sqrt(n)) + 1, 2):
#     while(n % i == 0):
#         l_ist.append(i)
#     n = n / i

# if n > 1:
#     l_ist.append(int(n))
# return l_ist

# num = int(input('Enter the number N for calculation: '))
# print(*prime_factors(num))

