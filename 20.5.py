# Задание 20.5 - выделение одного отведения из ЭЭГ

import os

input_filename = 'EEG.txt'
channel_number = int(input("Введите номер отведения (0-15): "))

fr = open(input_filename, 'r')
data = []

for line in fr:
    columns = line.strip().split('\t')
    if len(columns) > channel_number:
        data.append(columns[channel_number])

fr.close()

# Формируем имя выходного файла
base_name = os.path.splitext(input_filename)[0]
output_filename = base_name + str(channel_number) + '.txt'

fw = open(output_filename, 'w')
for value in data:
    fw.write(value + '\n')
fw.close()

print(f"Отведение {channel_number} сохранено в файл '{output_filename}'")