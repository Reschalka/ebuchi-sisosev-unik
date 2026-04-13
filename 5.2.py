import math

print("Решение квадратного уравнения")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

if a == 0:
    print("Это не квадратное уравнение")
else:
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Два корня: {x1:.2f}, {x2:.2f}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Один корень: {x:.2f}")
    else:
        print("Действительных корней нет")