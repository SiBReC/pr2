#Вариант 2 конвертер единиц
print("Выберите конвертер:\n")
print("1.Цельсия в фаренгейты\n"
      "2.Километры в мили\n"
      "3.Килограммы в фунты\n"
      "4.Метры в футы\n"
      "Ваш выбор: ")

try:
    chose_str = input()
    chose = int(chose_str)
except ValueError:
    print("\nНеправильный выбор")
    exit(1)

if chose < 1 or chose > 4:
    print("Нет такого конвертера")
    exit(1)

try:
    if chose == 1:
        x_str = input("Введите температуру: ").replace(",", ".")
    else:
        x_str = input("Введите значение: ").replace(",", ".")
    x = float(x_str)
except ValueError:
    print("Введено не число")
    exit(1)

if chose == 1:
    res = x * 9 / 5 + 32
    print(f"{x} C = {round(res, 2)} F")

if chose == 2:
    res = x * 0.621371
    print(f"{x} км = {round(res, 2)} миль")

if chose == 3:
    res = x * 2.20462
    print(f"{x} кг = {round(res, 2)} фунтов")

if chose == 4:
    res = x * 3.28084
    print(f"{x} м = {round(res, 2)} футов")
