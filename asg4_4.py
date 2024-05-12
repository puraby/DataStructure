class Student:
    def __init__(self, student_id, name, gender, age):
        # Initialize the Student object with the given id, name, gender, and age
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.age = age

    def printStudentInfo(self):
        # Using the format() method for string formatting
        print("Student Information:")
        print("Id: {}".format(self.student_id))
        print("Name: {}".format(self.name))
        print("Gender: {}".format(self.gender))
        print("Age: {}".format(self.age))

# Example usage of the class
student_obj1 = Student(1, "James", "Male", 18)
student_obj2 = Student(2, "Emily", "Female", 17)
student_obj3 = Student(3, "Amy", "Female", 21)
student_obj4 = Student(4, "Sam", "Male", 20)

# Printing student information using the printStudentInfo method
student_obj1.printStudentInfo()
student_obj2.printStudentInfo()
student_obj3.printStudentInfo()
student_obj4.printStudentInfo()

