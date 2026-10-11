COINS = [50, 10, 5, 2, 1]

amount = int(input("Введите сумму сдачи: "))

if amount < 0:
    print("Сумма не может быть отрицательной")
else:
    remaining = amount

    print("Сдача монетами:")
    for coin in COINS:
        count = remaining // coin
        remaining = remaining % coin
        print(f"{coin} сом: {count} шт.")
