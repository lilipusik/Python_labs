stroka = input("Введите строку: ")
result = ""

count = 1
for i in range(len(stroka)):
    if i != len(stroka) - 1 and stroka[i] == stroka[i + 1]:
        count += 1
        continue
    result += stroka[i] + str(count)
    count = 1
print("Закодированная строка: " + result)