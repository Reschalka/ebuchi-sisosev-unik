# Задание 20.1 - запись трёх столбцов чисел в файл

f = open('table.txt', 'w')

for i in range(1, 101):
    number = i
    square = i ** 2
    cube = i ** 3
    f.write(f"{number}\t{square}\t{cube}\n")

f.close()
print("Файл 'table.txt' успешно создан.")