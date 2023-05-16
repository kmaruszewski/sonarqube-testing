import re
if __name__ == '__main__':
    print("Podaj działanie:")
    inputed_string = input()


    def findtypeofaction(string):
        signs = ["+", "-", "*", "/"]
        for sign in signs:
            if sign in string:
                action = sign
                return action

    action = findtypeofaction(inputed_string)

    def calculate(input, action):
        if action == "+":
            splittedvalues = input.split("+")
            print("Wynik to", int(splittedvalues[0]) + int(splittedvalues[1]))

        if action == "-":
            splittedvalues = input.split("-")
            print("Wynik to", int(splittedvalues[0]) - int(splittedvalues[1]))

        if action == "/":
            splittedvalues = input.split("/")
            print("Wynik to", int(splittedvalues[0]) / int(splittedvalues[1]))

        if action == "*":
            splittedvalues = input.split("*")
            print("Wynik to", int(splittedvalues[0]) * int(splittedvalues[1]))

    calculate(inputed_string, action)