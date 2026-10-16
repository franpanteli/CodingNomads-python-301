# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet:
    def __init__(self, name, radius, mass, distance_from_sun):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance_from_sun = distance_from_sun

    def orbit(self):
        return f"{self.name} is orbiting the Sun."

    def __str__(self):
        return (
            f"Planet: {self.name}, "
            f"Radius: {self.radius} km, "
            f"Mass: {self.mass} kg, "
            f"Distance from Sun: {self.distance_from_sun} million km"
        )


# Create planet objects
earth = Planet("Earth", 6371, 5.972e24, 149.6)
mars = Planet("Mars", 3389.5, 6.417e23, 227.9)
jupiter = Planet("Jupiter", 69911, 1.898e27, 778.6)

# Print planet information
print(earth)
print(mars)
print(jupiter)

# Call a method
print(earth.orbit())