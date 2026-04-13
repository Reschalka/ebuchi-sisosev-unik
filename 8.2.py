# Задание 12
count = 0
sum_num = 0

while True:
    num = float(input("Введите число: "))
    count += 1
    sum_num += num

    if num >= 10:
        break

print(f"Введено чисел: {count}")
print(f"Сумма: {sum_num}")