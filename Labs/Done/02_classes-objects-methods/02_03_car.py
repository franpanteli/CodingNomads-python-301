# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.


class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_speed(self):
        self.max_speed += 5

    def print_details(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Maximum speed: {self.max_speed} km/h")


# Create two car objects
car1 = Car("Toyota Corolla", 2022, 180)
car2 = Car("Tesla Model 3", 2024, 250)

# Print the original details
print("Car 1:")
car1.print_details()

print("\nCar 2:")
car2.print_details()

# Increase the speed of each car
car1.increase_speed()
car2.increase_speed()

# Change the objects' attributes
car1.model = "Toyota Camry"
car2.year = 2025

# Print the updated details
print("\nUpdated Car 1:")
car1.print_details()

print("\nUpdated Car 2:")
car2.print_details()
