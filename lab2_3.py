def main():
    cow = int(input("Enter number of cows to purchase: "))
    duck = int(input("Enter number of ducks to purchase: "))
    chicken = int(input("Enter number of chicken to purchase: "))

    print("Cost:")
    print(f"{cow} cow = {cow * 30} grassies")
    print(f"{duck} duck = {duck * 5} grassies")
    print(f"{chicken} chick = {chicken * 3} grassies")

    cost = (cow * 30) + (duck * 5) + (chicken * 3)
    print(f"Total = {cost} grassies")


if __name__ == "__main__":
    main()