''''
1. Scope :-
    A variable is only available from inside the region it is created. This is called 'Scope of the variable'.

2. Local scope :-
    A variable created inside a function belongs to the local scope of that function, and can only be used inside that function. It will exist for as long as the function is executing. The parameter names in the function, they behave like a local variable.

3. Global scope :-
    A variable created in the main body of the python code is a global bariable and belongs to the global scope.
    Global variables are available from within any scope, global and local and we can access it anywhere in the program.

4. How to modify a global variable inside a function ?
    We use the 'global keyword' to do this. The global keyword allows us to modify the global variable. It is used to create a global variable and make changes to the variable in a local scope.

5. Rules of global keyword:
    If we assigned a value to a variable within the function body, it would be local unless explicitly declared as global. 
    
    Those variables that are referenced only inside a function are implicitly global. 
    
    There is no need to use the global keyword outside a function.

'''

# Example 1 (Scope)
num1 = 50 # Global Scope

def func1():
    num1 = 20
    num2 = 12
    print(num1)

func1() #Local O/P num1 = 20
print(num1) #Global O/P num1- 50



# Example 2 (Nested Function)
x = 50 # Global Variable

def harry():
    x=20

    def rohan():
        global x
        x=12

    print(x)
    rohan()

harry() #Local O/P x = 20
print(x) #Global O/P x = 12