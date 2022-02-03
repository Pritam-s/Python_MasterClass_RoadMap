# Python Lambda/Anonymous Functions or Throw-away functions.
'''
1. What is Lambda/Anonymous or throw-away functions ?

    a) In Python programming, an anonymous function or lambda expression is a function definition that is not bound to an identifier (def).

    b) While normal functions are defined using the 'def' keyword in python, the lambda functions are defined using the 'lambda' keyword.
    
    c) The anonymous function is an inline function. The lambda/anonymous functions are created using 'lambda' keyword/operator.

    d) Lambda operator cannot contain multiple expressions.

    e) Anonymous/Lambda functions can accept inputs and return the outputs, just like other functions do.



2. Differences between lambda expressions and simple functions.

    a. Can be passed immediately with or without variables.
    b. They are inline functions.
    c. Automatic return of results.
    d. There is neither a document string nor a name.



3. Why do we use Python Lambda functions ? What is the need of the lambda functions ?

    a. The main use of anonymous functions is, when we need a function just once. there is no need to create a function when a function is needed just once in our program.

    b. We can create anonymouse functions whenever needed. That's why they are also called as throw-away functions. 
 


4. Use cases of Python lambda/anonymous functions ?

    a. We use lambda functions when we require a function only once. 
    b. This throw-away functions are used along with other predefined functions such as reduce(), filter(), and map(). These functions help reduce the number of lines of the code when compared to named python functions.
'''

# Examples :-

# 1.1. A simple function to add two numbers.
def add(a,b):
    """This function just adds two numbers"""
    return a+b
print(f'This is the simple function and the addition of a + b is {add(9,5)}') #O/P - 14
 

# 1.2. The same example with lambda function.
add = lambda x,y : x+y
print(f'This is the lambda function and the addition of x + y is {add(10,20)}') # O/P - 30


# 2.1 
product = lambda x,y:x*y
print(product(9,3)) #O/P - 27


# 3
double = lambda x:x*2
print(double(5)) #O/P - 10


