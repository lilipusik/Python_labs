import pandas as pd

# 1
file = pd.read_table('marks.csv', sep=';', encoding='windows-1251')

# 2                     
print(file)

# 3
print("\nПервые 50 записей:\n", file.loc[:50, ('Фамилия','Математика')])

# 4
tables = pd.read_html(r"https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2_%D0%B8_%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%8B%D1%85_%D1%82%D0%B5%D1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9_%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D1%8B")
print("\nСтолицы стран Восточной Европы:\n", tables[1][['Название (Официальное название)','Столица']])
print(f"Размер таблицы: {len(tables[1])} * {len(tables[1].columns)}")