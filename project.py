import re, sys
from pyfiglet import Figlet


def main():
    while True:
        try:
            exp = get_exp()
            if exp == "EXIT":
                raise Exception
            f = get_f()
            if f == "EXIT":
                raise Exception
            match = re.search(r'^(\d\.)?(\d*) (\+|-|\*|/) (\d\.)?(\d*)$', exp)
            if match:
                num1, num2, oprtr = def_nums(exp)
                if oprtr == "+":
                    ans = addition(num1, num2)
                elif oprtr == "-":
                    ans = subtraction(num1, num2)
                elif oprtr == "*":
                    ans = multiplication(num1, num2)
                elif oprtr == "/":
                    ans = division(num1, num2)
                print_output(ans, f)
            else:
                raise ValueError
        except ValueError:
            sys.exit("ValueError")
        except Exception:
            sys.exit("\nExiting...\nExiting...\nExiting...")

def get_exp():
    print("\n\nThis is an infinite arithmetic calculator that adds/subtracts/multiplies/divides two numbers.\nEnter \"EXIT\" to exit.")
    exp = input("\n\nInput the expression to be calculated: ")
    return exp


def get_f():
    print("Please choose fonts from below.\n\tbulbhead\n\tdigital\n\tfuzzy\n\tlarry3d\n\tlean\n\tletters\n\tsmkeyboard\n\tspeed\n\tbubble")
    f = input("Input font: ")
    return f


def def_nums(exp):
    num1, oprtr, num2 = exp.split(" ")
    num1, num2 = float(num1), float(num2)
    return num1, num2, oprtr

def addition(num1, num2):
    ans = num1+num2
    return ans


def subtraction(num1, num2):
    ans = num1-num2
    return ans


def multiplication(num1, num2):
    ans = num1*num2
    return ans


def division(num1, num2):
    ans = num1/num2
    return ans


def print_output(ans, f):
    figlet = Figlet()
    figlet.setFont(font=f)
    print("\nAscii: ")
    print(figlet.renderText(f"= {round(ans, 3)}"))
    print(f"For those who can't read ASCII...\n= {round(ans, 3)}")


if __name__ == "__main__":
    main()
