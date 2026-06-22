""" Initializing Attributes Video Notes 
    -> outline 
        -> after learning about the __init()__ method, we are taking arguments and the lesson shows us how
    -> adding more elements to the Ingredients class
        -> adding attributes to Ingredients
        -> the __init__(): method 
            -> THIS IS A DUNDER METHOD, FOR INITIALISING A NEW OBJECT
            -> every new class inherits from it and it doesn't do anything 
            -> the arguments of this
                -> name <- the name of the ingredient 
                -> amount <- the amount of the object 
                -> self <- THE INSTANCE OF THE OBJECT WE ARE CREATING 
                    -> the eng instance we are creating 
                    -> it assigns the arguments we put into the class for the objects inside it 
        -> in the ingrefients class
            -> he imports ingredients
            -> then sets ing = to Ingredient()
            -> then he looks at the method defined in the class
                -> there is an error in the console, that he fixes
                -> this gives an object like a dictionary 
                -> it has a certain value and a name of the string 
                    -> three carrots
        -> we can then call ingredient.amount 
        -> ingredient.name gives us the name of the object we just made
            -> the name of an imagined ingredient object
            -> to look inside of the object we just made
            -> ingredient.attribute 
        -> we can create different instances of the same type of object
        -> the class is a blueprint description of what the object should look like 
        -> he sets a new ingredient 
            -> peas
            -> peas.amount = 3, for example 
            -> the amount of peas we need
            -> or, grammage
        -> he defines another new ingredient 
            -> tomatoes
            -> then the emount for them 
            -> tom.name 
            -> tom.amount 
            -> for tomatoes
        -> this shows the amount of different ingredient objects we have on the RHS of the console
"""

# CLASSES AND OBJECT-ORIENTED PROGRAMMING

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        
import sys

# Print Python version and platform correctly
print("Python %s on %s" % (sys.version, sys.platform))

# Add a folder to sys.path
sys.path.extend(['/Users/nartin/Documents/codingnomads/cooking_python'])

# Import the Ingredient class
from ingredients import Ingredient

# Create Ingredient instances
ing = Ingredient("carrots", 3)
print(ing.name)    # Output: carrots
print(ing.amount)  # Output: 3

peas = Ingredient("peas", 20)
print(peas.name)    # Output: peas
print(peas.amount)  # Output: 20

tom = Ingredient("tomatoes", 2)
print(tom.name)    # Output: tomatoes
print(tom.amount)  # Output: 2