class Calculator:

    def convert_to_float(self, value: str) -> float:
        """Конвертує рядок в float. Викидає ValueError, якщо конвертація не вдається."""
        try:
            return float(value)
        except ValueError as e:
            print(f"Помилка конвертації: {e}")
            return None
        finally:
            print("Спроба конвертації завершена.")

    def add(self, a: float, b: float) -> float:
        """Додає два числа."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Віднімає друге число від першого."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Множить два числа."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Ділить перше число на друге. Обробляє ділення на нуль."""
        try:
            return a / b
        except ZeroDivisionError as e:
            print(f"Помилка: ділення на нуль - {e}")
            return None
        finally:
            print("Спроба ділення завершена.")


# Приклад використання класу Calculator
calc = Calculator()

# Конвертація рядка в float
value = "10.5"
converted_value = calc.convert_to_float(value)
print(f"Конвертоване значення: {converted_value}")

# Арифметичні операції
if converted_value is not None:
    print(f"Додавання: {calc.add(converted_value, 5)}")
    print(f"Віднімання: {calc.subtract(converted_value, 2)}")
    print(f"Множення: {calc.multiply(converted_value, 3)}")
    print(f"Ділення: {calc.divide(converted_value, 0)}")  # Ділення на нуль для тестування