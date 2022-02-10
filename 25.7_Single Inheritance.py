# Single Inheritance :-
'''
1). What is Inheritance ?
    
    “Inheritance is the ability to define a new class(child class) that is a modified version of an existing class(parent class)”

    The child class can inherit all the functionality of the parent class and add its functionalities also. 
    We know that each class can have its constructor sand methods, so in case of inheritance the child class can make and use its constructor and also can use the constructor of the parent class. 



2) What is Single Inheritance ?

    Single inheritance exists when a class is only derived from a single base class. Or in other words when a child class is using the methods and properties of only a single parent class then single inheritance exists. Single inheritance and Multiple inheritance are very similar concepts, the only major difference is the number of classes. 


3. Advantages of Inheritance.

    It increases the code’s reusability as we do not have to copy the same code again to our new class.

    It makes the program more efficient.

    We can add more features to our already built class without modifying it or changing its functionality.

    It provides a representation of real-world relationships. 


'''


#Example :-
class Parent():
    def first(self):
        print("Parent Function")
    

class Child(Parent):
    def second(self):
        print("Child Function")


Papa = Parent()
Nikku = Child()

Papa.first() #O/P - Parent Function

Nikku.first() #O/P - Parent Function
Nikku.second() #O/P - Child Function

