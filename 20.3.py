# Задание 20.3 - запись данных о студентах в файл

n = int(input("Введите количество учеников в группе: "))

f = open('Зачёт.txt', 'w', encoding='utf-8')

for i in range(n):
    print(f"\nСтудент {i + 1}:")
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    grade = input("Оценка: ")

    f.write(f"{surname}\t{name}\t{patronymic}\t{grade}\n")

f.close()
print("Файл 'Зачёт.txt' успешно создан.")
