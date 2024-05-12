# Function to convert the sentence to the specified case
def convert_case(sentence, case):
    if case == "U":
        # Convert sentence to uppercase
        return sentence.upper()
    elif case == "L":
        # Convert sentence to lowercase
        return sentence.lower()
    else:
        return None

def main():
    while True:
        # Continuously prompt the user for input until they choose to quit
        sentence = input("Enter a sentence (or use q to quit): ")
        if sentence.lower() == "q":
            # If user enters 'q', exit the program
            print("The user has aborted the program.")
            break
        case = input("Uppercase or Lowercase? (U/L): ").upper()
        # If conversion was successful
        result = convert_case(sentence, case)

        # Print the converted sentence along with the original sentence and case
        print(f"The {['Uppercase', 'Lowercase'][case == 'L']} of {sentence} is {result}.")


if __name__ == "__main__":
    main()