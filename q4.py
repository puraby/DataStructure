def main():
    try:
        # Input two positive integers
        num1 = int(input("Enter 1st positive integer: "))
        num2 = int(input("Enter 2nd positive integer: "))

        if num2 == 0:
            return

        # Perform modulo operation
        modulo_result = num1 % num2
        print(f"Math operations:")
        print(f"Modulo: {num1} % {num2} = {modulo_result}")
        if modulo_result % 2 == 0:
                print(f"Is the Modulo result {modulo_result} an even number (Y/N)? Y")
        else:
            print(f"Is the Modulo result {modulo_result} an even number (Y/N)? N")

        # Perform floor division
        floor_division_result = num1 // num2
        print(f"Floor division: {num1} // {num2} = {floor_division_result}")
        if floor_division_result % 2 == 0:
            print(f"Is the Floor division result {floor_division_result} an even number (Y/N)? Y")
        else:
            print(f"Is the Floor division result {floor_division_result} an even number (Y/N)? N")

    except ValueError:
        pass
    except EOFError:
        pass  # Do nothing if EOFError occurs
    except Exception as e:
        pass

if __name__ == "__main__":
    main()