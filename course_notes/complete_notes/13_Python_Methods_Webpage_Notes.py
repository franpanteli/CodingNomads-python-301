""" Python Methods Webpage Notes 
    -> outline
        -> introduction 
        -> writing class methods
            -> class method example
        -> summary: Python methods 
    -> ATTRIBUTES ARE INSTANCE FUNCTIONS
        -> THE __init__() CONSTRUCTOR IS ONE OF THESE METHODS
        -> DUNDER INIT AND OTHER METHODS ARE ALSO CALLED SPECIAL METHODS / MAGIC METHODS, 
            BECAUSE THEY ARE NOT CALLED EXPLICITY 
    -> how to write class methods
        -> class method example 
            -> writing your own Python methods for class ojbects
            -> these methods giving our objects functionality
            -> THIS DEFINES AN expire() METHO TO THE Ingredient() CLASS
"""

class Ingredient:

    """Models a food item used as an ingredient."""
    def __init__(self, name):
        self.name = name

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name #add expired to the name of the ingredient  (this method example is 
            # irreversible once applied)

"""
    -> DEFININF THE Ingredient CLASS
    -> THEN DEFINING THE __init__() METHOD 
    -> THEN DEFINING OTHER METHODS FOR THE CLASS
        -> THIS IS DONE USING THE self.name VARIABLE, for the general class object 
    -> we first define the explore() method
        -> this prints a message ad adds the string "expired" in front of the instance's name 
        -> we can then create a new ingredient 
            -> the .expire method on it will change its name 
            -> we are still defininf the ingredients and the amount of them, just in a class
"""

i = Ingredient("peas")
print(i.name)  # OUTPUT: peas
i.expire()
print(i.name)  # OUTPUT: expired peas
print(i.name)  # OUTPUT: expired peas

"""
    -> we can't un-expire it once it's expired
        -> the name of the ingredient is permanently changed
        -> this reflects reality 
        -> it is a variable name, and we can reset it 
    -> WE WANT TO DEFINE WAYS THAT THE NAME OF THE (IN THIS CASE) INGREDIENT CAN CHANGE
    -> summary 
        -> classes can contain many METHODS (FUNCTIONS)
        -> class methods are avaliable to all instances of the class
            -> they are defined inside the class, with a standard syntax
            -> WHEN DEFINING A METHOD IN A CLASS, THE .self SYNTAX IS USED, TO REPRESENT AN INSTANCE OF THE CLASS OJBECT 
    -> next <- the self parameter we have been using      
""" 