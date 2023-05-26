import math

# Силакова Мария Вячеславовна, варинант 21, группа 44-22-114
def convert_value(x):
    if x < 3:
        y = x * math.cos(x**3) + x
    else:
        y = math.sqrt(x) * math.cos(0.0421 * x**2)
    return y

try:
    x = float(input("Введите числовое значение: "))
    result = convert_value(x)
    print("Результат:", result)
except ValueError:
    print("Неверный Ввод. Введите числовое значение.")