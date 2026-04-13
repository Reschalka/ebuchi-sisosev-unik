inches_total = int(input("Введите количество дюймов: "))

if inches_total < 0:
    print("Количество не может быть отрицательным")
else:
    # Общее количество дюймов
    total_inches = inches_total

    # Мили
    inches_per_mile = 1760 * 3 * 12  # 1760 ярдов * 3 фута * 12 дюймов
    miles = total_inches // inches_per_mile
    remaining_inches = total_inches % inches_per_mile

    # Ярды
    inches_per_yard = 3 * 12  # 3 фута * 12 дюймов
    yards = remaining_inches // inches_per_yard
    remaining_inches %= inches_per_yard

    # Футы
    feet = remaining_inches // 12
    inches = remaining_inches % 12

    print(f"{total_inches} дюймов")
    print(f"{miles} миль + {yards} ярдов + {feet} футов + {inches} дюймов")