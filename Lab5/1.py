from pandas import Series as sr

# 1
f = open('a.txt')
dicta = dict([(s.split()[0], int(s.split()[1])) for s in f.readlines()])
f.close()

# 2
series = sr(dicta)

# 3
print("Список учеников:\n", series)

# 4
print("\nУченики из 8 класса:", *series.index[series.values == 8], sep='\n')

# 5
series = series + 1
print("\nВсе учащиеся переведены на 1 класс:\n", series)

# 6
print("\nКоличество учеников в разных классах:\n", series.value_counts())

# 7
print("\nАвдеев: ", series["Avdeev"], "\nЛеонов: ", series["Leonov"])