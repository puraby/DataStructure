product_code = "377B"
product_name = "Beef Liquid Stock"
product_size = "250mL"
product_price = 2.15

print(product_code + ": " + product_name + ", " + product_size)


print(product_name + ", " + product_size + ", $" + str(product_price))
print("{}: {}, {}".format(product_code, product_name, product_size))
print("{}, {}, ${:.2f}".format(product_name, product_size, product_price))



def main():
    # Cost of each animal
    cow_cost = 30
    duck_cost = 5
    chick_cost = 3

    # Input number of animals to purchase
    num_cows = int(input("Enter number of cows to purchase: "))
    num_ducks = int(input("Enter number of ducks to purchase: "))
    num_chicks = int(input("Enter number of chickens to purchase: "))

    # Calculate total cost
    total_cost = (num_cows * cow_cost) + (num_ducks * duck_cost) + (num_chicks * chick_cost)

    # Display cost breakdown and total
    print("Cost:")
    print(f"{num_cows} cow = {num_cows * cow_cost} grassies")
    print(f"{num_ducks} duck = {num_ducks * duck_cost} grassies")
    print(f"{num_chicks} chick = {num_chicks * chick_cost} grassies")
    print(f"Total = {total_cost} grassies")


if __name__ == "__main__":
    main()
def main():
    print("{:>10} {:^30} {:<10}".format("Faces", "Name", "Vertices"))
    print("{:>10} {:^30} {:<10}".format("----", "----", "--------"))
    print("{:>10} {:^30} {:<10}".format("4", "Tetrahedron", "4"))
    print("{:>10} {:^30} {:<10}".format("6", "Cube", "8"))
    print("{:>10} {:^30} {:<10}".format("8", "Octahedron", "6"))
    print("{:>10} {:^30} {:<10}".format("12", "Dodecahedron", "20"))
    print("{:>10} {:^30} {:<10}".format("20", "Icosahedron", "12"))

if __name__ == "__main__":
    main()


def main():
    print("{:>10} {:^30} {:<10}".format("Faces", "Name", "Vertices"))
    print("{:>10} {:^30} {:<10}".format("----", "----", "--------"))
    print("{:>10} {:^30} {:<10}".format("4", "Tetrahedron", "4"))
    print("{:>10} {:^30} {:<10}".format("6", "Cube", "8"))
    print("{:>10} {:^30} {:<10}".format("8", "Octahedron", "6"))
    print("{:>10} {:^30} {:<10}".format("12", "Dodecahedron", "20"))
    print("{:>10} {:^30} {:<10}".format("20", "Icosahedron", "12"))

if __name__ == "__main__":
    main()
