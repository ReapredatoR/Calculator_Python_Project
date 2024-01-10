# defining functions for each operation
def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a**b


def terminate():
    print("Done. Terminating")
    exit()


# defining function to select operation
def select_op(choice):
    if choice != "#" and choice != "$" and choice in ["+", "-", "*", "/", "^", "%"]:
        a = input("Enter first number: ")
        if a == "0$":
            print(a)
            return
        elif a == "#":
            print("Done. Terminating")
            exit()
        else:
            a = float(a)
            print(int(a))

        b = input("Enter second number: ")
        if b == "0$":
            print(b)
            return
        elif b == "#":
            print(b)
            print("Done. Terminating")
            exit()

        else:
            b = float(b)
            print(int(b))
        if choice == "+":
            print(f"{a} + {b} = {add(a, b)}")
        if choice == "-":
            print(f"{a} - {b} = {substract(a, b)}")
        if choice == "*":
            print(f"{a} * {b} = {multiply(a, b)}")
        if choice == "/":
            if b == 0:
                print("float division by zero")
                print(f"{a} / {b} = None ")
            else:
                print(f"{a} / {b} = {divide(a, b)}")
        if choice == "^":
            print(f"{a} ^ {b} = {power(a, b)}")
        if choice == "%":
            print(f"{a} % {b} = {remainder(a, b)}")
    elif choice == "#":
        print("Done. Terminating")
        exit()
    elif choice == "$" or choice == "0$":
        return
    else:
        print("Unrecognized operation")


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if select_op(choice) == -1:
        print("Done. Terminating")
        exit()
