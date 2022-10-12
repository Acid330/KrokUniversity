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

    def __init__(self, width=10, height=5):
        if width > 100 or height > 100 or width <= 0 or height <= 0:
            raise Exception("width or height more then 100 or less then 1")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def area(self):
        return self.width * self.height


rect = Rectangle()
print(rect.perimeter(), rect.area())
