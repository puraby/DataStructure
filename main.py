product_code = "377B"
product_name = "Beef Liquid Stock"
product_size = "250mL"

print(product_code + ": " + product_name + ", " + product_size)
product_price = 2.15

print(product_name + ", " + product_size + ", $" + str(product_price))
print("{}: {}, {}".format(product_code, product_name, product_size))
print("{}, {}, ${:.2f}".format(product_name, product_size, product_price))

# Initialize variables
numbers = []
even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0

# Input loop
while True:
    user_input = input("Enter an integer or q to quit: ")

    if user_input.lower() == 'q':
        break

    num = int(user_input)
    numbers.append(num)

    # Update counts
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

# Calculate summary information
total_numbers = len(numbers)
sum_numbers = sum(numbers)

# Display summary information
print("\nSummary information:")
print(f"You have entered {total_numbers} integers.")
print(f"The sum of these numbers is {sum_numbers}.")
print(f"There are {even_count} even numbers.")
print(f"There are {odd_count} odd numbers.")
print(f"There are {positive_count} positive numbers.")
print(f"There are {negative_count} negative numbers.")













