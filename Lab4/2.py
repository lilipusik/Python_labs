import numpy as np

names = np.array(['Вася','Коля','Петя','Вася','Коля'])
marks = np.array([[4,5,4,3,4,5],[2,3,4,3,2,3],[4,4,3,3,2,3],[5,5,5,5,4,5],[3,3,4,3,4,5]])

while (True):
    name = input("Введите имя:")
    if name == "": break
    print("Оценки:\n", marks[np.where(names == name)])
