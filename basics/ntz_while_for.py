# перебор множеств
os = frozenset({'Windows', 'macOS', 'Ubuntu', 'ChromeOS'})
print(os)

for o in os:
    print(o)

# перебор словаря
d = {'FirstName': 'Boris', 'LastName': 'Ivanov', 'Age': 26}
print(d)

for k in d:
    print(f"{k} - {d[k]}")

for k, v in d.items():
    print(f"{k} - {v}")

for k in d.keys():
    print(k)

for v in d.values():
    print(v)


from collections import namedtuple

names = ('Alex', 'Michael', 'Fedor')
print(type(names))

for n in names:
    print(n)

# перебор именованных кортежей
Info = namedtuple('Information', 'Firstname, Lastname, Age, IsCoder')
info = [Info('Boris', 'Ivanov', 26, True), Info('Alex', 'Petrov', 20, False)]

for i in info:
    print(i)

digitals = range(20)
print(digitals)

for d in digitals:
    if d == 0:
        continue
    if d % 2 == 0:
        print(f"Число {d} четное. Пропускаем итерацию.")
        continue
    if d > 10:
        break

    print(d ** 2)
