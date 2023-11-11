str1 = input("Первая строка: ")
str2 = input("Вторая строка: ")
if (len(str1) != len(str2)): print("Строки должны быть одинаковой длины")
else:
    num = -1
    for i in range(len(str1)):
        str2 = str2[1:] + str2[0]
        if str2 == str1:
            num = i + 1
            break
    if num == -1: print("Первую строку нельзя получить из второй с помощью циклического сдвига")
    else: print(f"Первая строка получается из второй со сдвигом {num}")