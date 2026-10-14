#Вариант 4 расчет стоимости покупки +
names = []
prices = []
kols = []

dobavit = True
while dobavit:
    name = input("Введите название товара: ")
    if name.strip() == "":
        print("Название не может быть пустым, введите товар заново")
        continue

    try:
        price_str = input("Введите цену: ").replace(",", ".")
        price = float(price_str)
    except ValueError:
        print("Введено не число, введите товар заново")
        continue

    try:
        kol_str = input("Введите количество: ")
        kol = int(kol_str)
    except ValueError:
        print("Введено не число или оно не целое, введите товар заново")
        continue

    if price <= 0 or kol <= 0:
        print("Цена и количество должны быть больше нуля, введите товар заново")
        continue

    names.append(name)
    prices.append(price)
    kols.append(kol)

    #спрашиваем добавлять еще или нет
    while True:
        otvet = input("Добавить ещё один товар? (да/нет): ").lower()
        if otvet == "да":
            break
        elif otvet == "нет":
            dobavit = False
            break
        else:
            print("Напишите да или нет")

print()
itog = 0
for i in range(len(names)):
    stoim = prices[i] * kols[i]
    print(f"{names[i]}: {stoim}")
    itog += stoim

print("Общая стоимость:", itog)

#скидка
if itog >= 15000:
    skidka = 15
elif itog >= 10000:
    skidka = 10
elif itog >= 5000:
    skidka = 5
else:
    skidka = 0

skidka_rub = itog * skidka / 100
print(f"Скидка: {skidka}%")
print("Размер скидки:", skidka_rub)

final = itog - skidka_rub

#доп функционал: промокод
promo = input("Введите промокод (если нет просто Enter): ")
if promo == "STUDENT":
    print("Промокод принят, еще минус 3%")
    final = final - final * 3 / 100
elif promo == "":
    print("Без промокода")
else:
    print("Такого промокода нет")

#доп функционал: доставка
dost = input("Нужна доставка? (да/нет): ")
if dost == "да":
    if final >= 3000:
        print("Доставка бесплатная")
    else:
        print("Доставка 300 руб")
        final = final + 300
elif dost == "нет":
    print("Самовывоз")
else:
    print("Не понял ответ, считаем что самовывоз")

print("Итоговая стоимость:", round(final, 2))

#доп функционал: оплата
oplata = input("Способ оплаты (1 - карта, 2 - наличные): ")
if oplata == "1":
    print("Кэшбэк 1%:", round(final / 100, 2))
elif oplata == "2":
    try:
        dengi = float(input("Сколько даете денег: ").replace(",", "."))
    except ValueError:
        print("Введено не число")
        exit(1)
    if dengi < final:
        print("Не хватает денег:", round(final - dengi, 2))
    else:
        print("Сдача:", round(dengi - final, 2))
else:
    print("Нет такого способа оплаты")
