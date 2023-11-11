n = int(input("Количество заказов n = "))

humen_orders = dict()
for i in range(n):
    order = input(f"{i+1} заказ: ").split(' ')
    if not order[0] in humen_orders: 
        humen_orders[order[0]] = dict()
    if not order[1] in humen_orders[order[0]]:
        humen_orders[order[0]][order[1]] = int(order[2])
    else:
        humen_orders[order[0]][order[1]] += int(order[2])

humen_orders = dict(sorted(humen_orders.items()))
for humen, orders in humen_orders.items():
    print(f"{humen}:")
    orders = dict(sorted(orders.items()))
    for pizza, count in orders.items():
        print(f"\t{pizza}: {count}")