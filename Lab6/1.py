import pandas as pd
import datetime

# 1
table = pd.read_csv('weather1.csv', sep=';', header=6)
table.drop(table.columns[[len(table.columns)-1]], axis=1, inplace=True)
print(table)

# 2
table.drop(['ff10', 'ff3', 'WW' , 'W1', 'W2', 'Tn', 'Tx', 'Cl', 'Cm', 'Ch'], axis=1, inplace=True)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(table[:10])

# 3
def number_action():
    print('\n1. Погода за месяц\n'
          + '2. Средняя температура\n'
          + '3. Максимальная температура\n'
          + '4. Минимальное давление\n'
          + '5. Среднесуточная температура\n'
          + '6. Выход\n')
    return int(input('Введите номер действия: '))

table['Местное время в Перми'] = pd.to_datetime(table['Местное время в Перми'])
while(True):
    match number_action():
        case 1:
            month = int(input('Введите месяц цифрой: '))
            print("Информация по выбранному месяцу:\n", 
                  (table[table['Местное время в Перми'].dt.month == month]).sort_values(by='Местное время в Перми'))

        case 2:
            month = int(input('Введите месяц цифрой: '))
            print("Средняя температура за выбранный месяц: ",
                  (table[table['Местное время в Перми'].dt.month == month])['T'].mean())

        case 3:
            month = int(input('Введите месяц цифрой: '))
            time = list(map(int, input('Введите время: ').split(':')))
            max_temp = (table[(table['Местное время в Перми'].dt.time == datetime.time(hour=time[0], minute=time[1])) &
                              (table['Местное время в Перми'].dt.month == month)])['T'].max()
            print("Все дни с максимальной температурой за указанный месяц и время:\n",
                  table[(table['Местное время в Перми'].dt.month == month) & (table['T'] == max_temp)])

        case 4:
            month = int(input('Введите месяц цифрой: '))
            print("Минимальное давление за выбранный месяц: ",
                  (table[table['Местное время в Перми'].dt.month == month])['Po'].min())
            
        case 5:
            date = list(map(int, input('Введите дату: ').split('.')))
            print("Средняя температура за выбранный день: ",
                  (table[(table['Местное время в Перми'].dt.month == date[1]) &
                        (table['Местное время в Перми'].dt.day == date[0])])['T'].mean())

        case 6: break
            