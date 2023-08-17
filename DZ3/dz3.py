
# list_1 = [1, 2, 4, 5,]
# k = 3

# # Введите ваше решение ниже
# j = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         j += 1
# print(j)


# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:


# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8
# print(list_1)
# list_2 = list()
# for j in range(len(list_1)):
#     list_2.append(list_1[j] - k)
# print(list_2)
# for i in range(len(list_2)):
#     if list_2[i] < 0:
#         list_2[i] = list_2[i] * -1
# print(list_2)
# min = list_2[0]
# # z=0
# for i in range(len(list_2)):
#     if list_2[i] < min:
#         min = list_2[i]
#         z=i
#         print(list_2[i])
# print(list_1[z])




# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.



# dictionary = {'1':'А, В, Е, И, Н, О, Р, С, Т, A, E, I, O, U, L, N, S, T, R','2':'Д, К, Л, М, П, У, D, G', '3':'Б, Г, Ё, Ь, Я, B, C, M, P',
# '4':'Й, Ы, F, H, V, W, Y','5':'K, Ж, З, Х, Ц, Ч','8':'Ш, Э, Ю, J, X','10':'Ф, Щ, Ъ, Q, Z'}
# res = list()
# res_final = 0
# string = input()
# list_1 = list(string)  # s2 = s1.title()
# print(list_1)
# for i in range(len(list_1)):
#     for item in dictionary:
#         if list_1[i] in dictionary[item]:
#             res.append(item)
# print(res)
# for i in range(len(res)):
#     res_final = res_final + int(res[i])
# print(res_final)