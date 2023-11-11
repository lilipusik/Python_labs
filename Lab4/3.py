import numpy as np

m1 = np.random.randint(1, 10, 10)
m2 = np.random.randint(1, 10, 10)
print("m1: ", m1, "\nm2: ", m2)

# 1 симметрическая разность множеств
m3 = np.setxor1d(m1, m2)
print("\nm3: ", m3)

# 2 замена занчений элемнтов по условию
m1[(m1 % 2 == 0) | (m1 % 3 == 0)] = 1
print("\nnew m1: ", m1)

# 3 объединение массивов и преобразование в двумерный
m4 = np.reshape(np.concatenate((m1,m2), axis=0), (4,5), order='C')
print("\nm4: ", m4)

# 4 удаление 1 и 4 столбца
m4 = np.delete(m4, (0,3), 1)
print("\nnew m4: ", m4)

# 5 транспонирование матрицы
m5 = np.transpose(m4)
print("\m5: ", m5)