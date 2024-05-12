def format_dob(dob):
    parts = dob.split('-')
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return f"{parts[0]}/{months[int(parts[1]) - 1]}/{parts[2]}"

def main():
    student_number = input("Enter your student number: ")
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    dob = input("Enter your dob (DD-MM-YYYY): ")

    formatted_dob = format_dob(dob)

    xml_output = f'''<?xml version="1.0"?>
<student Id="{student_number}">
  <name>{name}</name>
  <department>{department}</department>
  <dob>{formatted_dob}</dob>
</student>'''

    print(f"\nHi {name}!\n{xml_output}")

if __name__ == "__main__":
    main()



class Staff:
    def __init__(self, staff_number, first_name, last_name, email):
        self.staff_number = staff_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def print_details(self, width):
        # Print the top border of the box
        print('-' * width)
        # Print the staff number line with padding
        print(f"| Staff number: {self.staff_number}".ljust(width - 1) + '|')
        # Print the full name with padding
        print(f"| {self.first_name} {self.last_name}".ljust(width - 1) + '|')
        # Print the email with padding
        print(f"| {self.email}".ljust(width - 1) + '|')
        # Print the bottom border of the box
        print('-' * width)

# Example usage
staffObj = Staff("012345", "John", "Smith", "js@gmail.com")
staffObj.print_details(40)
