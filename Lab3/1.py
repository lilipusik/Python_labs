k = int(input("Количество стран k = "))

set_country = dict()
for i in range(1, k + 1):
    country_cities = input(f"{i} страна: ").split(' ')
    set_country[country_cities[0]] = country_cities[1:]

for i in range(3):
    our_city = input(f"{i+1} город: ")
    flag = False
    for county, cities in set_country.items():
        if our_city in cities:
            print(f"Город {our_city} расположен в стране {county}")
            flag = True
            break
    if not flag:
        print(f"По городу {our_city} данных нет")