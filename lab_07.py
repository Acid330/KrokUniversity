import numpy as np


def matrix(s):
    a = []
    for i in range(s):
        a.append([])
        for j in range(s):
            a[i] += [int(input())]
            print(a)
    return a


print("\n""#1", "\n")
x = int(input("Количество символов в списке: "))
x1 = list()
for i in range(x):
    x1.append(int(input("Число списка: ")))

print(x1)
x1.reverse()
print(x1)

print("\n""#2", "\n")
s = 3
a = []
a = matrix(s)

b = np.array(a)
print(b)
b1 = b.transpose()
print("\n", b1)

print("\n""#3", "\n")
s = 3
a = matrix(s)

b = np.array(a)
print("\n", b)
print("\n", b.dot(b))

print("\n""#4", "\n")
s = 4
a = matrix(s)

b = np.array(a)
print("\n", b)

for i in range(len(b)):
    j = 0
    for j in range(len(b)):
        if b[i][j] < 0:
            b[i][j] = 0

print("\n", b)
