def main():
    product_code = "377B"
    product_name = "Beef Liquid Stock"
    product_size = "250mL"
    product_price = 2.15
    print(f"{product_code}: {product_name}, {product_size}")
    print(product_name + ", " + product_size + ", $" + str(product_price))
    print("{}: {}, {}".format(product_code, product_name, product_size))
    print("{}, {}, ${:.2f}".format(product_name, product_size, product_price))




if __name__ == "__main__":
    main()