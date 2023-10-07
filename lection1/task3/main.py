def askUser(number):
    return int(input(number))


def answerUser(answer):
    if answer == 1:
        a = int(input("Введіть температуру в градусах: "))
        print("Температура в фаренгейтах = ", (a * 9/5) + 32)
    else:
        b = int(input("Введіть температуру в фаренгейтах: "))
        print("Температура в градусах = ", (b - 32) * 5/9)


def main():
    answerUser(askUser(
        "1 - Перевести градуси в фаренгейти\n2 - Перевести фаренгейти в градуси\n Введіть 1 чи 2 - "))


main()
