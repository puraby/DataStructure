# Prompting the user to input the current height of the tree
old_height = float(input("Enter the current tree height: "))

# Prompting the user to input the growth rate of the tree per year
growth_rate = float(input("Enter the tree growth speed every year: "))

# Prompting the user to input the number of years for which they want to calculate the height
years = int(input("Enter how many year(s) (Integer): "))

# Loop through each year to calculate the tree's height
for year in range(1, years + 1):
    # Calculating the new height of the tree after each year
    new_height = old_height + (old_height * growth_rate)

    # Printing the result for each year
    print(f"After {year} year(s), the tree height will be: {old_height} x (1 + {growth_rate}) = {new_height}")

    # Updating the old height for the next iteration
    old_height = new_height

