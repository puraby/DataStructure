

basic_fee = 10
def calculate_postage(weight):
   # Basic fee for weights up to 1000 grams
    overweight_fee_per_500g = 4  # Additional fee for each 500 grams over 1000 grams

    if weight <= 1000:
        # If weight is no larger than 1000 grams, only basic fee is charged
        total_fee = basic_fee
        additional_overweight = 0
        overweight_fee = 0
    else:
        # Calculate additional overweight and overweight fee
        additional_overweight = weight - 1000
        overweight_fee = ((additional_overweight - 1) // 500 + 1) * overweight_fee_per_500g
        # Calculate total fee
        total_fee = basic_fee + overweight_fee

    return total_fee, additional_overweight, overweight_fee

def main():
    weight = int(input("Enter an integer weight in grams: "))

    total_fee, additional_overweight, overweight_fee = calculate_postage(weight)

    print(f"The additional overweight is {additional_overweight} grams")
    print(f"The additional overweight fee is ${overweight_fee}")
    print("The total postage fee is calculated by adding")
    print("the basic fee and the additional overweight fee:")
    print(f"${basic_fee} + ${overweight_fee} = ${total_fee}")

if __name__ == "__main__":
    main()