def find_chick_rabbit(leg):
    print("Print the number of chick(s) and rabbit(s):")
    if leg % 2 != 0:
        print("Your input is invalid.")
        return


    # Iterate over possible numbers of chickens
    # Maximum possible chickens would be legs//2 if all were chickens
    for chicks in range(0, leg// 2 + 1):
        # The remaining legs after accounting for the chickens must be divisible by 4 to form rabbits
        remaining_legs = leg - chicks * 2
        if remaining_legs % 4 == 0:
            rabbits = remaining_legs // 4
            print(f"Chick: {chicks}, Rabbit: {rabbits}")
            found = True


# Example usage:
find_chick_rabbit(18)
find_chick_rabbit(11)
