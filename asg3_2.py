# Player 1 inputs a number
player1_number = int(input("Enter an integer by player 1: "))
print("Let player 2 input another integer and guess the integer by player 1")

# Player 2 starts guessing
while True:
    player2_guess = int(input("Enter an integer by player 2: "))

    # Check if the guess is correct
    if player2_guess == player1_number:
        print("Correct! Finish the guess.")
        break
    # Provide hints to guide Player 2
    elif player2_guess < player1_number:
        print("Try a larger number and guess again.")
    else:
        print("Try a smaller number and guess again.")
