# Prompting the user to input a sentence
sentence = input("Enter a sentence: ")

# Prompting the user to input a character to remove from the sentence
char = input("Enter a character: ")
# Removing all occurrences of the specified character from the sentence
result = sentence.replace(char, "")
# Printing a message to indicate the operation being performed
print(f"After removing all the \"{char}\" characters from the sentence \"{sentence}\",")

# Printing the resulting sentence after removal of the specified character
print("the current sentence is:")
print(result)

