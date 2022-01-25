'''
1. Functions and Docstrings -

    a) Definition :-
        Functions can be defined as lines of code that are built to create a specific task and can be used again and again in a program when called


    b) There are two types of functions in the Python lang.
        
        - Built-in functions.
        [ eg:- print(), sum(), type(), range(), list(), str(), etc .... ]

        - User-defined functions 
    

    c) Creating a function :-

        In order to create a function, we have to use the "def" keyword accompanied by the function's name with a pair of parentheses.


    d) Arguments and parameters :-

        The purpose of paranthesis is to send arguments or parameters to a function.
        In other words, the parameters can be defined as values that are sent in the paranthesis.

        NOTE :- The terms parameter and arguments can be used for the same thing : information that are passed into a function.

        From a function's perspective:

            A parameter is the variable listed inside the parentheses in the function definition.

            An argument is the value that is sent to the function when it is called.    

    e) Return values :-

        Some functions may return a value to the caller, so in order to get the value, a return statement is put at the end of the body of the function that gives the values that has been calculated by the function.
        i.e. The Function can 'return' data as a result.
    

    f) Function calling :-

        Calling a function is very easy, we just habe to write the name of the function along with the closing paranthesis. If any arguments are required than we put those in the paranthesis.
        But, if it does not return anything, then we leave them empty.

    
2. Advantages of Functions :-

    If we are working on a big project then we will prefer to make as many functions as possible, so every other member of our team could use that.

    By using functions, we can avoid the repetition of code to an extent. As we have discussed in the previous tutorial i.e. Tutorial #22, more lines of code mean less efficiency. Also repeating the same code at different places will just make the code more crowded than required.

    The reusability of code is ensured by using functions. We can even use a function inside another function or in any part of our code.

    By making a function of code that we are going to use again and again, we can save a lot of time.
    

3. Docstrings -

    Docstring is a short form of documentation string. Its purpose is to give the programmer a brief knowledge about the functionality of the function.

    The syntax for writing a docstring is very simple as it is just a string written in between three double quotes placed three times (""" """) on either side of the string. But it has to be the first line of code in the function’s body. 
    
    To call a docstring we write the name of the function followed by ._doc_.

'''

# Examples :-

# Eg 1 Sum of two numbers

def sum(a,b):
    """This function simply adds two numbers."""
    add = a+b
    print(f'The sum of the two numbers {a} + {b} is {add}.')
    #return add


#sum(20,40)
num1 = sum(20,40) #The sum of the two numbers 20 + 40 is 60.
print(num1) # 'None' coz we haven't assigned a return value


#Eg 2 - Division of two numbers
'''
def funct2(a,b):
    """This function simply calculated the average of two numbers"""

    avg = (a+b)/2  #avg is the temporary variable made for storing the result of the expression.
    print(f'The average of two numbers {a} and {b} is {avg}')
    return avg  # Without the return value we cannot use the obtained result for anything. the value of the avg variable is now returned .i.e we can now assign the result obtained into a variable and use it for modifications.



num2 = funct2(30,45) # The average of two numbers 30 and 45 is 37.5
print(num2)  # 37.5
print(num2 + 20)  # 57.5

'''