def main():
    no1 = int(input("Enter the 1st integer: "))
    no2 = int(input("Enter the 2nd integer: "))
    if(no2 > no1):
        print(f"{no1} is smaller than {no2}")
        difference = no2 - no1
    else:
        print(f"{no1} is no smaller than {no2}")
        difference = no1 - no2

    print (f"The difference between {no1} and {no2} is: {difference}")


if __name__ == "__main__":
    main()

