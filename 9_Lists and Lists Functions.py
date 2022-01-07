'''
1. Lists -
    
    a) Python lists are containers used to store a list of values of any data type.
    b) We can also say that it is a collection of elements from any data type.

    c) Special Properties of Lists :
         List is a collection which is :-
         ordered.
         changeable. 
         Allows duplicate members.


2. Indexing of Lists -

    a) List elements can also be accessed by using Indices, i.e. the first element has 0 and so on.
    b) If you put an index that isn't on the list, you will get an error.


3. Slicing of Lists -

    a) Like string slicing, we can also do slicing of Lists. Also the default value of step argument is 1 (same as in string).
    
    slice1 = list1[start_index : stop_index : step]

    b) NOTE -
        * Never put any negative number smaller than -1 in step argument while slicing. eg:- -2, -3, -4 should never be used in Lists and strings. It doesn't works for some reason. (Could be supported in newer versions.)

        * The default value of 'start_index' is always 0. Likewise, the default value of 'stop_index' is always the length of the list or string.


4. List Methods -
    Some mostly used methods.
    a) list.append()
    b) list.insert()
    c) list.remove()
    d) list.pop()
    e) list.sort()


5) All Lists Methods - 

    Method	    Description

    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list
'''

