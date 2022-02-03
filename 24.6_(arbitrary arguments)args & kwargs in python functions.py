# (Arbitrary arguments & Arbitrary keywords) & kwargs in Python functions.
'''
1. What are arbitrary arguments(args*) and arbitrary keywords (kwargs**) ?

    a) We have seen that a function can only pass a certain number of arguments. The number of arguments has to be decided while defining the function, and it can not be changed while calling it. 
    
    b) In simple terms, the number of arguments passed should be the same as the ones that are defined. If we dislike this restriction and do not want ourselves to be bound by certain limits, then we can use *args and **kwargs.

    c) Before discussing *args and **kwargs, we should have a basic knowledge about types of arguments. 
    In Python programming, there are two types of arguments that can be passed in a function.- 
        These are - 
            1) Positional arguments.
            2) keyword arguments.

    d) We have been dealing with positional arguments all along. But keyword arguments are new ones.



2. Why is asterisk used in args* and kwargs** ?

    asterisk is more commonly known in Perl 6 and ruby as a splat operator.

    Asterisk is used in python as a mathematical symbol for multiplication, but in case of arguments, it refers to unpacking. The unpacking could be for a list, tuple, or a dictionary. We will discover more about it by defining *args and **kwargs.



3. In-depth with args*.

    a) args is a short form used for arguments. It is used to unpack an argument. In the case of *args, the argument could be a list or tuple. 
    
    b) Example :- Suppose that we have to enter the name of students who attended a particular lecture. Each day the number of students is different, so positional arguments would not be helpful because we can not leave an argument empty in that case. So the best way to deal with such programs is to define the function using the class name as formal positional argument and student names with parameter *args. In this way, we can pass student's names using a tuple.

    NOTE :- that the name args does not make any difference, we can use any other name, such as *myargs. The only thing that makes a difference is the Asterisk(*).



4. In-depth with kwargs**

    a) The full form of **kwargs is keyword arguments. It passes the data to the argument in the form of a dictionary. 
    
    b) Let's take the same example we used in the case of *args. The only difference now is that the student's registration, along with the student's name, has to be entered. So what **kwargs does is, it sends argument in the form of key and value pair. So the student's name and their registration both can be sent as a parameter using a single ** kwargs statement.

    NOTE :- The name kwargs** doesn't matter. Only double asterisk(**) matters.

    c) One of the instances where there will be a need for these keyword arguments will be when we are modifying our code, and we have to make a change in the number of parameters or a specific function.
'''

# Example
# Args* - Addition of n numbers using args.
def additn(*numbers):
    """This function takes up any number of arguments"""
    sum = 0
    for items in numbers:
        sum = sum + items
    print(f'The product of the numbers {str(numbers)} is {sum}.')

additn(1,2,3)
#O/P :- The product of the numbers (1, 2, 3) is 6.


# kwargs** - Displaying students info using arbitrary keywords.
def intro(**data):
    for key,value in data.items():
        print(f'{key} is {value}.')

intro(Firstname="Pritam", Lastname="Singh", Age=26, Phone=8097150258)
#O/P :- 
'''
Firstname is Pritam
Lastname is Singh
Age is 26
Phone is 8097150258
'''





