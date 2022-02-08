# Methods, Self & __init__ Constructors.
'''
1. Methods -

    a) A method is just like a function, with a def keyword and a single parameter in which the object's name has to be passed. 
    Methods in objects are functions that belong to the object.
    The method's purpose is to show all the details related to the object in a single go. 
    
    We choose variables that we want the method to take but do not have to pass them as parameters. Instead, we have to set the parameters we want to include in the method during its creation. 
    Using methods makes the process simpler and a lot faster.

    b) Method vs. Function:
    
    Methods and functions are very similar, yet there are some differences:

        a) Methods are explicitly for Object-Oriented programming.
        b) The method can only be used by the object that it is called for. In simple terms, for a method, the parameter must be an object.
        c)The method can only access the data that is initialized in the class the method is formed in. 



2. Self keyword -

    The self keyword is used in the method to refer to the instance of the current class we are using. The self keyword is passed as a parameter explicitly every time we define a method.

    NOTE :- 
        It does not have to be named 'self' , you can call it whatever you like, but it has to be the first parameter of any function in the class:



3. __init__ method -

    "__init__" is also called a constructor in object-oriented terminology. Whereas a constructor is defined as:

    "Constructor in Python is used to assign values to the variables or data members of a class when an object is created."

    there can be only one constructor for a specific class, so the name of the constructor is a constant, i.e., __init__.

    We declare a constructor in Python using the def keyword,

    In init() method ,arguments are optional. Constructors can be defined with any number of arguments or with no arguments.



4. Types of Constructors in python -

    a)  The default constructor in the one that does not take any arguments.
    b) Constructor with parameters in known as parmeterized constructor.


'''

#Examples :-
class plant:
    pot = 1

    def __init__(self, name, type, water, sunlight, fertilizer, soil): # Self keyword & __init__ constructor
        self.name = name
        self.type = type
        self.water = water
        self.sunlight = sunlight
        self.fertilizer = fertilizer
        self.soil = soil

    def printdetails(self): # self keyword
        return f'the plant name is {self.name} and the type of plant is {self.type} with water requirements is {self.water} and the sunlight requirement is {self.sunlight} and the fertilizer value should be {self.fertilizer} and the soil should be {self.soil} in a units of {self.pot}.'


jade = plant("Jade","Succulent",2, 1, 1, "porous")

print(jade.type)
print(jade.printdetails())

#O/P :-
'''
Succulent
the plant name is Jade and the type of plant is Succulent with water requirements is 2 and the sunlight requirement is 1 and the fertilizer value should be 1 and the soil should be porous in a units of 1.
'''



