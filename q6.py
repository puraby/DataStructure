def main():
    # Input user information
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    birthplace = input("Enter your birthplace: ")
    gender = input("Enter your gender: ")
    degree = input("Enter your degree: ")

    # Output user information
    print(f"\nHi {name}!")
    print("Here is your information:")
    print("name*****age*****birthplace*****gender*****degree")
    print(f"{name}*****{age}*****{birthplace}*****{gender}*****{degree}")

if __name__ == "__main__":
    main()
