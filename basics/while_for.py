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

    print(d**2)
