
def read_float(msg):
    try:
        return float(input(msg))
    except:
        print("Invalid.")
        return read_float(msg)

# -----------------  CALCULATOR -----------------
def calculator():
    print("\n------ SMART CALCULATOR ------")
    print("Supported operations:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("%  Modulo")
    print("** Power")
    print("------------------------------")

    try:
        num1 = float(input("Enter first number : "))
        op = input("Enter operator (+,-,*,/,%,**) : ")
        num2 = float(input("Enter second number : "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: Division by zero not allowed.")
                return
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        elif op == "**":
            result = num1 ** num2
        else:
            print("Invalid operator.")
            return

        print("Result =", result)

    except:
        print("Invalid input.")

# ----------------- CONVERTER -----------------
def converter():
    print("\n1) C → F")
    print("2) F → C")
    print("3) kg → g")
    print("4) g → kg")
    print("5) inch → cm")
    c = input("Choice: ")

    if c == "1":
        x = read_float("C: ")
        print("F:", x * 9/5 + 32)
    elif c == "2":
        x = read_float("F: ")
        print("C:", (x - 32) * 5/9)
    elif c == "3":
        x = read_float("kg: ")
        print("g:", x * 1000)
    elif c == "4":
        x = read_float("g: ")
        print("kg:", x / 1000)
    elif c == "5":
        x = read_float("inch: ")
        print("cm:", x * 2.54)
    else:
        print("Invalid option.")

# ----------------- TOOLS MENU -----------------
def tools_menu():
    while True:
        print("\n====== TOOLS ======")
        print("1) Calculator")
        print("2) Converter")
        print("3) Back")
        ch = input("Choice: ")

        if ch == "1":
            calculator()
        elif ch == "2":
            converter()
        elif ch == "3":
            return
        else:
            print("Invalid option.")

# ----------------- MAIN MENU -----------------
def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1) Tools")
        print("2) Exit")
        choice = input("Choice: ")

        if choice == "1":
            tools_menu()
        elif choice == "2":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

# ----------------- RUN -----------------
if __name__ == "__main__":
    main()
