import numpy as np

# 1 создание двумерного массива 8х8 с рандомными числами
matrix = np.random.randint(-10, 10, (8,8))
print("\tMatrix\n", matrix)

# 2 вырез центральной матрицы 4х4
centre_matrix = matrix[2:6, 2:6]
print("\n\tCentre_Matrix\n", centre_matrix)

# 3 удаление строк, в которых присутсвует минимальный элемент
index = np.where(matrix[:,:] == np.min(matrix))[0] # получаем индексы строк, в которых находится минимальный элемент
matrix2 = np.delete(matrix, index, axis=0)
print("\n\tMatrix_2\n", matrix2)

# 4 вставка строки под индексом 0, состояющую из минимального элемннта матрицы
matrix3 = np.insert(matrix2, 0, np.min(matrix2), axis=0)
print("\n\tMatrix_3\n", matrix3)

# 5 нахождение суммы и среднего значения двумерной матрицы
print("\nsum = ", np.sum(matrix3), "\navg = ", np.average(matrix3))