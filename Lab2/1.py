import random

list1 = [random.randint(-20,20) for _ in range(20)]
print("list1 = ", *list1, "\n")

list2 = [i*2 if i < 0 else i**0.5 for i in list1]
print("list2 = ", *list2, "\n")

index = [i for i in range(len(list2)) if list2[i] < 0]
index = [index[i] + i for i in range(len(index))]
list3 = list2
for i in index:
    list3.insert(i,0)
print("list3 = ", *list3, "\n") 

k = int(input("Введите число k = "))
while k in list3:
    list3.remove(k)
print("list4 = ", *list3, "\n") 

list3.reverse()
list3.extend([0]*3)
list3.reverse()
z = int(input("Введите число z = "))
list3.extend([z]*3)
print("list5 = ", *list3, "\n")

list3.sort()
print("list6 = ", *list3, "\n")