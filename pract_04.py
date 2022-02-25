print("\n""#1", "\n")
x1, x2, x3, x4 = input("Введите 4 числа через пробел: ").split()
print(max(int(x1), int(x2), int(x3), int(x4)))

print("\n""#2", "\n")
x = int(input("Год: "))
if x % 4 == 0:
    print("Высокостный год")
else:
    print("не высокостный год")

print("\n""#3", "\n")
a = int(input("Сторона a: "))
b = int(input("Сторона b: "))
c = int(input("Сторона c: "))
if a + b > c or b + c > a or c + a > b:
    print("Трикутник існує")
else:
    print("Трикутник не існує")

print("\n""#4", "\n")
for i in range(0, 101, 7):
        print(i)

print("\n""#5", "\n")
fact1 = int(input("Число для вычесляния факториала: "))
n, i = 1, 1
while i < fact1:
    i += 1
    n *= i
print(n)

print("\n""#6", "\n")
x = int(input("Ширина часов (нечётные числа): "))
i = 0
x1 = x
while x > 0:
    if x > 1:
        print(i * " ", end="")
        print(x * "*")
        x -= 2
        i += 1
    else:
        print(i * " ", end="")
        print("*")
        x = 0
x = 1
i = int(((x1 - 1) / 2) - 1)
while x < x1:
    if x < x1:
        x += 2
        print(i * " ", end="")
        print(x * "*")
        i -= 1
    else:
        print(x1 * "*")
        x = 0
