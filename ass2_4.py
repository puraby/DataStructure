# Prompting the user to input the number of rows for the matrix
rows = int(input("Enter the number of rows: "))
# Prompting the user to input the number of columns for the matrix
cols = int(input("Enter the number of columns: "))
# Printing a message to indicate the dimensions of the matrix
print(f"Display the following matrix with {rows} rows and {cols} columns:")
# Iterating through each row of the matrix
for i in range(1, rows + 1):
    # Generating values for the current row using list comprehension
    # Each value in the row is the product of the row number (i) and column numbers (from 1 to cols)
    row_values = [i * j for j in range(1, cols + 1)]
    # Joining the row values into a string separated by spaces and printing the row
    print(" ".join(map(str, row_values)))
