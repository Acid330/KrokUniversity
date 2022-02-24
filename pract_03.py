import math

print("#1", "\n")
for i in range(1, 10):
    print(i)

print("\n""#2", "\n")
for i in range(9, 0, -1):
    print(i)

print("\n""#3", "\n")
for i in range(5, 14):
    if i % 2:
        print(i)

print("\n""#4", "\n")
y = 0
while True:
    x = int(input("Input number: "))
    if x == 0:
        print(y)
        break
    else:
        y += x
        print(y)

print("\n""#5", "\n")
x = input("Input number: ")
y = list(x)
y.reverse()
x1 = str()
for i in range(len(y)):
    x1 += y.pop(0)
x1 = int(x1)
print(x1)

print("\n""#6", "\n")
x = int(input("Input number: "))
print(math.factorial(x))
