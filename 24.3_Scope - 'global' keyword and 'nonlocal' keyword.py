'''
1. How to modify a global variable inside a function ?
    We use the 'global keyword' to do this. The global keyword allows us to modify the global variable. It is used to create a global variable and make changes to the variable in a local scope.

2. Rules of global keyword:
    If we assigned a value to a variable within the function body, it would be local unless explicitly declared as global. 

    Those variables that are referenced only inside a function are implicitly global. 

    There is no need to use the global keyword outside a function.

3. Nested Function. effect of nesting on scope.
    When we define a function inside another function, it becomes a nested function. We already know how to access a global function from a function by using a global keyword. 
    When we declare a local variable in a function, its scope is usually restricited to that function alone. 
    This is because each function and subfunction stores its variables in it sepatate workspace. A nested function also has its own workspace. But it can be accessed to the workspaces of all functions in which it is nested. 
    A variable whos values is assigned by the primary function can be read or overwritten by a function nested at any level within the primary.

4. Nonlocal Variables
    The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
    Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.
    We Use the keyword nonlocal to declare that the variable is not local.
'''

# 1.1 . Usage of 'Global keyword' and building a nested function.
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


# 1.2 The same above example without the 'global' keyword.
x = 50 # Global Variable
def harry():
    x=20 
    def rohan():
        x=12
    print(x)
    rohan()
harry() #Local O/P x = 20
print(x) #Global O/P x = 50


# 2.1 'global' keyword 
x = "global"
def funcnew():
    global x
    y = 'local'
    x = 'newlocalx'
    print(f'This is y :- {y}, This is x :- {x}')
funcnew()
print(x) #printing this x before callling the function will still give the value of x as 'global'. since the function hasn't been called, the global keyword hasn't came into effect till now. 
'''
O/P :-
This is y :- local, This is x :- newlocalx
newlocalx
'''

# 2.2 - The same above problem without the 'global' keyword
x = "global"
def funcnew():
    y = 'local'
    x = 'newlocalx'
    print(f'This is y :- {y}, This is x :- {x}')
funcnew()
print(x) #printing this x before callling the function will still give the value of x as 'global'. since the function hasn't been called, the global keyword hasn't came into effect till now. 
#But, printing this x after calling the function funcnew(), will result in the value of global x been replaced by new value of x = newlocalx'''
'''
O/P :- 
This is y :- local, This is x :- newlocalx
global
'''



# 3.1 with 'nonlocal' keyword
def outerfunc():
    x = "local_1"
    def innnerfunc():
        nonlocal x # without the use of this 'nonlocal' keyword , the output of print(output(x)) = gives local_1
        x = "nonlocal"
        print(f'This is inner x : {x}')
    innnerfunc()
    print(f'This is outer x : {x}')
outerfunc()
#O/P
'''
This is inner x : nonlocal
This is outer x : nonlocal'''


# 3.2 the same above problem without the 'nonlocal' keyword
def outerfunc():
    x = "local_1"
    def innnerfunc():
        # without the use of this 'nonlocal' keyword , the output is print(output(x)) = local_1
        x = "nonlocal"
        print(f'This is inner x : {x}')
    innnerfunc()
    print(f'This is outer x : {x}')
outerfunc()
# O/P
'''
This is inner x : nonlocal
This is outer x : local_1 '''

