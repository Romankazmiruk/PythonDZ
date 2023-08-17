# n = 385916 

# n1 = n//100000
# n2 = n//10000 % 10
# n3 = n//1000 % 10
# n4 = n//100 % 10
# n5 = n//10 % 10
# n6 = n % 10

# if n1 + n2 + n3 == n4 + n5 + n6:
#     print('билет счастливый')
# else:
#     print('билет обычный')


# n=3
# m=3
# c=9
# if m * n > c and c % 2 == 0:
#     print('yes')
# elif m * n == c:
#     print ('yes')
# else:
#     print('no')



# ____________________________________________

# a = {1, 1, 2, 0, -1, 3, 4, 4}
# print(len(a))

# sp = []
# sp.append (5)
# sp.extend([7,8,True])
# sp.insert(0,5.7)
# print (sp)

# for i,k enumerate(sp)

# t=(4,5,6)

# print(t[0])

# словарь

# d={}
# d["дядя ваня"] = "545643"
# d["дядя вaя"] = "5456asd43"
# print(d)

# множества

# s=set()
# s.add(5)
# s.add(6)
# print(s)

# sp = []
# sp.append(5)
# sp.extend([7,8,True])
# sp.insert(0,5.7)
# sp = sp + [1,2,True,44]
# print(sp)
# # print(sp[3::])
# # print(sp[2:5])
# # print(sp[-5])
# a = sp.pop()
# print(a)
# sp.remove(True)
# del sp[0]

# for i,k in enumerate(sp):
#     print(i,k)
# print(sp)
# t = (4,8,9)
# print(t[0])

# d = {}
# d["дядя Ваня"] = "+78465564"
# d["дядя Вова"] = "12312131"
# del d["дядя Вова"]
# print(d)
# for key, value in d.items():
#     print(key, value)

# print(d.keys())
# print(d.values())

# s = set()
# s.add(5)
# s.add(7)
# print(s)
# print(6 in s)

# list tuple dict set



# Задача №17. Общее обсуждение
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# sp = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(sp)))

# data = [1, 1, 2, 0, -1, 3, 4, 4]
# print(data)
# different_numbers = []
# for number in data:
#     if number not in different_numbers:
#         different_numbers.append(number)
# print(f"Различных чисел: {len(different_numbers)}")

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить з

# sp = [1, 2, 3, 4, 5,5]
# k=3
                  # print(sp[3:]) 
                  # sp1 = sp[k:] + sp[:k]
                  # print(sp1)


# for _ in range(k):
#     sp.insert(0, sp.pop())

# Задача №21. Общее обсуждение
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# sp = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# sp1 = []

# for i in sp:
#     for k, v in i.items():
#         # print(v.strip())
#         if v.strip() not in sp1:
#             sp1.append(v.strip())
# print(sp1)



# print("Original List: ",dictcionary)
# u_value = set( val for dic in dictcionary for val in dic.values())
# print("Unique Values: ",u_value)


# v = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]

# v2 = []
# for i in v:
#     for k,v in i.items():
#         if v.strip() not in v2:
#             v2.append(v.strip())
#             print(k.strip(), v.strip()) 

# print(v2)


# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.



# v = [0, -1, 5, 2, 3]
# i = 1
# j = 0
# while i < len(v):
#     if v[i] > v[i-1]:

#         j+=1
#     i+=1
# print(j)