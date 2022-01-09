'''
1. Tuples - ( )
    
    A Tuple is an immutable data type in Python. A tuple in python is a collection of elements enclose in () paranthesis. Tuple, once defined, can't be changed, i.e. it's elements or values cannot be altered or manipulated.

    NOTE - 
    * To create a tuple of one/single element, it is necessary to put a comma ',' after that one element like this tup=('element',). because if we only give a single element inside the parenthesis, the python interpreter will interpret it as a single entity.

2. Tuples Methods :-

    Method	Description
    
    count()	Returns the number of times a specified value occurs in a tuple
    
    index()	Searches the tuple for a specified value and returns the position of where it was found
'''

#Examples :-

tup1 = ("Olof", "kumiko", "Teddy", "Puppy", 1232, 54,68,797,98,797,6876,8768,987.9,79,8464,9877,65461654415,11,213,13544,33216,43262,6,True,None)

print('\n This is the count method and the result is',tup1.count(797)) #count() method

print('\n This is the index method and the result is',tup1.index("Puppy")) #index() method

'''
O/P Output -

    
 This is the count method and the result is 2        

 This is the index method and the result is 3 

'''