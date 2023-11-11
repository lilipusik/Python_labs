import random
import math

#1
secret = random.randint(1,100)
num = int(input("Введите число: "))
while(num != secret):
    print("Упс, ты не угадал :) Я загадал число, которое ", end = " ")
    if num > secret: print("меньше " + str(num))
    else: print("больше " + str(num))
    num = int(input("Попробуй еще раз: "))
print("Молодец, ты угадал!")

#2
a,b,c = map(float,input("Введите коэффициенты через пробел: ").split(' '))
if (a == 0 or b == 0 or c == 0): print("Нулевых коэффициентов быть не должно")
else:
    d = b**2 - 4*a*c
    if d == 0: print("x = ", -b/(2*a))
    elif d < 0: print("Корней нет")
    else: print("x1 = ", (-b-math.sqrt(d))/(2*a), ", x2 = ", (-b+math.sqrt(d))/(2*a))
    
#3
n, m = map(int,input("Введите n и m через пробел: ").split(' '))
d = 1
while d % n or d % m:
    d += 1
print("d =", d)

#4 
bills = [5000, 1000, 500, 200, 100]
money = int(input("Введите сумму, которую хотите снять: "))
countbills = [0] * len(bills)
summa = 0
for i in range(len(bills)):
    while summa + bills[i] <= money:
        countbills[i] += 1
        summa += bills[i]
    if summa == money or summa > money: break
if summa != money: result = "Данную сумму банкомат выдать не может"
else:
    result = f"{5000:^10}{1000:^10}{500:^10}{200:^10}{100:^10}" + "\n" + "-"*50 + "\n"
    for i in countbills:
        result += f"{i:>10}"
file = open('Lab1/4.txt','w',encoding='utf-8')
file.write(result)
file.close()

#5
a, b = map(int,input("Введите длину и ширину комнаты через пробел: ").split(' '))
if a < 1 or a > 10 or b < 0 or b > 10: print("Размер комнаты указан некорректно")
else:
    x, y = map(int,input("Введите координаты через пробел: ").split(' '))
    if x < 1 or x > 10 or y < 0 or y > 10: print("Робот не может находиться за пределами комнаты")
    else:
        file = open('Lab1/5.txt')
        commands = file.readline().split(' ')
        file.close()
        for i in range(len(commands)):
            cmd = commands[i]
            if cmd == "N" and x + 1 <= 10: x += 1
            elif cmd == "S" and x - 1 > 0: x -= 1
            elif cmd == "W" and y - 1 > 0: y -= 1
            elif cmd == "E" and y + 1 <= 10: y += 1
            elif cmd == "X":
                print("СТОП")
                break
            print("Марсоход находится на позиции", x, y)
    
#6
def path():
    return int(input("Цифра: "))

def room():
    print("Вы в спальне. Куда идем?\n1 - В ванную\n2 - В коридор")
    return path()
    
def bathroom():
    print("Вы в ванной. Куда идем?\n1 - В спальню\n2 - В коридор")
    return path()
    
def hall():
    print("Вы в коридоре. Куда идем?\n1 - В спальню\n2 - В ванную\n3 - На кухню\n4 - В дверь")
    return path()

def kitchen():
    print("Вы на кухне. Куда идем?\n1 - В коридор\n2 - В открытое окно")
    return path()

places = ["room","bathroom","hall","kithen"]
pl = random.choice(places)
places.extend(["door","window"])
while pl != "door" and pl != "window":
    match pl:
        case "hall":
            p = hall()
            if p == 1: pl = "room"
            elif p == 2: pl = "bathroom"
            elif p == 3: pl = "kithen"
            else: pl = "door"
        case "room":
            pl = "bathroom" if room() == 1 else "hall"
        case "bathroom":
            pl = "room" if bathroom() == 1 else "hall"
        case _:
            pl = "hall" if kitchen() == 1 else "window"
if pl == "door": print("Молодец, ты выбрался из квартиры!")
else: print("Ты выпрыгнул из окна и разбился. Игра провалена")

#7
def nok(a,b):
    if a == 0: return b
    return nok(b % a, a)

def reducing(a):
    d = nok(a[0],a[1])
    x = (a[0] // d, a[1] // d)
    return x[0]//x[1] , x[0]%x[1] , x[1]

def sumfrac(x,y):
    x1 = x[0]*y[1]
    y1 = y[0]*x[1]
    return x1+y1 , x[1]*y[1]

k = int(input("Введите количество дробей: "))
fractions = []
summa = [0,0]
for _ in range(k):
    a,b = map(int,input("Введите числитель и знаменатель через пробел: ").split(' '))
    fractions.append((a,b))
for i in range(k):
    if i == 0:
        summa[0],summa[1] = sumfrac(fractions[i],fractions[i+1])
    elif i != 1:
        summa[0],summa[1] = sumfrac(summa,fractions[i])
a,b,c = reducing(summa)
if a == 0 and b == 0: print(0)
elif a == 0: print(f"{b}/{c}")
elif b == 0: print(a)
else: print(f"{a} {b}/{c}")