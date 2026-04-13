x = float(input("Расстояние от вас до ближайшего столба: "))
y = float(input("Расстояние между столбами: "))
n = int(input("Номер столба: "))
distance = x + (n - 1) * y
print(f"Расстояние от вас до {n} столба: {distance:.2f} м")