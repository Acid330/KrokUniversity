import math


# 1


class Rational:

    def __init__(self, a=3, b=6):
        short = math.gcd(a, b)
        if short != 1:
            self.a = int(a / short)
            self.b = int(b / short)
        else:
            self.a = a
            self.b = b

    def fraction(self):
        return f"{self.a}/{self.b}"

    def point(self):
        return self.a / self.b


rt = Rational()
print(rt.fraction(), rt.point(), "\n")


# 2
class Rectangle:

    min_size=0
    max_size=100

    @classmethod
    def validate(cls, arg):
        return cls.min_size < arg <= cls.max_size

    def __init__(self, width=10, height=5):
        if self.validate(width) and self.validate(height):
            self.width = width
            self.height = height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def area(self):
        return self.width * self.height


rect = Rectangle()
print(rect.perimeter(), rect.area())
