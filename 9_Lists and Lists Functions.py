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


#Examples :-

lists1 = ["Hello","Kumiko",True,456,334.98,"Olof","Teddy",False,None,546,87,"Puppy"]

lists2 = [454,64,54,87,64,2,5,6,84,6,43,21,84,354,846,354465,431,654687,6843,676,3,44,6,6,6]

#Some important Built-in functions -
print(len(lists1))
print(type(lists1))
print(max(str(lists1)))
print(min(str(lists1)))
print(max(lists2))
print(min(lists2))

#Indexing & Slicing
print(lists1[::])
print(lists1[0:12:1]) #Using default values of start_index, stop_index and step. start_index - 0, stop_index - length of the list, index - 1.
print(lists1[::-1]) #reverse the list
print(lists1[::-3]) #Using -ve step value smaller than -1 gives appropriate results as there are no values for arguments for the start_index and stop_index.
print(lists1[0:12:-3]) #Using the -ve step value smaller than -1 will result in an unexpected behavior as there are values for arguments of start_index & stop_index.
print(lists1[2:9:-1])


#Lists Methods -

#count()
print('\nThis is the count() method and the result is',lists2.count(6)) #count()

#extend() - here lists2 extends lists1
print(lists1.extend(lists2))
print('\nThis is the extend() method and the result is',lists1)

#append()
lists1.append('This is the appended item')
print('\nThis is the append() method and the result is',lists1)

#index()
print('\nThis is the index() method and result is',lists2.index(21))

#pop() - We put index number as an argument. Here 'Hello' having index 0 is popped and removed.
lists1.pop(0)
print('\nThis is the pop() method and the result is',lists1)

#remove() - We put the item-name as it is. Here None from list1 is removed.
lists1.remove(None) 
print('\nThis is the remove() method and the result is',lists1)

#reverse()- reverse 
lists1.reverse()
print('\nThis is the reverse() method and the result is',lists1)

#sort() - method
lists2.sort()
print('\nThis is the sort() method and the result is', lists2)
