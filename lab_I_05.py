#Varinat 7
print("\n""#А", "\n")
n = int(input("Факториал числа: "))
x = 1
for i in range(1,n+1):
    x *= i
print(x)

print("\n""#Б", "\n")
s=str(input("Последовательность от 2 до 20 слов,слова от 1 до 8 букв: "))
if len(s.split())>20:
    print("В последовательности больше 20 слов ,введите последовательность по новой")
    s = str(input("Последовательность от 2 до 20 слов,слова от 1 до 8 букв: "))
elif len(s.split())<2:
    print("В последовательности меньше 2 слов ,введите последовательность по новой")
    s = str(input("Последовательность от 2 до 20 слов,слова от 1 до 8 букв: "))

n = ""
s=s.lower()
for i in range(len(s)):
        s = s.replace('  ', ' ')
if s[-1]==".":
    s = list(s)
    s.remove(".")
    s.append(" .")
    s=n.join(s)
else:
    s = list(s)
    s.append(" .")
    s=n.join(s)

print(s)
x=0
s1=s.split()
s1.remove(".")
for i in range(len(s1)):
    k=len(s1[i])
    for j in range(k):
        if s1[i][j]==s1[i][k-1]:
            print("Слова которые начинаються и заканчиваются одинаковой буквой:", s1[i])
            break
        else:
            break
for i in range(len(s1)):
    if s1[i]!=s1[-1]:
        print("Слова которые отличаются от последнего слова:",s1[i])

print("\n""#В", "\n")
s=str(input("Последовательность слов: "))

n = ""
s=s.lower()
for i in range(len(s)):
        s = s.replace('  ', ' ')

print(s)
x=0
s1=s.split()
b="р"
for i in range(len(s1)):
    k=len(s1[i])
    for j in range(k):
        if b==s1[i][k-1]:
            x+=1
            break
        else:
            break

print(x)
