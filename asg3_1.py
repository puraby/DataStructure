
# Input for the first integer
first_int = int(input("Enter the 1st integer: "))

# Input for the second integer
second_int = int(input("Enter the 2nd integer: "))

# Input for the number of equations to display
num_equations = int(input("Enter number of equations: "))

# Display the header for equation display
print("Equation display:")
count = 0

while count < num_equations:
  # Calculate the result of the multiplication
  result = first_int * second_int
  print("{0} * {1} = {2}".format(first_int, second_int, result))
  # Increment both integers for the next equation
  first_int += 1
  second_int += 1
  # Increment the counter
  count += 1