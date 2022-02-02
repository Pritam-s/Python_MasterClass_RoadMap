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

6. Nested Function. effect of nesting on scope.
    When we define a function inside another function, it becomes a nested function. We already know how to access a global function from a function by using a global keyword. 
    When we declare a local variable in a function, its scope is usually restricited to that function alone. 
    This is because each function and subfunction stores its variables in it sepatate workspace. A nested function also has its own workspace. But it can be accessed to the workspaces of all functions in which it is nested. 
    A variable whos values is assigned by the primary function can be read or overwritten by a function nested at any level within the primary.

7. Nonlocal Variables
    The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
    Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.
    We Use the keyword nonlocal to declare that the variable is not local.
'''


# 1. Creating a Global Variable (Will be accessible inside as well as outside a function)
var1 = 220
def test():
    print(f'This num1 {var1} is also accessible inside the function.')

test()
print(f'This num1 {var1} is also accessible outside the function.')
#O/P :-
#This num1 220 is also accessible inside the function.
#This num1 220 is also accessible outside the function.



# 2. Creating a Local variable (will be available only inside the function) (Local Scope)
num1 = 50 #Global Variable
def func1():
    num1 = 20 #Local var
    num2 = 12 #Local var
    print(f'This is the local num1 {num1} and local num2 {num2}')

func1() 
print(f'This is the global num1 {num1}') 
#O/P - 
#This is the local num1 20 and local 12
#This is the global num1 50

