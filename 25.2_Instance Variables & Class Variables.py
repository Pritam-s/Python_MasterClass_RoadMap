#Instance Variables & Class Variables
'''
1. What are Instance variables and Class variables ?

    When working with python, we have to work with two ttypes of variables, i.e, 
        - Instance variables 
        - Class variables. 

    OOPS allows the variables to be used at the class level or the instance level. 

    Making use of class and instance variables can ensure that our code adheres to the DRY (don't repeat yourself) principle to reduce repetition within code.



2. A Quick Go-through :-

    Instance Variables - 
        a) Instance variables are created only for a specific object.
        b) The object can change, create, or update only its instance variables.
        c) The objects cannot change the class value or variable by updating it. However, it can change the values of their particular instance variables.
    
    Class Variables -
        a) While, In the case of class variables, the variables and values we create or define are set as default for all the objects. 



3. Instance Variables -

    "Instance variables are the variables for which the value of the variable is different for every instance."

    We can also that the value is different for every object that we create.

    Every instance of the class has its own copy of that variable. Changes made to the variable don't affect the other instances of that class.



4. Class Variables -

    "Class attributes are owned by the class directly, which means that they are not tied to any object or instance."
    

    NOTE :- 
        Updating the value of the class variable will not change it for the instance variables of the objects.


'''


#Examples :-
class Student: #Class
    std = "10th"
    div = "B"
    age = 16

Pritam = Student() #Object 1 - 1st Instance
print(f'Age of Pritam is {Pritam.age}.')
print(f'Division of Pritam is {Pritam.div}.')

Vicky = Student() #Object 2 - 2nd instance
print(f'Age of Vicky is {Vicky.age}.')

Vicky.age = 25 #Assigning a new value to the instance having the class variable "age". 
print(f'New Age of Vicky is {Vicky.age}.')

Student.age = 30 #Assigning a new value to the class variable 'age'.
print(f'New Age of Student is {Student.age}.')

