'''
1. try and exception handling in python -

    a) What exactly an exception is ?
    " An exception is said as an error, that causes a program to crash. Unlike syntax error, it is syntactically correct and occurs mostly due to our negligence "

    b) Python has built-in support for dealing with many sorts of exceptions automatcially, but we can also define our own.

2. In short -

    a) When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

    These exceptions can be handled using the try statement.

    b) We can also print the exception by converting it into a string. This way program does not terminate but executes completely except for the area where the exception occurred.

3. What it does ?

    a) The 'try' block lets you test a block of code for errors.

    b) The 'except' block lets you handle the error.

    c) The 'else' block lets you execute code when there is no error.

    d) The 'finally' block lets you execute code, regardless of the result of the try- and except blocks.

4. Advantages of using try and except.

    a) Without a try block if an exception occurs the program will surely crash.

    b) If we have some part of code that is not much important but can cause an exception, then we must write it down in the try block so it does not cause the whole program to crash.

'''

# 1.Examples - try and except
'''
print("Please enter the 1st number")
num1 = input()
print("Please enter the 2nd number")
num2 = input()
try:
    print(f'The sum of these numbers is {int(num1)} + {int(num2)} = {num1+num2}')
except Exception as e:
    print(e)

print("This line is very very important")
'''


# 2. Example - try, except, else, finally
print("Please enter the 1st number")
num1 = input()
print("Please enter the 2nd number") 
num2 = input()
try:
    print(f'The addition of the numbers {int(num1)} + {int(num2)} is {num1+num2} ')
except:
    print("This is except statement because Something went wrong")
else:
    print("This is else statement because Everything went fine")
finally:
    print("This is finally statement and This will run regardless of 'no errors' or 'erros'") 