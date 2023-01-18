from math import sqrt


message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(number: float) -> float:
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def Calc(your_number: float) -> float:
    if your_number <= 0:
        result: float = 0.0
    else:
        result: float = CalculateSquareRoot(your_number)
    print(f"Мы вычислили квадратный корень из введённого вами числа. "
          f"Это будет: {result}")


print(message)
Calc(25.5)
