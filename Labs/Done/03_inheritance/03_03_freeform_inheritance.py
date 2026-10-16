# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.


# CLASSES AND INHERITANCE
# =======================

# 1. Create the parent class: Vehicle

class Vehicle:
    """Models a general vehicle."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        """Starts the vehicle."""
        print(f"The {self.brand} {self.model} is starting.")

    def stop(self):
        """Stops the vehicle."""
        print(f"The {self.brand} {self.model} has stopped.")

    def display_info(self):
        """Displays vehicle information."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


# 2. Create the first child class: Truck

class Truck(Vehicle):
    """Models a truck."""

    def __init__(self, brand, model, year, cargo_capacity):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self):
        """Loads cargo into the truck."""
        print(
            f"The truck can carry "
            f"{self.cargo_capacity} kg of cargo."
        )

    def display_info(self):
        """Overrides the parent's display_info method."""
        super().display_info()
        print(f"Cargo capacity: {self.cargo_capacity} kg")


# 3. Create the second child class: Motorcycle

class Motorcycle(Vehicle):
    """Models a motorcycle."""

    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def rev_engine(self):
        """Revves the motorcycle engine."""
        print(f"The engine revs at {self.engine_cc} cc.")

    def display_info(self):
        """Overrides the parent's display_info method."""
        super().display_info()
        print(f"Engine size: {self.engine_cc} cc")


# 4. Create a child of Motorcycle: ElectricMotorcycle
# This gives us three levels of inheritance:
# Vehicle -> Motorcycle -> ElectricMotorcycle

class ElectricMotorcycle(Motorcycle):
    """Models an electric motorcycle."""

    def __init__(
        self, brand, model, year, engine_cc, battery_range
    ):
        super().__init__(brand, model, year, engine_cc)
        self.battery_range = battery_range

    def charge(self):
        """Charges the electric motorcycle."""
        print(f"The motorcycle is charging.")

    def display_info(self):
        """Overrides Motorcycle's display_info method."""
        super().display_info()
        print(f"Battery range: {self.battery_range} km")


# 5. Create objects to test the classes

truck1 = Truck("Volvo", "FH16", 2024, 25000)

motorcycle1 = Motorcycle("Honda", "CB500F", 2023, 500)

electric_motorcycle1 = ElectricMotorcycle(
    "Zero", "SR/F", 2025, 0, 250
)


# 6. Test the Truck class

print("=== TRUCK ===")
print(truck1)
truck1.display_info()
truck1.start()
truck1.load_cargo()
truck1.stop()

print()


# 7. Test the Motorcycle class

print("=== MOTORCYCLE ===")
print(motorcycle1)
motorcycle1.display_info()
motorcycle1.start()
motorcycle1.rev_engine()
motorcycle1.stop()

print()


# 8. Test the ElectricMotorcycle class

print("=== ELECTRIC MOTORCYCLE ===")
print(electric_motorcycle1)
electric_motorcycle1.display_info()
electric_motorcycle1.start()
electric_motorcycle1.charge()
electric_motorcycle1.stop()
