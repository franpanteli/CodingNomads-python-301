""" Why Use a Python Class Video Notes 
    -> outline
        -> benefits of Python classes
        -> creating our own Python classes
    -> OOP in Python   
        -> a way to do programming that Python supports
        -> WE CAN BUILD OUR OWN OBJECTS
        -> EVERYTHING IN PYTHON IS AN OBJECT
    -> why we need a custom object
        -> you can astore elemtns in a dictionary 
            -> ingredients and the number of them 
            -> we can also access them 
            -> we then get an output from this 
            -> we can combine different ingredeients that the list stores 
            -> adding the quantities of different ingredients 
            -> writing ingredient dict and the name of the element in the dictionary 
                -> we can also get something else, for example the Latin name of the ingredient we are extracting 
                -> we want to keep more information there 
                -> this is when the dictionary can grow in size, a lot 
    -> you can create your own objects and datatpes 
        -> you can then print the types of these
        -> CREATING OUR OWN OBJECTS
            -> STRUCTURING THE DATA INSIDE THE OBJECTS <- next 
"""

ingredient_dict = {"carrots": 3, "potatoes": 2, "peas": 20, "tomatoes": 2}

ingredient_dict["carrots"]

ingredient_dict["carrots"] + ingredient_dict["potatoes"]

print(ingredient_dict)

type(3)

#{'carrots': 3, 'potatoes': 2, 'peas': 20, 'tomatoes': 2}