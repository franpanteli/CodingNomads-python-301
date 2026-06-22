""" Class Recap + Instance Variables Video Notes 
    -> outline
        -> recapping classes and instance variables  
    -> he is in trello with different tasks 
        -> to learn 
        -> learning 
        -> learned 
    -> the basics of OOP slimmed down  
        -> CREATING A CLASS AND OJBECT, BY CALLING THE class CONSTRUCTOR 
        -> also, instance variables 
            -> name is an instance variable of Tom P's 
            -> you can't just call the name, but you can call the name attribute of an object
                -> this is an INSTANCE VARIABLE 
                    -> ingredient.name returns a different value of this
"""

# CLASSES AND OBJECT-ORIENTED PROGRAMMING
class Ingredient: #defining the Ingredient class 

    #the __init__() method 
        #THIS IS __init__(), NOT __init()__
        #it is a dunder method (__syntax__)
        #DUNDER METHODS ARE ALSO CALLED SPECIAL METHODS, OR MAGIC METHODS 
        #THEY ARE DEFINED INSIDE CLASSES (THIS IS WHY - THEY ARE CALLED INEXPLICITY)
        #THIS ALSO HAS ARGUMENTS, THAT DEFINE THE SELF OF THE OBJECT 
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount