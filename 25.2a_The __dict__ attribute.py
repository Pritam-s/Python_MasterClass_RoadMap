# The __dict__ attribute.-
'''
The __dict__ attribute -

    Every object in Python has an attribute that is denoted by __dict__. It maps the attribute name to its value. This dictionary stores all the attributes defined for the object itself.
'''

#Examples -

class plant: # This is the class 'plant'
    water = 5
    soil = 3
    sunlight = 1
    fertilizer = 0.5

print(plant.__dict__) # __dict__ for the class.

Jade = plant()
Jade.type = "Succulent"
Jade.color = "Green"
Jade.pot = "Small"
print(Jade.__dict__) # __dict__ for the object.