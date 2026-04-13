# Задание 20.2 - запись sin и cos в файл

import math

f = open('trig.txt', 'w')

step = math.pi / 24
x = 0

while x <= 2 * math.pi:
    sin_x = math.sin(x)
    cos_x = math.cos(x)
    f.write(f"{x:.4f}\t{sin_x:.4f}\t{cos_x:.4f}\n")
    x += step

f.close()
print("Файл 'trig.txt' успешно создан.")