import numpy as np
from pandas import Series as sr

# 1
series = sr(np.random.randint(1, 100, 20))
print("Массив:\n", *series)

# 2
print("\nЭлементы под номерами от 5 до 10:\n", *series[5:11].values)

# 3
print("\nЭлементы от 10 до 50:\n", *series[(series.values >= 10) & (series.values <= 50)].values)

# 4
a, b, c = map(int, input("\na, b, c = ").split())
index = series[series.where((series.values == a) | (series.values == b) | (series.values == c)).notnull()].index
print("Индексы элементов с заданными значениями:\n", *index)

# 5
print("\nЧетные элементы:\n", *series[series.values % 2 == 0].values)

# 6
series[series.values > 70] = 0
print("\nЗамена элементов, больших 70, на 0:\n", *series.values)