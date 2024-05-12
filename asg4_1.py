def displayEquation(num):
    # Convert number to string to easily access its digits
    num_str = str(num)

    # Check if the number is exactly three digits
    if len(num_str) == 3 and num_str.isdigit():
        # Extract each digit
        a, b, c = int(num_str[0]), int(num_str[1]), int(num_str[2])
        # Calculate the product of the digits
        product = a * b * c
        # Display the equation using string formatting
        print("The multiplication of three digits is: {} * {} * {} = {}".format(a, b, c, product))
    else:
        # Display error message if not a three-digit number
        print("The argument should be a positive three-digit number.")


# Example usage
displayEquation(num=99)
displayEquation(num=1000)
displayEquation(num=253)
displayEquation(num=5343)
displayEquation(num=734)
displayEquation(num=25)
