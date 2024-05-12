while True:
    # Input integers from the user
    first_int = int(input("Enter the 1st integer: "))
    second_int = int(input("Enter the 2nd integer: "))

    # Input operation choice
    operation = input("Enter the math operation (+, -, *, / or exit): ")

    # Process the operation
    if operation == '+':
        result = first_int + second_int
        print(f"Display addition: {first_int} + {second_int} = {result}")
    elif operation == '-':
        result = first_int - second_int
        print(f"Display subtraction: {first_int} - {second_int} = {result}")
    elif operation == '*':
        result = first_int * second_int
        print(f"Display multiplication: {first_int} * {second_int} = {result}")
    elif operation == '/':
        if second_int != 0:
            result = first_int / second_int
            print(f"Display division: {first_int} / {second_int} = {result:.1f}")
        else:
            print("Error: Division by zero is not allowed.")
    elif operation.lower() == 'exit':
        print("EXIT!")
        break
    else:
        print("Invalid operation. Please enter a valid math operation or 'exit'.")
