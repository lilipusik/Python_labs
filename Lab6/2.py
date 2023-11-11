import pandas as pd

# 1
table = pd.read_csv('FIFA.csv', sep=',')

# 2
print(table.groupby('Year').count()['Datetime'])

# 3
pd.set_option('display.max_rows', None)
print(table[table['Year'] == 2014][['Datetime', 'City']])

# 4
table.insert(loc=9, column='Goals', value=list(table['Home.Team.Goals'] + table['Away.Team.Goals']), allow_duplicates=True)
print(table[['Datetime', 'Goals', 'Home.Team.Name', 'Away.Team.Name']])

# 5
print(table.groupby('Year').agg({'Goals' : ['count', 'max', 'min']}))

# 6
print(table.groupby(['City', 'Stadium']).count()['Datetime'])

# 7
print(table.groupby('Datetime').agg({'Goals' : 'mean'}))

# 8
years = table.groupby('Year').agg({'Goals' : 'sum'})
print(years[years['Goals'] > 150])