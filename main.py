print("Задание 1")
n = 0
s = 0
c = 0
v = []
while True:
    u = int(input())
    if u == 0:
        break
    s += u
    c += 1
    v.append(u)
avg = s / c
print(avg)
for u in v:
    if u % 2 == 0:
        print(u + avg)
    else:
        print(u)

print("Задание 2")
z = int(input())
x = ['кофе', 'чай','компот', 'какао']
m = " "
for i in range(z):
    k = i % len(x)
    m += x[k] + " "
print(m)

print("Задание 3")
w = []
while True:
    e = input()
    if e == 'STOP':
        break
    w.append(e)
r = sorted(set(w))
for e in r:
    print(e)

print("Задание 4")
a = int(input('Количество студентов: '))
for _ in range(a):
    b = input('ФИО студента: ')
    c = []
    for _ in range(5):
        d = int(input('Оценка студента: '))
        c.append(d)
    q = c.count(5)
    w = c.count(4)
    e = c.count(3)
    r = sum(c) / len(c)
    print(f'{b}\t{q}\t{w}\t{e}\t{r}')


