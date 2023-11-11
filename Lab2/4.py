N = int(input("Количество друзей N = "))
K = int(input("Количество расписок K = "))

dolgi = [0] * N
for _ in range(K):
    a = int(input("Кому: "))
    b = int(input("От кого: "))
    c = int(input("Сколько: "))
    dolgi[a-1] -= c
    dolgi[b-1] += c

print("\nПодсчитанные долги друзей:")
for num, dolg in enumerate(dolgi, start=1):
    print(num, ":", dolg)
