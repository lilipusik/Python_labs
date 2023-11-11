from pandas import Series as sr
import numpy as np

# 1
series = sr([1, 2, np.NAN, 3, 4, np.NAN, 7, 8, np.NAN, 10])

# 2
print("Массив без nan:\n", *series[series.notnull()].values)

# 3
series = series ** 0.5
print("\nЗначения под корнем:\n", *series.values)

# 4
series[series.isnull()] = -1
print("\nЗамена элементов nan на -1: ", *series.values)