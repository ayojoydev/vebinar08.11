from math import gcd


class Fraction:
    def __new__(cls, numerator, denominator=1):
        # Проверка, чтобы знаменатель не был равен нулю
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")

        # Создание нового экземпляра класса
        instance = super().__new__(cls)
        return instance

    def __init__(self, numerator, denominator=1):
        # Сокращаем дробь, используя наибольший общий делитель
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

        # Убедимся, что знак дроби всегда находится в числителе
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # Перегрузка операторов математических операций
    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = (self.numerator * other.denominator + other.numerator * self.denominator)
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = (self.numerator * other.denominator - other.numerator * self.denominator)
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Деление на ноль.")
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)
        else:
            return NotImplemented

    # Перегрузка операторов сравнения
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < self.denominator * other.numerator
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator <= self.denominator * other.numerator
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > self.denominator * other.numerator
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator >= self.denominator * other.numerator
        else:
            return NotImplemented


frac1 = Fraction(3, 4)
frac2 = Fraction(1, 2)

# Математические операции
print(frac1 + frac2)  # Вывод: 5/4
print(frac1 - frac2)  # Вывод: 1/4
print(frac1 * frac2)  # Вывод: 3/8
print(frac1 / frac2)  # Вывод: 3/2

# Сравнение дробей
print(frac1 == frac2)  # Вывод: False
print(frac1 > frac2)   # Вывод: True
print(frac1 <= frac2)  # Вывод: False
