weight = float(input("Введите вес боксёра: "))

if weight < 0:
    print("Ошибка: вес не может быть отрицательным")
elif weight <= 60:
    print("Категория: легкий вес")
elif weight <= 64:
    print("Категория: первый полусредний вес")
elif weight <= 69:
    print("Категория: полусредний вес")
else:
    print("Не проходит")