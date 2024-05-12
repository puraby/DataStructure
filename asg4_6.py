class Subject:
    def __init__(self, code, building, capacity):
        # Initialize the Subject object with code, building, and capacity attributes
        self.code = code
        self.building = building
        self.capacity = capacity

    def __str__(self):
        # Define the string representation of the Subject object
        return 'Subject[code="{code}", building="{building}", capacity={capacity}]'.format(
            code=self.code, building=self.building, capacity=self.capacity)

# Example usage of the class
subject1 = Subject("csit110", "B40", 500)
subject2 = Subject("csit881", "B20", 300)

# Printing instances of the Subject class
print(subject1)  # Expected output: Subject[code="csit110", building="B40", capacity=500]
print(subject2)  # Expected output: Subject[code="csit881", building="B20", capacity=300]
