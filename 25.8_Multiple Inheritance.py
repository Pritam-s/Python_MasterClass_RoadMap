# Multiple Inheritance :-
'''
1). What is Multiple Inheritance ?

    "In multiple inheritance, a class is derived from more than one class i.e. multiple base classes. The child class, in this case, has features of both the parent classes."


2). How the Multiple Inheritance works ?

    As the name implies, python's multiple inheritance is when a class inherits from more than one class. This concept is very similar to multilevel inheritance. It is also nearly the same as a single-level inheritance because it contains all of the same functionality, except for the number of base classes. 

    NOTE :- While using the concept of multiple inheritance, the order of placing the base classes is very important.



3). Method Overriding.

    Override means having two methods that have the same name. They may perform same tasks or different tasks. 
    
    In python, when the same method defined in the parent class is also defined in the child class, the process is known as Method overriding. This is also true when multiple classes have the same method and are linked together somehow.  
'''

#Example :-
class Father():
    var1 = 10
    def func1(self):
        print("This is the Base1 class")


class Son():
    var1 = 20
    def func2(self):
        print("this is the Base2 class")


class Grandson(Father, Son): #Multiple Inheritance. Note the order of the classes we have provided as an paremeter to the Grandson as an multiple inheritance.
    def func3(self):
        print("This is the Base3 class")

    
Nikku = Grandson()
Nikku.func1()
Nikku.func2()
Nikku.func3()

print(Nikku.var1) #O/P - 10 . If we switch the order of the classes we have provided as an parameter in multiple inheritance the result will be 20.

 #If there is no var1 in inside the Object's class,  the var1 value will be first searched inside the order of the classes provided in the parameter as for Multiple inheritance. that's why it is important to note the order of the classes we have provided as an argument in multiple Inheritance.