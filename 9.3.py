b = int(input("Введите конечное число: "))

summa = 0
for i in range(10, b + 1):
    summa += i

print(f"Сумма чисел от 10 до {b}: {summa}")