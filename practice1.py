#1
print("Hello world")
#2
print("Krok education")
print("Kosenko Roman")
print("KN-21")
#3
a=int(input("Длина прямоугольника:"))
b=int(input("Длина ширина:"))
print("Площадь прямоугольника:",a*b)
#4
x1=int(input("Введите 1 число: "))
y=int(input("Введите 2 число: "))
m=x1+y
p=x1*y
d=x1/y
c=x1-y
print("Сумма:",m)
print("Произведение:",p)
print("Разность:",d)
print("Частное:",c)
#5
r=int(input("Введите радиус окружнсти:"))
pi=3.14159
D=2*r
S=pi*(r**2)
L=pi*D
print("Диаметр окружности:",D)
print("Площадь окружности:",S)
print("Длинна окружности:",L)
#6
x=[]
x=input("Введите любое число: ")
k,s,p=1,0,1
for i in range(len(x)):
    g=int(x[i])
    j=g//k%10
    s+=j
    p*=j
print("Сумма:",s)
print("Произведение:",p)




