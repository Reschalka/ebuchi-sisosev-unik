# Задание 20.4 - поиск оценки по фамилии

search_surname = input("Введите фамилию студента: ")

f = open('Зачёт.txt', 'r', encoding='utf-8')
found = False

for line in f:
    parts = line.strip().split('\t')
    if len(parts) == 4:
        surname, name, patronymic, grade = parts
        if surname == search_surname:
            print(f"Оценка студента {surname} {name} {patronymic}: {grade}")
            found = True
            break

if not found:
    print(f"Студент с фамилией '{search_surname}' не найден.")

f.close()