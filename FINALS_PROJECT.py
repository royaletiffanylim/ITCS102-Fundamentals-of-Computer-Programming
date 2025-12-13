# menu_surname.py

import sys

def safe_input(prompt="", default=None):
    try:
        return input(prompt)
    except (OSError, EOFError):
        return default

def print_examples():
    print("\n--- PRINT STATEMENTS EXAMPLE ---")
    print("Hello, World!")
    print("Python is Fun!")
    print("Have a Woderful Day Ahead! \n-Tiff ;p")

def variables_examples():
    print("\n--- VARIABLES EXAMPLE ---")
    name = input("Enter Name Here: ").upper()
    age = input("Enter Age Here: ").upper()
    course = input("Enter Course Here: ").upper()
    section = input("Enter Section Here: ").upper()
    print(f"\nName: {name} \nAge: {age} \nCourse: {course} \nSection: {section}")

def operators_examples():
    print("\n--- OPERATORS EXAMPLE ---")
    a = eval(input("Enter First Number Here: "))
    b = eval(input("Enter Second Number Here: "))
    print("First Number = ", a, "\nSecond Number = ", b)
    print("\nAddition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Modulus:", a % b)
    print("Exponent:", a ** b)
    print("Floor Division:", a // b)

def conditionals_examples(num=None):
    print("\n--- CONDITIONALS EXAMPLE ---")
    if num is None:
        s = safe_input("Enter a number: ", default="0")
        try:
            num = int(s)
        except (TypeError, ValueError):
            num = 0
    if num > 0:
        print("Number Entered is a Positive Number")
    elif num < 0:
        print("Number Entered is a Negative Number")
    else:
        print("Zero")

def loops_examples():
    print("\n--- LOOPS EXAMPLE ---")
    print ("🦜 PARROT SIMULATOR - THE ECHO CHAMBER") 
    word = input("What Do You Want Your Parrot To Say? ")
    squawk  = eval(input("How many times should the Parrot squawk it? ")) 

    print ("Listen to your Parrot:")
    for s in range (squawk, 0, -1) :
        print ("🦜 SQUAWK!", word,"!")

def lists_examples():
    print("\n--- LISTS EXAMPLE ---")
    fruits = ["apple", "banana", "cherry"]
    print("Fruits:", fruits)
    add = input("Enter Fruit to be Added: ")
    fruits.append(add)
    print("After adding orange:", fruits)

def functions_examples(name=None):
    print("\n--- FUNCTIONS EXAMPLE ---")
    def greet(name):
        return f"Hello, {name}! Keep Moving Forward! :p"
    if name is None:
        name = safe_input("Enter Your Name: ", default="User")
        if name is None:
            name = "User"
    print(greet(name))

def run_user_program(code_lines=None):
    print("\n--- RUN YOUR OWN PYTHON CODE ---")
    if code_lines is None:
        print("Type Your Python Code Below. Type 'END' On A New Line To Run It.")
        code_lines = []
        while True:
            line = safe_input("", default=None)
            if line is None:
                break
            if line.strip().upper() == "END":
                break
            code_lines.append(line)
    if not code_lines:
        print("No Code Provided.")
        return
    user_code = "\n".join(code_lines)
    try:
        exec(user_code, {})
    except Exception as e:
        print("Error in your code:", e)

def submenu(title, actions):
    while True:
        print(f"\n--- {title} MENU ---")
        for i, option in enumerate(actions.keys(), start=1):
            print(f"{i}. {option}")
        print("0. Back to Main Menu")
        choice = safe_input("Enter choice: ", default=None)
        if choice is None:
            print("No Input Available. Returning To Main Menu.")
            break
        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(actions):
            list(actions.values())[int(choice) - 1]()
        else:
            print("Invalid choice. Try again.")

def main_menu():
    while True:
        print("\n===== PYTHON FUNDAMENTALS INTERACTIVE MENU =====")
        print("1. Print Statements")
        print("2. Variables")
        print("3. Operators")
        print("4. Conditionals")
        print("5. Loops")
        print("6. Lists")
        print("7. Functions")
        print("8. Run Your Own Program")
        print("0. Exit")
        choice = safe_input("Enter Your Choice: ", default=None)
        if choice is None:
            print("No input available. Exiting Interactive Menu.")
            break
        if choice == "1":
            submenu("PRINT STATEMENTS", {"Printing Sample Program": print_examples})
        elif choice == "2":
            submenu("VARIABLES", {"Variables Sample Program": variables_examples})
        elif choice == "3":
            submenu("OPERATORS", {"Basic Operators": operators_examples})
        elif choice == "4":
            submenu("CONDITIONALS", {"If-Else Sample Program": conditionals_examples})
        elif choice == "5":
            submenu("LOOPS", {"Loops Sample Program": loops_examples})
        elif choice == "6":
            submenu("LISTS", {"List Operations": lists_examples})
        elif choice == "7":
            submenu("FUNCTIONS", {"Function Sample Program": functions_examples})
        elif choice == "8":
            run_user_program()
        elif choice == "0":
            print("Exiting Program... Thank You For Interacting With Me! \nHope You Enjoyed Interacting With Me!")
            try:
                sys.exit()
            except SystemExit:
                break
        else:
            print("Invalid Option. Try Again.")

def run_tests():
    print("\n=== RUNNING AUTOMATED TESTS ===")
    print_examples()
    variables_examples()
    operators_examples()
    conditionals_examples(num=-5)
    conditionals_examples(num=0)
    conditionals_examples(num=7)
    loops_examples()
    lists_examples()
    functions_examples(name="Alice")
    run_user_program(code_lines=["print('Hello from user code')"]) 
    print("=== TESTS COMPLETED ===")

# ===== PROGRAM START =====
probe = safe_input("Enter Name Here: ").upper()
confirm = safe_input("Are You Ready To Run This Menu? (yes/no): ")

if confirm.lower() == "yes":
    print(f"\nWELCOME, {probe}!")
    main_menu()
else:
    print("Thank You For Interacting With Me!")