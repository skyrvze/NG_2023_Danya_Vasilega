UserAnswer = str(input("Виберіть дію з числами:\n 1. +\n 2. -\n 3. *\n 4. /\n 5. корінь\n 6. степінь\n "))
a = int(input("Введіть перше чило: "))
b = int(input("Введіть друге чило: "))

match UserAnswer:
    case "1":
        print("Результат = ", a+b)
    case "2":
        print("Результат = ", a-b)
    case "3":
        print("Результат = ", a*b)
    case "4":
        print("Результат = ", a/b)
    case "5":
        print("Корінь першого числа = {}, Корінь другого числа = {}".format(
            a**0.5, b**0.5))
    case "6":
        FirstPowerOfNumber = int(input("Введіть степінь для першого числа: "))
        SecondPowerOfNumber = int(input("Введіть степінь для першого числа: "))
        print("Степінь першого числа = {}, Степінь другого числа = {}".format(a**FirstPowerOfNumber, b**SecondPowerOfNumber))
    case _:
        print("Такої команди не існує")




