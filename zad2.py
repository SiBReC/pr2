#Вариант 2 конвертер единиц +
rabota = True
while rabota:
    print("Выберите конвертер:\n")
    print("1.Цельсия в фаренгейты\n"
          "2.Километры в мили\n"
          "3.Килограммы в фунты\n"
          "4.Метры в футы\n"
          "5.Литры в галлоны\n"
          "6.Мегабайты в гигабайты\n"
          "7.Часы в минуты\n"
          "8.Рубли в доллары (курс 80)\n"
          "Ваш выбор: ")

    try:
        chose_str = input()
        chose = int(chose_str)
    except ValueError:
        print("\nНеправильный выбор")
        chose = 0

    if chose < 1 or chose > 8:
        print("Нет такого конвертера")
    else:
        try:
            if chose == 1:
                x_str = input("Введите температуру: ").replace(",", ".")
            else:
                x_str = input("Введите значение: ").replace(",", ".")
            x = float(x_str)
        except ValueError:
            print("Введено не число")
            x = None

        if x != None:
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

            if chose == 5:
                res = x * 0.264172
                print(f"{x} л = {round(res, 2)} галлонов")

            if chose == 6:
                res = x / 1024
                print(f"{x} МБ = {round(res, 4)} ГБ")

            if chose == 7:
                res = x * 60
                print(f"{x} ч = {round(res, 2)} мин")

            if chose == 8:
                res = x / 80
                print(f"{x} руб = {round(res, 2)} $")

    #спрашиваем продолжать или нет
    while True:
        otvet = input("Выполнить ещё одно преобразование? (да/нет): ").lower()
        if otvet == "да":
            break
        elif otvet == "нет":
            rabota = False
            break
        else:
            print("Неправильный ответ, напишите да или нет")

print("Работа программы завершена.")
