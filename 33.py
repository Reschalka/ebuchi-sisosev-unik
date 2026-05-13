# Задание 33

import math


def my_range_square(start=None, stop=None, step=None):
    # Определяем, сколько параметров передано
    if stop is None:
        # Передан только один параметр
        stop = start
        start = 0
        step = 1
    elif step is None:
        step = 1

    # Генерируем числа и возводим в квадрат
    result = []
    i = start
    while i < stop:
        result.append(i ** 2)
        i += step

    return result


if __name__ == "__main__":

    # 1 параметр: квадраты от 0 до 4
    print("\n1. my_range_square(5):")
    print(f"   {my_range_square(5)}")

    # 2 параметра: квадраты от 2 до 6
    print("\n2. my_range_square(2, 7):")
    print(f"   {my_range_square(2, 7)}")

    # 3 параметра: квадраты от 1 до 10 с шагом 2
    print("\n3. my_range_square(1, 11, 2):")
    print(f"   {my_range_square(1, 11, 2)}")


    print("\nmy_range_square(10):", my_range_square(10))
    print("  (квадраты от 0 до 9)")

    print("\nmy_range_square(3, 8):", my_range_square(3, 8))
    print("  (квадраты от 3 до 7)")

    print("\nmy_range_square(0, 20, 3):", my_range_square(0, 20, 3))
    print("  (квадраты чисел 0, 3, 6, 9, 12, 15, 18)")