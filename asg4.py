def number_string(startNumber, endNumber, separator, show):
    # Check if the 'show' parameter is to display "even" numbers
    if show == "even":
        # Create a list of even numbers within the specified range
        numbers = [num for num in range(startNumber, endNumber + 1) if num % 2 == 0]
    # Check if the 'show' parameter is to display "odd" numbers
    elif show == "odd":
        # Create a list of odd numbers within the specified range
        numbers = [num for num in range(startNumber, endNumber + 1) if num % 2 != 0]

    # Join the numbers in the list into a string, separated by the given 'separator'
    result = separator.join(map(str, numbers))
    print(result)
    # Return the resulting string


# Example usage of the function with comments
# Example 1: Print even numbers from 5 to 16, separated by "*"
(number_string(startNumber=5, endNumber=16, separator="*", show="even"))
# Example 2: Print odd numbers from 5 to 16, separated by "#"
(number_string(startNumber=5, endNumber=16, separator="#", show="odd"))
# Example 3: Print odd numbers from 1 to 9, separated by "*"
(number_string(startNumber=1, endNumber=9, separator="*", show="odd"))
# Example 4: Print even numbers from 2 to 8, separated by "#"
(number_string(startNumber=2, endNumber=8, separator="#", show="even"))
