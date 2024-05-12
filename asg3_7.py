# Gather input numbers from the user until "quit" is entered
input_numbers = []
while True:
    user_input = input("Enter an integer (or enter quit): ")
    if user_input.lower() == 'quit':
        break
    else:
        try:
            number = int(user_input)
            input_numbers.append(number)
        except ValueError:
            print("That's not an integer. Please try again!")

# Selection sort algorithm (modified to sort from largest to smallest)
print("Selection Sort Algorithm for {}".format(input_numbers))
for i in range(len(input_numbers)-1):
    # Find the maximum element in remaining unsorted array
    max_idx = i
    for j in range(i + 1, len(input_numbers)):
        if input_numbers[j] > input_numbers[max_idx]:
            max_idx = j

    # Swap the found maximum element with the first element
    input_numbers[i], input_numbers[max_idx] = input_numbers[max_idx], input_numbers[i]

    # Print the progress after each round
    print("After round {}: {}".format(i, input_numbers))
