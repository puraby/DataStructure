def display_integer(number, count, operator):
    if operator == "backward":
        # Loop for the specified count, decrementing each time
        for i in range(1, count + 1):
            print("number {} is: {}".format(i, number - (i - 1)))
    elif operator == "forward":
        # Loop for the specified count, incrementing each time
        for i in range(1, count + 1):
            print("number {} is: {}".format(i, number + (i - 1)))
    else:
        # If the operator is neither "backward" nor "forward"
        print("Please input a backward or forward operator.")

# Example usage
print("=======")
display_integer(number=100, count=3, operator="backward")
print("=======")
display_integer(number=100, count=3, operator="forward")
print("=======")
display_integer(number=100, count=3, operator="none")
print("=======")
