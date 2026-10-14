#Вариант 4 расчет стоимости покупки
name = input("Товар: ")
if name == "":
    print("Название не может быть пустым")
    exit(1)

try:
    price_str = input("Цена: ").replace(",", ".")
    price = float(price_str)
except ValueError:
    print("Введено не число")
    exit(1)

try:
    kol_str = input("Количество: ")
    kol = int(kol_str)
except ValueError:
    print("Введено не число или оно не целое")
    exit(1)

if price <= 0 or kol <= 0:
    print("Цена и количество должны быть больше нуля")
    exit(1)

itog = price * kol
print("Итого:", itog)

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
print(f"Скидка в процентах: {skidka}%")
print("Скидка в рублях:", skidka_rub)

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

print("Итоговая цена:", round(final, 2))

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
