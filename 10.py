n = int(input("Введите количество гостей: "))

cuts1 = 0
pieces = 1
while pieces < n:
    pieces *= 2
    cuts1 += 1
print(f"1) {cuts1} разрезов")

# 2
half = (n + 1) // 2
need_piec2 = n + half
cuts2 = 0
pieces = 1
while pieces < need_piec2:
    pieces *= 2
    cuts2 += 1
print(f"2) {cuts2} разрезов")

# 3
need_piec3 = n + 10
cuts3 = 0
pieces = 1
while pieces < need_piec3:
    pieces *= 2
    cuts3 += 1
print(f"3) {cuts3} разрезов")