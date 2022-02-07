class Employee:
    """This class takes up the details of the employees in our firm"""
    leaves_allowed = 10
    timings = "9 to 5"
    
    def print_details(self): #Self
        return f'The leaves allocated to {self.fullname} is {self.leaves_allowed}, his full name is {self.fullname}, his weight is {self.weight}kgs, his education qualification is {self.edu}'

    def __init__(self, aname, age, weight, edu):
        self.fullname = aname
        self.age = age
        self.weight = weight
        self.edu = edu 
    


#Self
'''
Pritam = Employee()
Pritam.name = "Pritam Singh"
Pritam.salary = 550000
print(Pritam.print_details())'''

#__init__ (Constructor)
print(Employee.__doc__)
Pritam = Employee("Pritam Singh", 25, 68, "B.tech")
print(Pritam.print_details())
print(Pritam.weight)
print(Pritam.change_leaves(34))
print(Pritam.leaves_allowed)


