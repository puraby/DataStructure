
money = int(input("Enter how much money (Integer) you have: "))

# The costs of red and green balls
red_ball_cost = 3
green_ball_cost = 5

# A flag to indicate if at least one combination has been found
combination_found = False

max_green_balls = money // green_ball_cost

# Loop through all possible combinations of green balls
for green_balls in range(max_green_balls, -1, -1):
    # Calculate the remaining money after buying green balls
    money_left = money - (green_balls * green_ball_cost)
    # Calculate how many red balls can be bought with the remaining money
    red_balls = money_left // red_ball_cost
    # Calculate the remaining money after buying red balls
    money_left -= (red_balls * red_ball_cost)

    # If no more balls can be bought with the leftover money, print the combination
    if money_left < red_ball_cost:
        print(f"You can buy {red_balls} red ball(s) and {green_balls} green ball(s)")
        combination_found = True

# If no combination is found that spends all money, print that no balls can be bought
if not combination_found:
    print("You can buy 0 red ball(s) and 0 green ball(s)")


