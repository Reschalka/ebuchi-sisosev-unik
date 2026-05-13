import math

def my_cosh(x, eps=10**(-10)):
    result = 1      # будущий результат
    term = 1        # текущее приращение
    i = 1           # номер приращения
    x2 = x * x

    while abs(term) > eps:
        term = term * x2 / ((2*i - 1) * (2*i))
        result = result + term
        i = i + 1

    return result

# Процедура
def my_cosh_proc(x, eps=10**(-10)):
    res = my_cosh(x, eps)
    print(f"ch({x}) = {res}")
    print(f"Проверка math.cosh({x}) = {math.cosh(x)}")
    print(f"Разница: {abs(res - math.cosh(x))}")
    print()

if __name__ == "__main__":
    A = float(input("Введите значение x: "))

    print("\nВызов с одним позиционным параметром")
    print(my_cosh(A))

    print("\nВызов с двумя позиционными параметрами")
    print(my_cosh(A, 10**(-6)))

    print("\nВызов с именованным параметром")
    print(my_cosh(A, eps=10**(-8)))

    print("\nПроцедура")
    my_cosh_proc(A)