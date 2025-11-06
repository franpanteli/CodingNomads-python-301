""" Python Classes, Objects and Instance Variables Webpage Notes 
    -> outline 
        -> introduction 
        -> define an empty class
            -> tasks 
        -> the constructor method 
        -> summary: Python classes, objecta and instance variables 
    -> the ingredients class
"""

class Ingredient:
    """Creates an empty Ingredient object."""
    pass

i = Ingredient()

i.name = "carrot"
print(i.name)  # OUTPUT: carrot

"""
    -> this creates an empty ingredient object
    -> creating an empty instance of the class
    -> it beig empty
    -> then assigning a value to the variable in the instance
"""

print(name) #creates a variable in the namespace object

"""
    -> we can define within the local project scope
    -> we want to use the class as a variable that defines the different methods
    -> __init()__ <- THIS DUNDER IS CALLED WHEN WE ARE CREATING A NEW INSTANCE
        -> for initialising 
"""

c = Ingredient() 
#an init method:
print(c.name)  # OUTPUT: carrot 

"""
    -> methods are functions that belong to an object
    -> we can explore this method
    -> using the dunder method
    -> we can reuse this class, once defined
    -> we don't need to use the instance namespace once defined
    -> it is suggesting we create more instances
    -> summary 
        -> adapting the dunder init method to take arguments
        -> __init__() NOT __init()__
        -> the __init__() method is called when initialising a new object
        -> WE CAN CREATE CUSTOM DUNDER INIT METHODS
        -> custom init methods can contain custom instance variables 
"""