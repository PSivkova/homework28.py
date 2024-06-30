print('Задача 1: Фабрика Функций.')
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
# в зависимости от переданных аргументов.


def operation(n):
    if n == '*':
        def multiply(x, y):
            return x * y

        return multiply
    elif n == '/':
        def divide(x, y):
            return x / y

        return divide


my_func = operation('*')
print(my_func(2, 5))
my_func = operation('/')
print(my_func(2, 5))

print('Задача 2: Лямбда-Функции')
# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def.
# Например, возведение числа в квадрат
square = lambda x: x ** 2
print(square(5))


def square(x):
    return x ** 2


print(square(5))

print('Задача 3: Вызываемые Объекты')
# Задача 3: Вызываемые Объекты.
# Создать класс с Rect c полями a, b, которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c):
        return f'{c}{self.a * self.b}'


result = Rect(2, 4)
print(f'Стороны: {result.a}, {result.b}')
print(result("Площадь: "))

