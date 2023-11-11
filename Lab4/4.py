import numpy as np
import scipy as scp

# a = np.round(np.random.rand(3, 3), 2)
a =   np.array([[0.54, 0.25, 0.2 ],
       [0.3 , 0.17, 0.1 ],
       [0.08, 0.06, 0.09]])

print("Матрица А\n", a)

# 1
s = np.sum(a.reshape(3, 3), axis=0)
for i in range(len(s)):
    if s[i] >= 1:
        a[:, i] = 0
print("Матрица А после проверки\n", a)

# 2
det = np.linalg.det(a)
print("Определитель матрицы A: det = ", det)

# 3
#b = np.eye(n) - a
b = np.eye(3) - a
print("Матрица B = E - A\n", b)

# 4
c = np.linalg.inv(b)
print("Обратная матрица B (C = B^(-1))\n", c)

# 5
# y = np.random.randint(1, 100, n)
y = [[30], [17], [10]]
print("Вектор Y = ", y)

# 6
x = np.dot(c, y)
print("Вектор X =\n", x)

# 7
xx = np.dot(a, x) + y
print("Полученный вектор Х =\n", xx)