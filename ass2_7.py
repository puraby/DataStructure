# Prompting the user to enter an odd positive integer
num = int(input("Enter an odd positive integer: "))
# Calculating half size of the diamond
half_size = num // 2 + 1
print("The diamond pattern is:")
# Upper part of the diamond
for i in range(1, half_size + 1):
    # Calculating the number of spaces for each row
    spaces = " " * (half_size - i)
    # Calculating the number of stars for each row
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Lower part of the diamond
for i in range(half_size - 1, 0, -1):
    # Calculating the number of spaces for each row
    spaces = " " * (half_size - i)
    # Calculating the number of stars for each row
    stars = "*" * (2 * i - 1)
    print(spaces + stars)