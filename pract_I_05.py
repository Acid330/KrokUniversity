import string

print("\n""#1", "\n")
sqrtlist_01 = list()
for i in range(1, 31):
    sqrtlist_01.append(i ** 2)
print(sqrtlist_01)

print("\n""#2", "\n")
exam_st_date = input("Дату: ")
exam_st_date = exam_st_date.split()
print(exam_st_date[1], exam_st_date[0], exam_st_date[2], sep="/")

print("\n""#3", "\n")
f = string.punctuation
number = str(input("Числа: "))
print(number)
for i in range(len(f)):
    number = number.replace(f[i], '')

number = number.split()
x1 = list()
for i in range(len(number)):
    x1.append(number[i])
x2 = tuple(x1)
print(x1, "\n", x2)

print("\n""#4", "\n")
a = list(input("1 список: "))
b = list(input("2 список: "))
print(bool(set(a) & set(b)))

print("\n""#5", "\n")
x = int(input("Количество остановок: "))
number = tuple()
result = 0

for i in range(x):
    x1 = int(input("Зашло на остановке: "))
    x2 = int(input("Вышло на остановке: "))
    x3 = tuple([[x1, x2]])
    number += x3

for i in range(len(number)):
    result += number[i][0] - number[i][1]
print(result)
