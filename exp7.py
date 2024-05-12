print("Welcome to Ocean World.")
under_6 = input("How many tickets for children under 6?")
under_6_17 = input("How many tickets for children age between 6-17?")
adult = input("How many tickets for adults?")
print("Receipt:")
total = int(under_6) + int(under_6_17) + int(adult)
print("Number of tickets:" + str(total))
cost_6_17 = int(under_6_17)*7
cost_adult = int(adult)*20

total_cost = cost_6_17 + cost_adult
print("Total cost $" +str(total_cost))