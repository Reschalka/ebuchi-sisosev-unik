with open('cisla.txt', 'r', encoding='utf-8') as f:
    numbers = [float(line.strip()) for line in f if line.strip()]

squares = list(map(lambda x: x**2, numbers))
result = sum(squares)

print(f"Сумма квадратов чисел: {result}")