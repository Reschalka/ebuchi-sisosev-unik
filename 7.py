# a) 1, 2, 3, 4, ...
def seq_a(n):
    if n == 1:
        return 1
    return seq_a(n-1) + 1

# b) 0, 5, 10, 15, ...
def seq_b(n):
    if n == 1:
        return 0
    return seq_b(n-1) + 5

# c) 1, 1, 1, 1, ...
def seq_c(n):
    if n == 1:
        return 1
    return seq_c(n-1)

# d) 1, -1, 1, -1, ...
def seq_d(n):
    if n == 1:
        return 1
    return -seq_d(n-1)

# e) 1, -2, 3, -4, 5, -6, ...
def seq_e(n):
    if n == 1:
        return 1
    return (-1)**(n+1) * n

# f) 2, 4, 8, 16, ...
def seq_f(n):
    if n == 1:
        return 2
    return seq_f(n-1) * 2

# g) 2, 4, 16, 256, ...
def seq_g(n):
    if n == 1:
        return 2
    return seq_g(n-1) ** 2

# h) 0, 1, 2, 3, 0, 1, 2, 3, 0, ...
def seq_h(n):
    if n == 1:
        return 0
    return (seq_h(n-1) + 1) % 4

# i) 11, 31, 51, 71, ...
def seq_i(n):
    if n == 1:
        return 11
    return seq_i(n-1) + 20

print("a:", [seq_a(i) for i in range(1, 6)])
print("b:", [seq_b(i) for i in range(1, 6)])
print("c:", [seq_c(i) for i in range(1, 6)])
print("d:", [seq_d(i) for i in range(1, 6)])
print("e:", [seq_e(i) for i in range(1, 7)])
print("f:", [seq_f(i) for i in range(1, 6)])
print("g:", [seq_g(i) for i in range(1, 6)])
print("h:", [seq_h(i) for i in range(1, 10)])
print("i:", [seq_i(i) for i in range(1, 6)])