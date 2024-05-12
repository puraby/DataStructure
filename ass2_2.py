# Prompting the user to input the first integer
num1 = int(input("Enter the 1st integer: "))
# Prompting the user to input the second integer
num2 = int(input("Enter the 2nd integer: "))
# Prompting the user to input the divisor
divisor = int(input("Enter the 3rd integer: "))

# Printing a message to indicate which numbers will be printed
print(f"Print all the numbers between {num1} and {num2} that can be divided by {divisor}:")

# Looping through each number between num1 and num2 (inclusive)
for num in range(num1, num2 + 1):
    # Checking if the current number is divisible by the divisor
    if num % divisor == 0:
    # Printing the number if it is divisible
     print(num)