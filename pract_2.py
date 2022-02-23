import math

print("Task #1", "\n")

x = int(input("Input x: "))
y = int(input("Input y: "))
z = int(input("Input z: "))

# 1
tmp = x % 2
print("1)x is odd?", end=" = ")
if tmp == 1:
    print(bool(1), "\n")
else:
    print(bool(0), "\n")

# 2
print("2)x is a multiple of 20?", end=" = ")
tmp = x % 20
if tmp == 0:
    print(bool(1), "\n")
else:
    print(bool(0), "\n")

# 3
print("3)x and y are both positive?", end=" = ")
if x > 0 and y > 0:
    print(bool(1), "\n")
else:
    print(bool(0), "\n")

# 4
print("4)x and y have the same sign?", end=" = ")
if x > 0 and y > 0 or x < 0 and y < 0:
    print(bool(1), "\n")
else:
    print(bool(0), "\n")
# 5
print("5)x and y have different signs?", end=" = ")
if x > 0 and y < 0 or x < 0 and y > 0:
    print(bool(1), "\n")
else:
    print(bool(0), "\n")
# 6
print("6)x, y, and z are bound to equal values?", end=" = ")
print(bool(x == y == z), "\n")
# 7
print("7)x, y, and z are bound to different values?", end=" = ")
if x == y or x == z or y == z or x == y == z:
    print(bool(0), "\n")
else:
    print(bool(1), "\n")
# 8
print("8)two variables store the same value, but the third one is different?", end=" = ")
if x == y != z or x == z != y or y == z != x:
    print(bool(1), "\n")
else:
    print(bool(0), "\n")

print("Task #2", "\n")
x1, y1 = input("Input x1,y1: ").split()  # Через пробел в одну строку 2 числа (2 4)
x2, y2 = input("Input x2,y2: ").split()
x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
A = x1, y1
B = x2, y2
print("A =", A)
print("B =", B)
# 1
print("1)distance between A and B?", end=" = ")
print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), "\n")
# 2
print("2)the slope of the line from the A to B?", end=" = ")
if x1 - x2 == 0:
    print(bool(0), "\n")
else:
    print((y2 - y1) / (x2 - x1), "\n")
# 3
print("3)whether both points lie on the same line from the origin?", end=" = ")
if x1 == x2 or y1 == y2:
    print(bool(1), "\n")
else:
    print(bool(0), "\n")
# 4
print("4)whether the first point is above the second", end=" = ")
if x1 > x2 and y1 > y2:
    print(bool(1), "\n")
else:
    print(bool(0), "\n")
# 5
print("5)what quadrant the first point lies in (1st, 2nd, 3rd, or 4th)", end=" = ")
if x1 > 0 and y1 > 0:
    print("2st", "\n")
    u1 = 2
elif x1 < 0 and y1 < 0:
    print("3st", "\n")
    u1 = 3
elif x1 < 0 and y1 > 0:
    print("1st", "\n")
    u1 = 1
elif x1 > 0 and y1 < 0:
    print("4st", "\n")
    u1 = 4
# 6
print("6)whether the two points lie in the same quadrant", end=" = ")
if x2 > 0 and y2 > 0:
    u2 = 2
elif x2 < 0 and y2 < 0:
    u2 = 3
elif x2 < 0 and y2 > 0:
    u2 = 1
elif x2 > 0 and y2 < 0:
    u2 = 4

print(u1 == u2)
