import random

def input_numbers():
    return input("Сергей:\nНужное число есть среди вот этих чисел: ")

n = input("Максимальное число n = ")
secret_num = str(random.randint(1, int(n)))
possible_nums = {str(i) for i in range(1,int(n)+1)}

serg = input_numbers()
while serg != "Помогите!" and serg != secret_num:
    numbers = serg.split(' ')
    print("Ответ Ивана:", end=' ')
    if secret_num in numbers:
        print("Да")
        if len(numbers) == 1: break
        for num in list(possible_nums):
            if not num in numbers:
                possible_nums.remove(num)
    else:
        print("Нет")
        for num in numbers:
            if num in possible_nums:
                possible_nums.remove(num)
    serg = input_numbers()

if serg == "Помогите!":
    print("Иван мог загадать следующие числа: ", *possible_nums)
else:
    print("Сергей отгадал число!")