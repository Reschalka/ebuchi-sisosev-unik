a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

summa = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        summa += i

print(f"Сумма чётных чисел от {a} до {b}: {summa}")