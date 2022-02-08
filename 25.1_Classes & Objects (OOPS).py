#Classes & Objects (OOPS) -
'''
1. What is Object oriented programming (OOP) paradigm ?
    
    Python is a powerful programming language that supports the object-oriented programming paradigm. In object-oriented programming, the program splits into self-contained objects. Each object represents a different part of the application which can communicate among themselves.

    A programming technique that requires the use of objects and classes is known as OOP. Object-Oriented Programming is based on the principle of writing reusable code that the user can access multiple times.



2. What is python Classes ?

    A class is a collection of Objects.
    
    A class is like an object constructor, or a 'Blueprint' for creating objects.



3. What is python objects ?

    Almost everything in Python is an object, with its properties and methods.

    An object is defined as an instance of a class possessing attributes. 
    
    Every object has a state and a behavior.



4. Why to use OOPS and classes ?

    By using oop, we can divide our code into many sections known as classes. Each class holds a distinct purpose or usage. For example, if we have created a class named "Books," then all the attributes it possesses should be related to books, such as the number of pages, publishing date or price, etc.

    There is no limit to the number of classes we can create in a program. Also, one class can be easily accessible by another, and we can also restrict the access of a class so other classes can not use its functions. This concept comes in handy while working on bigger projects. 
    
    
    Eg:- All the employees are given separate tasks to work on the classes they have been assigned. And after they are done with their contribution, the classes can be combined as a whole to form a complete project. 




'''

class plant: # This is the class 'plant'
    water = 5
    soil = 3
    sunlight = 1
    fertilizer = 0.5


ZZ = plant() #Object 1 - 1st instance of the class 'plant'
print(f'Fertilizer requirement for ZZ plant is {ZZ.fertilizer}.') #O/P - Fertilizer requirement for ZZ plant is 0.5
print(f'Sunlight requirement for ZZ plant is {ZZ.sunlight}.') #O/P - Sunlight requirement for ZZ plant is 1.


Peace_Lily = plant() #Object 2 - 2nd instance of class 'plant'
print(f'The soil requirement for peace lily is {Peace_Lily.soil}.') #O/P - The soil requirement for peace lily is 3.
print(f'The water requirement for peace lily is {Peace_Lily.water}.') #O/P - The water requirement for peace lily is 5.




