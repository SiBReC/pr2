#Вариант 1 консольный калькулятор
import math

try:
    a_str = input("Введите первое число: ").replace(",", ".")
    a = float(a_str)
except ValueError:
    print("Введено не число")
    exit(1)

operation = input("Введите операцию (+, -, *, /, //, %, ^): ")

try:
    b_str = input("Введите второе число: ").replace(",", ".")
    b = float(b_str)
except ValueError:
    print("Введено не число")
    exit(1)


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
            exit(1)
    if operation == "//":
        try:
            c = a // b
            print ("Результат:", c)
        except ZeroDivisionError:
            print("Деление на ноль")
            exit(1)
    if operation == "%":
        try:
            c = a % b
            print ("Результат:", c)
        except ZeroDivisionError:
            print("Деление на ноль")
            exit(1)
    if operation == "^":
        c = math.pow(a, b)
        print ("Результат:", c)




else:
    print("Я не могу выполнить эту операцию")
