while True:
    # Input integers from the user
    first_int = int(input("Enter the 1st integer: "))
    second_int = int(input("Enter the 2nd integer: "))

    # Input operation choice
    operation = input("Enter the math operation (+, -, *, / or exit): ")

    # Process the operation
    if operation == '+':
        result = first_int + second_int
        print("Display addition: {} + {} = {}".format(first_int, second_int, result))
    elif operation == '-':
        result = first_int - second_int
        print("Display subtraction: {} - {} = {}".format(first_int, second_int, result))
    elif operation == '*':
        result = first_int * second_int
        print("Display multiplication: {} * {} = {}".format(first_int, second_int, result))
    elif operation == '/':
        if second_int != 0:
            result = first_int / second_int
            print("Display division: {} / {} = {:.1f}".format(first_int, second_int, result))
        else:
            print("Error: Division by zero is not allowed.")
    elif operation.lower() == 'exit':
        print("EXIT!")
        break
    else:
        print("Invalid operation. Please enter a valid math operation or 'exit'.")



