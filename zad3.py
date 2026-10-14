#Вариант 3 проверка характеристик числа
try:
    a_str = input("Введите число: ")
    a = int(a_str)
except ValueError:
    print("Введено не число или оно не целое")
    exit(1)

print("Ваше число:", a)

#положительное отрицательное ноль
if a > 0:
    print("Положительное: да")
elif a < 0:
    print("Положительное: нет (отрицательное)")
else:
    print("Положительное: нет (это ноль)")

#четное
if a % 2 == 0:
    print("Четное: да")
else:
    print("Четное: нет")

#на 3
if a % 3 == 0:
    print("Делится на 3: да")
else:
    print("Делится на 3: нет")

#на 5
if a % 5 == 0:
    print("Делится на 5: да")
else:
    print("Делится на 5: нет")

#простое
prost = True
if a < 2:
    prost = False
for i in range(2, abs(a)):
    if a % i == 0:
        prost = False
        break
if prost:
    print("Простое: да")
else:
    print("Простое: нет")

#кол-во цифр (минус не считаем)
print("Количество цифр:", len(str(abs(a))))
