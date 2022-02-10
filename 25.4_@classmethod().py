#@classmethod in python OOPS.
'''
1). What is classmethods() ?
    
    As we have observed, we cannot change the value of a variable defined in the class from outside using an object. Instead, if we try that, a new instance variable will be created for the clas having the value we assigned. But no change will occur in the original value of the variable.

    The classmethod() function is used to convert a method into a class method.



2.) Working of a classmethod.

    A class method receives the class as implicit first argument, just like an instance method receives the instance.

    Class methods take 'cls' parameter that points to the class and not the object instance when the method is called.



3.) @classmethod decorator.

    A @classmethod Decorator is a built-in function in Python. It can be applied to any method of the class. We can change the value of variables using this method too.


4.) To sum up :-

    The Python class method is a way to define a function for the Python class. It receives the class as an implicit first argument. Using @classmethod decorator, creating as many constructors for a class that behaves like a factory constructor is possible.
'''

# Examples :-
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


    @classmethod
    def change_pot(cls, new_pot):
        cls.pot = new_pot


jade = plant("Jade","Succulent",2, 1, 1, "porous")

print(jade.type)
print(jade.printdetails())

ZZ = plant("ZZ", "Succulent", 0.5, 0.5, 0.5,"porous")
print(ZZ.printdetails())
print(f'Before class method the value of pot in instance variable is {ZZ.pot}')
print(f'Before class method the value of pot in class variable is {plant.pot}')

#Change in the value of a instance variable for a class variable doesn't changes the value of the class variable. That's why we use @classmethod.
'''ZZ.pot = 5 
print(f'After changing the value of pot in instance variable, the value of pot is {ZZ.pot}')
print(f'After changing the value of pot in class variable, the value of pot is {plant.pot}')'''

ZZ.change_pot(10) #Applying the @classmethod()
print(f'After applying the @classmethod. changing the value of pot in instance variable, the value of pot is {ZZ.pot}.')
print(f'After applying the @classmethod. changing the value of pot in class variable, the value of pot is {plant.pot}.')



