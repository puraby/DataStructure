even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0
total_num = 0
sum = 0

while True:
    num = input("Enter an integer or q to quit: ")

    if num.lower() == 'q':
        break

    total_num = total_num + 1
    sum = sum + int(num)

    if int(num) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if int(num) > 0:
        positive_count += 1
    elif int(num) < 0:
        negative_count += 1



print("\nSummary information:")
print("You have entered {0} integers.".format(total_num))
print("The sum of these numbers is {0}.".format(sum))
print("There are {0} even numbers.".format(even_count))
print("There are {0} odd numbers.".format(odd_count))
print("There are {0} positive numbers.".format(positive_count))
print("There are {0} negative numbers.".format(negative_count))






