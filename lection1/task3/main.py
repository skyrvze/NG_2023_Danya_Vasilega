def askUser(number):
    return int(input(number))

def answerUser(answer):
    if answer == 1:
        a = int(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit = ", (a * 9/5) + 32)
    else:
        b = int(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius = ", (b - 32) * 5/9)

def main():
    print("this program converts degrees Celsius to Fahrenheit and vice versa")
    answerUser(askUser("1 - Convert Celsius to Fahrenheit\n2 - Convert Fahrenheit to Celsius\n Enter your operate 1 or2 - "))
main()
