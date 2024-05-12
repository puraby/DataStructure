
num_items = int(input("Enter the number of items: "))
shipping_method = input("Enter shipping method (s/r/e): ")
print()
print("Receipt:")

if(num_items<=50):
    print(f"{num_items} items x $3 = ${num_items * 3}")
    if shipping_method == 'r':
            print(f"Registered post: $15")
            print(f"Total: ${num_items * 3 + 15}")
    elif shipping_method == 's':
            print(f"Standard post: $10")
            print(f"Total: ${num_items * 3 + 10}")
    elif shipping_method == 'e':
            print(f"Express post: $20")
            print(f"Total: ${num_items * 3 + 20}")


else:
    print(f"{num_items} items x $2 = ${num_items * 2}")
    if shipping_method == 'r':
        print(f"Registered post: $10")
        print(f"Total: ${num_items * 2 + 10}")
    elif shipping_method == 's':
        print(f"Standard post: $0")
        print(f"Total: ${num_items * 2 + 0}")
    elif shipping_method == 'e':
        print(f"Express post: $17")
        print(f"Total: ${num_items * 2 + 17}")






