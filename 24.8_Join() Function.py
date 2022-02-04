# Join() function in python.
'''
Syntax - string.join(iterable)

1. What is Join() function ?

    "Join is a function in Python, that returns a string by joining the elements of an iterable, using a string or character of our choice."

    "The join() method takes all items in an iterable and joins them into one string.
    A string must be specified as the separator."    

    The iterable can be a list, dictionary, tuple, set, str. int.
    the string that separtes could be a comma, blank space, /n, or anything you wish.



2. Why we use join() function ?

    It's is a lot easier and more compact than using a loop. We use a variable for iteration along with a string or fstring to print all the elements onto the screen.


3. Limitations - 

    a)  In the case of the dictionary, the join function will only return the key part, separated by the string in between, leaving the value side behind.

    b) n situations where the iterable consists of a multi-data type, such as a list or tuple consisting of all integer variables and one single, double variable, the join function will not work. Instead, it will display an error. For join to function properly, all the variables should have the same sort of data type, either it is an integer, string, or any other.

'''


# Examples -


# Example 1 - 
'''list1 = ["Pritam", "Singhwa", "Shailendra", "Kumarwa"] #only single data type allowed.
sep = ' & '
print(sep.join(list1))'''


# Example 2 -
lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]
for item in lis:
    print(item, "and", end=" Stop ") 
#O/P -
'''
John and Stop cena and Stop Randy and Stop orton and Stop Sheamus and Stop khali and Stop jinder mahal and Stop
'''

# Example 3 -
lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]
a = ", ".join(lis)
print(a, "other wwe superstars")
#O/P -
'''
John, cena, Randy, orton, Sheamus, khali, jinder mahal other wwe superstars
'''