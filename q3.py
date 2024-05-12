def main():
    # Input subject details
    code = input("Enter subject code: ")
    title = input("Enter subject title: ")
    cp = int(input("Number of credit points: "))
    cost_per_cp = int(input("Cost per credit point: "))
    is_core = input("Is this a core subject (Y/N)? ").upper()

    # Calculate total fee
    total_fee = cp * cost_per_cp

    # Output result
    print("\nHere is the JSON output")
    print("{")
    print(f'  "code": "{code}",')
    print(f'  "title": "{title}",')
    print(f'  "core": "{is_core}",')
    print(f'  "cp": {cp},')
    print(f'  "fee": {total_fee}')
    print("}")

if __name__ == "__main__":
    main()
