'''
# 1. input() function - 

This function allows the user to receive input from the keyboard into the program as a string.

input() function always takes input as a string, i.e., if we ask the user to take a number as input, even then, it will take it as a string, and we will have to typecast it into another data type as per the use case.

eg:- input()
'''

#Example for input() function in python.
example1 = input("Please enter your good name.\n")
print("The name entered by the user is "+ example1+".")


#Example for input() function with typecasting as the default datatype for any input() function is string.
example2 = float(input("Please enter any number of your choice.\n"))
print("The number entered by the user is ", example2)





