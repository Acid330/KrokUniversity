import math

a = int(input("Input A: "))
b = int(input("Input B: "))
print("A =", a, "B =", b)

print("\n""#1", "\n")
a, b = b, a
print("A =", a, "B =", b)

print("\n""#2.1", "\n")
print("Average number: ", (a + b) / 2)

print("\n""#2.2", "\n")
print("Average geometric number: ", math.sqrt(a + b))

print("\n""#3", "\n")
x = input("Input number: ")
y = list(x)
y.reverse()
x1 = str()
for i in range(len(y)):
    x1 += y.pop(0)
x1 = int(x1)
print(x1)

print("\n""#4", "\n")
hour, minute = 0, 0
second = int(input("Second: "))
while True:
    if second >= 3600:
        second -= 3600
        hour += 1
    elif 60 < second < 3600:
        second -= 60
        minute += 1
    else:
        print("Hour: ", hour, "Minute: ", minute, "Second: ", second)
        break

print("\n""#5", "\n")
print("Значения времени взято с прошлой задачи")
hour_corner = 360 / 12
minute_corner = 360 / 60
second_corner = 360 / 60
cor = "°"
print("Hour: ", int(hour * hour_corner), cor, "Minute: ", int(minute * minute_corner), cor, "Second: ",
      int(second * second_corner), cor)

print("\n""#6", "\n")
x = int(input("Input number: "))

y = x % 2
if y:
    print("Число не парное")
else:
    print("Число парное")
y = x % 10
if y == 5:
    print("Число заканчиваеться на 5")
else:
    print("Число не заканчиваеться на 5")

print("\n""#7", "\n")
day = int(input("Day: "))
Dayweek = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
y = day % 7
if y == 0:
    y += 7
    print(Dayweek[y])
else:
    print(Dayweek[y])
