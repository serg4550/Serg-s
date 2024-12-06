print('Lesson 7: Iterators, Closure function')


class Counter:
    limit: int
    step: int
    index: int

    def __init__(self, limit: int, step: int = 1):
        self.index = 0
        self.limit = limit
        self.step = step

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += self.step
        if self.index > self.limit:
            raise StopIteration
        return self.index

    def arithmetic_operations(self):
        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        def multiply(a, b):
            return a * b

        def divide(a, b):
            if b == 0:
                raise ValueError("Division by zero is not allowed.")
            return a / b

        return add, subtract, multiply, divide

    def check_and_convert(self, value):
        if isinstance(value, (int, float)):
            return value
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Cannot convert {value} to int or float.")


numbers = ['one', 'two', 3, 4, 'five', 'c++', 'c#']
counter = Counter(10, step=2)  # Устанавливаем шаг равным 2

# Виклик арифметичних операцій
add, subtract, multiply, divide = counter.arithmetic_operations()

for i in counter:
    try:
        number = counter.check_and_convert(numbers[i])
        print(f'Value at index {i}: {number}')

        # Приклади використання арифметичних операцій
        if i >= 2:  # Для того, щоб уникнути помилок з рядками
            print(f'Addition: {add(2, number)}')
            print(f'Subtraction: {subtract(2, number)}')
            print(f'Multiplication: {multiply(2, number)}')
            try:
                print(f'Division: {divide(2, number)}')
            except ValueError as e:
                print(e)

    except IndexError:
        print(f'Index {i} is out of range for numbers list.')
    except ValueError as e:
        print(e)