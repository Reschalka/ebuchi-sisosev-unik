# Задание 21.1 - чтение бинарного файла с 4 каналами

from struct import unpack
import os

filename = 'Rat.wdq'
channel = int(input("Введите номер отведения (0-3): "))
measurements = 100

f = open(filename, 'rb')
all_data = []

# Читаем весь файл как знаковые 2-байтные числа
while True:
    buffer = f.read(2)
    if not buffer:
        break
    value = unpack('h', buffer)[0]
    all_data.append(value)

f.close()

# Выбираем нужный канал (каналы идут последовательно)
channel_data = all_data[channel::4][:measurements]

# Записываем в текстовый файл
output_name = os.path.splitext(filename)[0] + str(channel) + '.txt'
fw = open(output_name, 'w')
for val in channel_data:
    fw.write(str(val) + '\n')
fw.close()

print(f"Канал {channel} сохранён в '{output_name}'")