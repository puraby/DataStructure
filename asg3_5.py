while True:
    user_input = input("Enter a string (or exit): ")

    if user_input.lower() == 'exit':
        print("You exit the game.")
        break

    # Initialize pointers to check symmetry
    start = 0
    end = len(user_input) - 1
    symmetric = True  # Assume the string is symmetric until proven otherwise

    # Loop to check symmetry
    while start < end:
        if user_input[start] != user_input[end]:
            symmetric = False  # Found characters that don't match
            break
        start += 1
        end -= 1

    # Print the result based on the symmetry check
    if symmetric:
        print("The input string is symmetric.")
    else:
        print("The input string is not symmetric.")
