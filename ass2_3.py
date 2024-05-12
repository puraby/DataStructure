# Prompting the user to input some characters
characters = input("Enter some characters: ")
# Prompting the user to input the start position
start_position = int(input("Enter the start position: "))

# Prompting the user to input the number of characters they want
num_characters = int(input("Enter the number of characters you want: "))
# Calculating the end position, ensuring it doesn't exceed the length of the input characters
end_position = min(start_position + num_characters, len(characters))
# Printing a message to indicate the format of displaying characters
print("Display the characters that are connected by \"->\":")
# Joining the characters from the start position to the end position with "->" in between
print("->".join(characters[start_position:end_position]))