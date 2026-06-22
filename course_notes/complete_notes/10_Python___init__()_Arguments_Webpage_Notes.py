""" Python __init__() Arguments Webpage Notes 
    -> outline
        -> introduction
        -> pass arguments to __init__()
            -> method body
        -> type error
        -> why use arguments
            -> tasks
        -> summary: __init__() arguments
    -> __init__()
        -> this behaves like other functions
        -> it can take and pass arguments
        -> class IS A CONSTRUCTOR
        -> THIS IS A DUNDER METHOD
    -> making other methods
    -> WE ARE USING name AS ANOTHER PARAMETER
        -> name is being assigned to a new instance of the variable
            -> instantiation
"""

class Ingredient:
    """Models a food item used as an ingredient."""

    def __init__(self, name):
        self.name = name

"""
    -> we need to pass an argument to name 
    -> the name belongs to this one object
        -> THE NAME ATTRIBUTE CAN BE ACCESSED USING THE .name METHOD
            -> THIS IS NOT A FUNCTION, BECAUSE IT HAS NO BRACKETS 
"""

i = Ingredient("peas")
print(i.name)  # OUTPUT: peas

"""
    -> type error 
        -> instantiating a new object without a method, when the __init__() method says we need one 
            -> this is missing a positional argument 
                -> it literally means an argument is missing 
                -> WE NEED TO INCLUDE ALL ARGUEMENTS, OR WE GET A POSITIONAL ARGUEMENT ERRROR
                    -> THIS IS ASSOCIATED WITH THE DUNDER __init__() method 
"""

j = Ingredient()
# OUTPUT: TypeError: __init__() missing 1 required positional argument: 'name'

"""
    -> why use arguments 
        -> arguments are for building functions 
            -> they make classes more useful 
        -> we can create any ingredient that we can name 
        -> WE USE ARGUMENTS FOR FUNCTIONS, AS WELL AS FOR CLASSES
            -> for example, being able to create different types of ingredients 
            -> methods can take more than one argument 
            -> THE DIFFERENCE BETWEEN A METHOD AND A FUNCTION IS THAT A METHOD IS LIKE A FUNCTION, BUT FOR CLASSES
                -> THE METHOD IS SPECIFIC TO THE CLASS, AND NOT SOMETHING THAT ANY VARIABLE IN THE CODE CAN JUST USE  
"""

#we are defining four different ingredients
c = Ingredient("cauliflower")
b = Ingredient("broccoli")
d = Ingredient("dandelion")

#printing the names of those ojbects
print(c.name, b.name, d.name) #THESE ARE NAME ATTRIBUTES (METHODS)
# OUTPUT: cauliflower broccoli dandelion

"""
    -> task 
        -> add two different attributes we want the incredient class to have 
        -> write the code for this 
        -> add them after the name 
        -> dishes that they can be used in 
        -> expity and use by dates 
    -> summary 
        -> the __init__() can have custom parameters
        -> custom parameters must be passed o the constructor when instantiating a new object
        -> __init__() IS A DUNDER METHOD 
            -> this is called implicitly when we instantiate an object
        -> custom instance variables allow new objects to have unique variables during declaration 
    -> next <- INSTANCE METHODS 
"""
