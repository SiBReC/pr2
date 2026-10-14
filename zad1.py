#Вариант 1 консольный калькулятор +
import math

rabota = True
while rabota:
    try:
        a_str = input("Введите первое число: ").replace(",", ".")
        a = float(a_str)
    except ValueError:
        print("Введено не число, попробуйте заново")
        continue

    operation = input("Введите операцию (+, -, *, /, //, %, ^): ")

    try:
        b_str = input("Введите второе число: ").replace(",", ".")
        b = float(b_str)
    except ValueError:
        print("Введено не число, попробуйте заново")
        continue


    if operation in ("+", "-", "*", "/", "//", "%", "^"):
        if operation == "+":
            c = a + b
            print("Результат:", c)
        if operation == "-":
            c = a - b
            print ("Результат:", c)
        if operation == "*":
            c = a * b
            print ("Результат:", c)
        if operation == "/":
            try:
                c = a / b
                print ("Результат:", c)
            except ZeroDivisionError:
                print("Деление на ноль")
        if operation == "//":
            try:
                c = a // b
                print ("Результат:", c)
            except ZeroDivisionError:
                print("Деление на ноль")
        if operation == "%":
            try:
                c = a % b
                print ("Результат:", c)
            except ZeroDivisionError:
                print("Деление на ноль")
        if operation == "^":
            try:
                c = math.pow(a, b)
                print ("Результат:", c)
            except (ValueError, OverflowError):
                print("Не получается посчитать степень")
    else:
        print("Я не могу выполнить эту операцию")

    #спрашиваем продолжать или нет
    while True:
        otvet = input("Хотите выполнить ещё одну операцию? (да/нет): ").lower()
        if otvet == "да":
            break
        elif otvet == "нет":
            rabota = False
            break
        else:
            print("Напишите да или нет")

print("Работа программы завершена.")
