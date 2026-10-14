#Вариант 3 проверка характеристик числа +
rabota = True
while rabota:
    try:
        a_str = input("Введите число: ")
        a = int(a_str)
    except ValueError:
        print("Введено не число или оно не целое")
        continue

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

    #полный квадрат
    kvadrat = False
    if a >= 0:
        k = int(a ** 0.5)
        #на всякий проверяем соседние, а то корень бывает неточный
        if k * k == a or (k + 1) * (k + 1) == a:
            kvadrat = True
    if kvadrat:
        print("Полный квадрат: да")
    else:
        print("Полный квадрат: нет")

    #спрашиваем продолжать или нет
    while True:
        otvet = input("Проверить ещё одно число? (да/нет): ").lower()
        if otvet == "да":
            break
        elif otvet == "нет":
            rabota = False
            break
        else:
            print("Напишите да или нет")

print("Работа программы завершена.")
