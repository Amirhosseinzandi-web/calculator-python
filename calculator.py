
def isValidNumber(num1 , num2):
    try:
        float(num1)
        float(num2)
        return True
    except ValueError :
        return False
        



def calculator():
    num1 = input("please enter first number \n")
    num2 = input("please enter second number \n")
    op = input("please enter your operator \n")

    if isValidNumber(num1 , num2) :
        num1 = float(num1)
        num2 = float(num2)

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        else:
            print("invalid operator !!!")
            calculator()

    else:
        print("invalid number !!!")
        calculator()

calculator()