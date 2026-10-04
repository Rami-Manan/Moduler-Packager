# Multi-Utility Toolkit
# Run this file:  python main.py

import importlib
from toolkit import datetime_utils, math_utils, random_utils
from toolkit import uuid_utils, file_ops, unit_utils

LINE = "=" * 40


def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Working Hours Calculator")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                now = datetime_utils.current_datetime()
                print("\nCurrent Date and Time:", now)
                file_ops.save_log("Showed current date and time: " + now)
            elif choice == "2":
                d1 = input("\nEnter the first date (YYYY-MM-DD): ")
                d2 = input("Enter the second date (YYYY-MM-DD): ")
                days = datetime_utils.date_difference(d1, d2)
                print("Difference:", days, "days")
                file_ops.save_log("Difference between " + d1 + " and " + d2 + " = " + str(days) + " days")
            elif choice == "3":
                d = input("\nEnter a date (YYYY-MM-DD): ")
                print("Example formats: %d/%m/%Y  or  %A, %d %B %Y")
                fmt = input("Enter the format: ")
                result = datetime_utils.format_date(d, fmt)
                print("Formatted date:", result)
                file_ops.save_log("Formatted " + d + " as " + result)
            elif choice == "4":
                seconds = datetime_utils.stopwatch()
                print("Time taken: %.2f seconds" % seconds)
                file_ops.save_log("Stopwatch time: %.2f seconds" % seconds)
            elif choice == "5":
                secs = int(input("\nEnter seconds for countdown: "))
                datetime_utils.countdown(secs)
                file_ops.save_log("Countdown of " + str(secs) + " seconds finished")
            elif choice == "6":
                start = input("\nEnter start time (HH:MM, 24 hour): ")
                end = input("Enter end time (HH:MM, 24 hour): ")
                hours = datetime_utils.working_hours(start, end)
                print("Working hours: %.2f" % hours)
                file_ops.save_log("Working hours " + start + " to " + end + " = %.2f" % hours)
            elif choice == "7":
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Invalid input, please try again.")
        print(LINE)


def conversion_menu():
    while True:
        print("\nUnit Conversions:")
        print("1. Kilometres to Miles")
        print("2. Miles to Kilometres")
        print("3. Kilograms to Pounds")
        print("4. Pounds to Kilograms")
        print("5. Celsius to Fahrenheit")
        print("6. Fahrenheit to Celsius")
        print("7. Back")
        choice = input("Enter your choice: ")

        if choice == "7":
            break
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice, try again.")
            continue

        try:
            value = float(input("Enter value: "))
            if choice == "1":
                result = unit_utils.km_to_miles(value)
            elif choice == "2":
                result = unit_utils.miles_to_km(value)
            elif choice == "3":
                result = unit_utils.kg_to_pounds(value)
            elif choice == "4":
                result = unit_utils.pounds_to_kg(value)
            elif choice == "5":
                result = unit_utils.celsius_to_fahrenheit(value)
            else:
                result = unit_utils.fahrenheit_to_celsius(value)
            print("Result: %.2f" % result)
            file_ops.save_log("Conversion option " + choice + ": " + str(value) + " -> %.2f" % result)
        except ValueError:
            print("Invalid input, please enter a number.")
        print(LINE)


def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Logarithm")
        print("6. Unit Conversions")
        print("7. GCD, LCM and Prime Check")
        print("8. Back to Main Menu")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                n = int(input("\nEnter a number: "))
                result = math_utils.factorial(n)
                if result is None:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print("Factorial:", result)
                    file_ops.save_log("Factorial of " + str(n) + " = " + str(result))
            elif choice == "2":
                p = float(input("\nEnter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))
                amount, interest = math_utils.compound_interest(p, r, t)
                print("Total Amount: %.2f" % amount)
                print("Compound Interest: %.2f" % interest)
                file_ops.save_log("Compound interest = %.2f, amount = %.2f" % (interest, amount))
            elif choice == "3":
                angle = float(input("\nEnter angle in degrees: "))
                s, c, t = math_utils.trig(angle)
                print("sin = %.4f" % s)
                print("cos = %.4f" % c)
                print("tan = %.4f" % t)
                file_ops.save_log("Trigonometry done for angle " + str(angle))
            elif choice == "4":
                print("\n1. Circle  2. Rectangle  3. Triangle  4. Square")
                shape = input("Choose a shape: ")
                if shape == "1":
                    r = float(input("Enter radius: "))
                    area = math_utils.area_circle(r)
                elif shape == "2":
                    l = float(input("Enter length: "))
                    b = float(input("Enter breadth: "))
                    area = math_utils.area_rectangle(l, b)
                elif shape == "3":
                    b = float(input("Enter base: "))
                    h = float(input("Enter height: "))
                    area = math_utils.area_triangle(b, h)
                elif shape == "4":
                    s = float(input("Enter side: "))
                    area = math_utils.area_square(s)
                else:
                    print("Invalid shape.")
                    continue
                print("Area: %.2f" % area)
                file_ops.save_log("Area calculated = %.2f" % area)
            elif choice == "5":
                x = float(input("\nEnter a positive number: "))
                base = float(input("Enter base (0 for natural log): "))
                result = math_utils.logarithm(x, base)
                print("Logarithm: %.4f" % result)
                file_ops.save_log("Logarithm of " + str(x) + " = %.4f" % result)
            elif choice == "6":
                conversion_menu()
                continue
            elif choice == "7":
                a = int(input("\nEnter first number: "))
                b = int(input("Enter second number: "))
                g, l = unit_utils.gcd_lcm(a, b)
                print("GCD:", g, " LCM:", l)
                n = int(input("Enter a number to check prime: "))
                if unit_utils.is_prime(n):
                    print(n, "is prime")
                else:
                    print(n, "is not prime")
                file_ops.save_log("GCD/LCM of " + str(a) + " and " + str(b) + " = " + str(g) + "/" + str(l))
            elif choice == "8":
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Invalid input, please try again.")
        print(LINE)


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling from Data")
        print("6. Dice Game")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                low = int(input("\nEnter minimum: "))
                high = int(input("Enter maximum: "))
                num = random_utils.random_number(low, high)
                print("Random Number:", num)
                file_ops.save_log("Random number generated: " + str(num))
            elif choice == "2":
                count = int(input("\nHow many numbers: "))
                low = int(input("Enter minimum: "))
                high = int(input("Enter maximum: "))
                numbers = random_utils.random_list(count, low, high)
                print("Random List:", numbers)
                file_ops.save_log("Random list generated: " + str(numbers))
            elif choice == "3":
                length = int(input("\nEnter password length: "))
                print("Generated Password:", random_utils.random_password(length))
                file_ops.save_log("Password of length " + str(length) + " generated")
            elif choice == "4":
                digits = int(input("\nEnter number of digits: "))
                print("Generated OTP:", random_utils.random_otp(digits))
                file_ops.save_log("OTP of " + str(digits) + " digits generated")
            elif choice == "5":
                text = input("\nEnter items separated by commas: ")
                data = text.split(",")
                k = int(input("How many items to pick: "))
                print("Sample:", random_utils.sample_data(data, k))
                file_ops.save_log("Random sampling done on " + str(len(data)) + " items")
            elif choice == "6":
                rounds = int(input("\nHow many rounds: "))
                results = random_utils.dice_game(rounds)
                n = 1
                for player, computer, result in results:
                    print("Round", n, "- You:", player, "Computer:", computer, "->", result)
                    n = n + 1
                file_ops.save_log("Dice game played for " + str(rounds) + " rounds")
            elif choice == "7":
                break
            else:
                print("Invalid choice, try again.")
        except ValueError as e:
            print("Invalid input:", e)
        print(LINE)


def uuid_menu():
    while True:
        print("\nGenerate Unique Identifiers:")
        print("1. Generate UUID")
        print("2. Generate Invoice ID")
        print("3. Generate Session ID")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            value = uuid_utils.generate_uuid()
            print("Generated UUID:", value)
        elif choice == "2":
            value = uuid_utils.invoice_id()
            print("Generated Invoice ID:", value)
        elif choice == "3":
            value = uuid_utils.session_id()
            print("Generated Session ID:", value)
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")
            continue
        file_ops.save_log("Generated ID: " + value)
        print(LINE)


def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Replace text in a file")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("\nEnter file name: ")
                if file_ops.create_file(name):
                    print("File created successfully!")
                    file_ops.save_log("Created file " + name)
                else:
                    print("File already exists.")
            elif choice == "2":
                name = input("\nEnter file name: ")
                data = input("Enter data to write: ")
                file_ops.write_file(name, data)
                print("Data written successfully!")
                file_ops.save_log("Wrote to file " + name)
            elif choice == "3":
                name = input("\nEnter file name: ")
                print("File Content:")
                print(file_ops.read_file(name))
                file_ops.save_log("Read file " + name)
            elif choice == "4":
                name = input("\nEnter file name: ")
                data = input("Enter data to append: ")
                file_ops.append_file(name, data)
                print("Data appended successfully!")
                file_ops.save_log("Appended to file " + name)
            elif choice == "5":
                name = input("\nEnter file name: ")
                old = input("Enter text to replace: ")
                new = input("Enter new text: ")
                count = file_ops.replace_in_file(name, old, new)
                print(count, "replacement(s) done.")
                file_ops.save_log("Replaced text in " + name)
            elif choice == "6":
                break
            else:
                print("Invalid choice, try again.")
        except FileNotFoundError:
            print("File not found. Create it first.")
        print(LINE)


def explore_module():
    print("\nExplore Module Attributes:")
    name = input("Enter module name to explore: ")
    try:
        module = importlib.import_module(name)
    except ModuleNotFoundError:
        print("Module not found. For our own modules type e.g. toolkit.math_utils")
        return
    attributes = []
    for item in dir(module):
        if not item.startswith("_"):    # skip the __ ones
            attributes.append(item)
    print("Available Attributes in", name, "module:")
    print(attributes)
    file_ops.save_log("Explored module " + name)


def main():
    print(LINE)
    print("Welcome to Multi-Utility Toolkit")
    print(LINE)
    file_ops.save_log("Program started")

    while True:
        print("\nChoose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print(LINE)
        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            file_ops.save_log("Program closed")
            print(LINE)
            print("Thank you for using the Multi-Utility Toolkit!")
            print(LINE)
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
