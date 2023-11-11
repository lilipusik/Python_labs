num = input("Введите число: ").rstrip('0')
if float(num) // 1 <= 0:
    step = num.lstrip('0.')
    count = len(num) - len(step) - 1
    num = step[0] + "." + step[1:]
    print(f"x = {num} * 10^(-{count})")
else:
    step = num.replace('.','')
    number = int(float(num))
    x = 0
    while number > 10:
        number //= 10
        x += 1
    print(f"x = {step[0]}.{step[1:]} * 10^({x})")
