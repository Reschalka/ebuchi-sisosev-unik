num = input("Введите число: ")
max_digit = num[0]

for digit in num:
    if digit > max_digit:
        max_digit = digit

count_max = num.count(max_digit)
print(f"Макс цифра: {max_digit}")
print(f"Встречается: {count_max}")