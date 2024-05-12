def calculate_cost(num_of_item):
    if num_of_item <= 50:
        cost = num_of_item * 3 + 10
    else:
        cost = num_of_item * 2
    return cost

def generate_recipt(num_of_item, cost):
    print("Receipt:")
    if num_of_item <= 50:
        print(f"{num_of_item} items x $3 = ${num_of_item * 3}")
        print("Postage: $10")

    else:
        print(f"{num_of_item} items x $2 = ${num_of_item * 2}")
        print("Postage: $0")

    print(f"Total: ${cost}")

def main():
    num_items = int(input("Enter the number of items: "))
    print()
    cost = calculate_cost(num_items)

    generate_recipt(num_items,cost)

if __name__ == "__main__":
    main()


