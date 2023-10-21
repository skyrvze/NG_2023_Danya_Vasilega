UserAnswer = str(input("Choose an orerate with numbers:\n 1. +\n 2. -\n 3. *\n 4. /\n 5. square root\n 6. power\n "))
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

match UserAnswer:
    case "1":
        print("Result = ", a+b)
    case "2":
        print("Result = ", a-b)
    case "3":
        print("Result = ", a*b)
    case "4":
        print("Result = ", a/b)
    case "5":
        print("The square root of the first number = {}, The square root of the second number = {}".format(
            a**0.5, b**0.5))
    case "6":
        FirstPowerOfNumber = int(input("Enter the power for the first number: "))
        SecondPowerOfNumber = int(input("Enter the power for the second number: "))
        print("Power of the first number = {}, Power of the second number = {}".format(a**FirstPowerOfNumber, b**SecondPowerOfNumber))




