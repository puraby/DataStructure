def main():
    # Input the number of dogs, horses, and birds
    num_dogs = int(input("Enter the number of dog(s): "))
    num_horses = int(input("Enter the number of horse(s): "))
    num_birds = int(input("Enter the number of bird(s): "))

    # Calculate total number of legs
    total_dog_legs = num_dogs * 4
    total_horse_legs = num_horses * 4
    total_bird_legs = num_birds * 2
    total_legs = total_dog_legs + total_horse_legs + total_bird_legs

    # Output the results
    print(f"There are {num_dogs} dog(s), {num_horses} horse(s) and {num_birds} bird(s)")
    print(f"The total number of dog legs is: {num_dogs} x 4 = {total_dog_legs}")
    print(f"The total number of horse legs is: {num_horses} x 4 = {total_horse_legs}")
    print(f"The total number of bird legs is: {num_birds} x 2 = {total_bird_legs}")
    print(f"The total number of legs is: {total_dog_legs} + {total_horse_legs} + {total_bird_legs} = {total_legs}")

if __name__ == "__main__":
    main()
