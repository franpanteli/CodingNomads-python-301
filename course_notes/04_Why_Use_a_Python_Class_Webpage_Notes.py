""" Why Use a Python Class Webpage Notes 
    -> outline
        -> introduction
        -> cooking with Python
            -> without a class
        -> summary: why use a Python class
    -> introduction
        -> previous <- OOP high-level theoretical view
        -> creating classes
    -> cooking with Python
        -> building an Ingredient class
        -> building soup from this class
        -> cooking ingredients
        -> without a class
            -> storing the ingredients in a list
"""

ingredients = ["carrot", "pea", "squash"]

"""
    -> this is for only storing names of the ingredients 
        -> we need methods
    -> we also need more information, like the amount of each ingredient 
        -> we can use a dictionary to do this
        -> mapping the name of each ingredient to a list / other dictionary that contains more information about the 
            food item  
"""

ingredients = {
                'carrots': {'name': 'carrot', 'amount': 3},
                'peas': {'name': 'pea', 'amount': 12}
              }

"""
    -> this dictionary contains the names and the amount of each ingredient type 
    -> we can then use this information to write a recipie 
"""

print(f"Let's take {ingredients['carrots']['amount']} of {ingredients['carrots']['name']} and {ingredients['peas']['amount']} of {ingredients['peas']['name']}.")

"""
    -> 
"""