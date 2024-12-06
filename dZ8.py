import logging


logging.basicConfig(
    filename='calculation_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

class Calculation:
    def __call__(self, operation, a, b):
        try:
            a = self.check_and_convert(a)
            b = self.check_and_convert(b)

            if operation == '+':
                return a + b
            elif operation == '-':
                return a - b
            elif operation == '*':
                return a * b
            elif operation == '/':
                if b == 0:
                    raise ValueError("Division by zero is not allowed.")
                return a / b
            else:
                raise ValueError(f"Unsupported operation: {operation}")

        except Exception as e:
            logging.error(str(e))
            raise

    def check_and_convert(self, value):
        if isinstance(value, (int, float)):
            return value
        try:
            return float(value)
        except ValueError as e:
            logging.error(f"Cannot convert {value} to int or float: {str(e)}")
            raise ValueError(f"Cannot convert {value} to int or float.")


calc = Calculation()

# Тестові дані
numbers = ['one', 'two', 3, 4, 'five', 'c++', 'c#']

for i in range(len(numbers)):
    try:
        number = calc.check_and_convert(numbers[i])
        print(f'Value at index {i}: {number}')


        if i >= 2:
            print(f'Addition: {calc("+", 2, number)}')
            print(f'Subtraction: {calc("-", 2, number)}')
            print(f'Multiplication: {calc("*", 2, number)}')
            try:
                print(f'Division: {calc("/", 2, number)}')
            except ValueError as e:
                print(e)

    except IndexError:
        print(f'Index {i} is out of range for numbers list.')
    except ValueError as e:
        print(e)