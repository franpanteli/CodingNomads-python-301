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
    -> output: Let's take 3 of carrot and 12 of pea.
    -> the issues with this classless approach 
        -> it leaves out the plurals 
        -> THE MAIN ISSUE WITH THIS IS THAT YOU CAN'T USE ATTRIBUTES EASILY 
            -> e.g, accessing the amount of a certain ingredient you want
            -> dictionaries aren't the best data structures for storing this information, classes are
            -> we can define our own classes for this 
    -> summary: why use a Python class 
        -> planning the ingredient class
        -> we can't store many attirbutes in a list (although we can in a list of tuples)
            -> attirbutes we want to store include ingredients, and the amount of each 
        -> ATTRIBUTES CAN BE STORED IN A DICTIONARY, BUT ACCESSING THEM IS HARDER THIS WAY (HARDER THAN IT NEEDS TO BE
            FOR THIS CONTEXT)
"""