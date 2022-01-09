'''
1. Sets - { }

    a) The concept of sets in python is same as in mathematics.

        In Mathematics :-
            "A set is a collection of well-defined objects and non-repetitive elements." 
            i.e. - A set with 1,2,3,4,3,4,5,2,2,3 is can be written as {1,2,3,4,5}.
    
        In Python :-
            "A set is a data strucure having unordered, unique and unindexed elements."
            Elements are also called as Entries, and no two entries could be same.


    b) Properties of Sets :-

        * Iterable (Iterations can be perfromed using loops)
        * Mutable (can be updated by adding or removing entries)
        * No duplication allowed.

    c) Structure of Sets :-

        i) Elements are written between two curly brackets separated by comma. eg:- set1 = {1,2,3,4,5}

        ii) There is also a Built-in 'set' constructor function which can be used to form a set.

    NOTE :- Sets is not exclusive to only Python. Many programming languages have sets data type like C++,Java, Swift, JavaScript. Pascal was amongst the 1st language to have supported Sets.

2. Sets Methods :-

    Method	Description

    add()	Adds an element to the set

    clear()	Removes all the elements from the set

    copy()	Returns a copy of the set

    difference()	Returns a set containing the difference between two or more sets

    difference_update()	Removes the items in this set that are also included in another, specified set

    discard()	Remove the specified item
    intersection()	Returns a set, that is the intersection of two other sets

    intersection_update()	Removes the items in this set that are not present in other, specified set(s)

    isdisjoint()	Returns whether two sets have a intersection or not

    issubset()	Returns whether another set contains this set or not

    issuperset()	Returns whether this set contains another set or not

    pop()	Removes an element from the set

    remove()	Removes the specified element

    symmetric_difference()	Returns a set with the symmetric differences of two sets

    symmetric_difference_update()	inserts the symmetric differences from this set and another

    union()	Return a set containing the union of sets

    update()	Update the set with the union of this set and others


'''



# Examples :-

s = set() #set initialized using 'set' constructor.
s2 = {65,69,25}
# 1. add()
s.add(420) # add() method -single element added using add() method.
print('\nA single element is added to the set using add() method and the result is',s,'\nNOTE:- add() takes only one argument.\n')

s.add(420)
s.add(69)

#
print('The s is a set with elements s =',s)
print('The s2 is a set with elements s2 =',s2)

#2. difference()
s.difference(s2)
print('\nThis is the difference() method and the result is',s)

#3. difference update()
s.difference_update(s2)
print('\nThis is the difference update() method and the result is',s)

# 4. Intersection()
s.intersection(s2)
print('\nThis is the intersection() method and the result is',s)

# 5. isdisjoint()
print('\nThis is the isdisjoint() method and the result is',s2.isdisjoint(s))

# 6. issubset()
print('\nThis is the issubset() method and the result is',s.issubset(s2))

# 7. issuperset()
print('\nThis is the issuperset() method and the result is',s.issuperset(s2))

#8. symmetric_difference()
new = s.symmetric_difference(s2)
print('\nThis is the symmetric_difference() method and the result is',new)

#9. union()
new2 = s.union(s2)
print('\nThis is the union() method and the result is',new2)

#10. update()
s.update(s2)
print('\nThis is the update() method and the result is',s)

