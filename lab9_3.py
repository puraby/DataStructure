class Staff:
    def __init__(self, staff_number, first_name, last_name, email):
        self.staff_number = staff_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def print_details(self, width):
        print('-' * width)
        print("| Staff number: {:<{}}|".format(self.staff_number, width - 17))
        print("| {} {:<{}}|".format(self.first_name, self.last_name, width - len(self.first_name) - 3))
        print("| {:<{}}|".format(self.email, width - 3))

        print('-' * width)

# Example usage
staffObj = Staff("012345", "John", "Smith", "js@gmail.com")
staffObj.print_details(40)
