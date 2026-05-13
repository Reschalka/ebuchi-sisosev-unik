from functools import reduce

with open('texts.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Разбиваем на слова
words = text.split()

# Фильтруем:
words_on_u = list(filter(lambda w: w.lower().startswith('у'), words))

if words_on_u:
    longest = reduce(lambda a, b: a if len(a) >= len(b) else b, words_on_u)
    print(f"Самое длинное слово на 'у': {longest} (длина: {len(longest)})")
else:
    print("Слов на букву 'у' не найдено")



# # Читаем файл
# with open('text.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#
# # Разбиваем на слова
# words = text.split()
#
# # Фильтруем:
# words_end_iy = list(filter(lambda w: w.endswith('ый'), words))
#
# if words_end_iy:
#     shortest = min(words_end_iy, key=len)
#     print(f"Самое короткое слово на '-ый': {shortest} (длина: {len(shortest)})")
# else:
#     print("Слов на '-ый' не найдено")


# with open('text.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#
# # Убираем символ переноса строки в конце
# lines = [line.rstrip('\n') for line in lines]
#
# longest_line = max(lines, key=len)
#
# print(f"Самая длинная строка ({len(longest_line)} символов):")
# print(longest_line)