# Staticmethods
'''
1. What is the need of Classmethods as an alternative constructor. ?

    Using a method as a constructor. It has its own advantages. By using a method as a constructor, we would be able to pass the values to it using a string.

    Note that we are talking about a class method, not a static method.



2. Working of the Classmethods as an alternative constructor.
    
    The parameters that we have to pass to our constructor would be the class i.e., cls and the string containing the parameters. Moving on towards the working, we have to use a function "split()," that will divide the string into parts. And the parts as results will be stored in a list. We can now pass the parameters to the constructor using the index numbers of the list or by the concept of *args.



3. split() :-

    What split() does is, it takes a separator as a parameter. If we do not provide any, then the default separator is any whitespace it encounters. Else we can provide any separator to it such as full stop, hash, dash, colon, etc. After separating the string into parts, the split() function stores it into a list in a sequence. 
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

    @classmethod # classmethod as alternative constructor

    def from_dash(cls, text): # method I prefer (using  dunder methods such as __getitems__ , __contains__ . etc)
        var = text.split("-")
        return(var)


    ''' def from_dash(cls, text): #method to get items as list and indexed.
        var = text.split("-") 
        return cls(var[0], var[1], var[2], var[3], var[4], var[5])'''

    
    '''def from_dash(cls, text): # shorthand method using *args
        return cls(*text.split("-"))'''

        
        


jade = plant("Jade","Succulent",2, 1, 1, "porous")

print(jade.type)
print(jade.printdetails())

peace_lily = plant.from_dash("Peace-lily-requires-more-water-sandsoil")
print(peace_lily)
print(peace_lily.index('water'))
print(peace_lily.__getitem__(3))
print(peace_lily.__getitem__(5))
print(peace_lily.__contains__("water"))


