# Static Methods :-
'''
1). What are Static Methods ?

    Static method is one of the important concepts to use while you are learning OOPs programming with Python. 
    
    A static method is very much easy to understand if we are familiar with class methods. It is also easier to implement than a class method because it can be accessed without any object. However, we can also access it using a class or any instance.

    NOTE :- We do not need the self or cls to be passed as the first argument in a static method.



2.) Static methods in python.

    a static method in Python is treated differently than in other languages. Static methods in Python are extremely similar to python class methods, but the difference is that a static method is bound to a class rather than the objects for that class.
    
    To define a static method, we use the @staticmethod decorator, which is a built-in decorator. Also, there is no need to import any module to use decorators. 
    
    Using a static method in a class, we permit it to be accessed only by the class objects or inside the class.



3. Usage of static methods -

    Static methods do not require any knowledge related to the class that they are built-in. They are only formed in a class so that only the class instances can access them. We can use a static method for simple functionality that is mostly not related to the class.



4. Advantages of Python static method. -

    Static methods have a very clear use case. When we need some functionality not for an Object but with the complete class, we make a method static. This is advantageous when we need to create utility methods.
    
    NOTE :-  We do not need the self or cls to be passed as the first argument in a static method.
'''

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

    #The static method needs no self or cls. Also it has no knowledge related to a class. also, a static method cannot alter or change any variable value or state of the class.
    @staticmethod 
    def addition(a,b):
        return a+b

jade = plant("Jade","Succulent",2, 1, 1, "porous")

print(jade.type)
print(jade.printdetails())

print(jade.addition("Jade", "Succulent"))
print(jade.addition(5,4))