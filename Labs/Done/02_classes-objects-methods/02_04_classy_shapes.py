# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

import math


# --- Rectangle Class ---
class Rectangle:

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    """Calculates the area of the rectangle."""
    return self.length * self.width

  def perimeter(self):
    """Calculates the perimeter of the rectangle."""
    return 2 * (self.length + self.width)


# --- Circle Class ---
class Circle:

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    """Calculates the area of the circle using pi * r^2."""
    return math.pi * (self.radius**2)

  def circumference(self):
    """Calculates the circumference of the circle using 2 * pi * r."""
    return 2 * math.pi * self.radius


# ==========================================
# TESTING THE CLASSES
# ==========================================

if __name__ == "__main__":
  # Create a Rectangle instance
  my_rect = Rectangle(length=10, width=5)
  print(f"Rectangle (Length: {my_rect.length}, Width: {my_rect.width})")
  print(f"  - Area: {my_rect.area()}")
  print(f"  - Perimeter: {my_rect.perimeter()}\n")

  # Create a Circle instance
  my_circle = Circle(radius=7)
  print(f"Circle (Radius: {my_circle.radius})")
  print(f"  - Area: {my_circle.area():.2f}")
  print(f"  - Circumference: {my_circle.circumference():.2f}")