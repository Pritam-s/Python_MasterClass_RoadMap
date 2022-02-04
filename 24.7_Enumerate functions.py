# Enumerate functions :- syntax - enumerate(iterable_items, start_index=0)
'''
1. What is an enumerate function ?

    "An enumerater is a built-in function that provides and index to data structure elements, making iterations through them easier and simpler."

    To cycle through items of a data structure, we normally write an for loop with an iterator and an integer variable which we have to increment every time the loop runs. -- To replace this procedure we have a python built-in function known as 'enumerate function'.



2. Working of an enumerate function.

    What enumerate function does is, it assigns an index to every element or value in the object that we want to iterate, so we do not have to assign a specific variable for incremental function, instead we have to apply a for loop, and our function will start working. Its syntax is a lot simpler and shorter than what we have been following till now.



3.Syntax
    
    enumerate(iterable, start=0)
    When calling a simple enumeration function, we have to provide two parameters:

    The data structure that we want to iterat.
    The index from where we want to start our iteration.



4. Advantages of using Enumerate:-

        It is a built-in function.

        It makes the code shorter.

        We do not have to keep count of the number of iterations.

        It makes the implementation of for loop simpler and cleaner.

        Lesser code so lessor chances of error and bugs.

        We can loop through string, tuple or objects using enumerate.

        We can start the iteration from anywhere within the data structure as we have the option of providing the starting index for iteration.
'''


# Examples :-

# 1. Iterating through the items of a list.
list1 = [416,324,3312,576,4531,11,23,4,1,2,3,"Pritam","Shailendra","Vicky"]
for index,items in enumerate(list1):
    try: 
        if(items%2==0):
            print(f'index {index} & item-name {items}')
    except Exception as errormsg:
        print(f'{items} - are string type data and error message display :- {errormsg}.')
# O/P :-
'''
index 0 & item-name 416
index 1 & item-name 324
index 2 & item-name 3312
index 3 & item-name 576
index 7 & item-name 4
index 9 & item-name 2
Pritam - are string type data and error message display :- not all arguments 
converted during string formatting.
Shailendra - are string type data and error message display :- not all arguments converted during string formatting.
Vicky - are string type data and error message display :- not all arguments converted during string formatting.'''



# 2. Printing all the items of a tuple as a list.
tuple1 = ("Hello", "Goodmorning", "Pritam", "Singhwaa","Vicky","Guptain","Shailendra", "Kumarwa", 323, 5468)
result = enumerate(tuple1,6)
print(list(result))
'''
O/P :- 
[(6, 'Hello'), (7, 'Goodmorning'), (8, 'Pritam'), (9, 'Singhwaa'), (10, 'Vicky'), (11, 'Guptain'), (12, 'Shailendra'), (13, 'Kumarwa'), (14, 323), (15, 5468)]
'''



# 3. Creating a Dictionary and using enumerate.
Students = {
    "Name":"Pritam Singh",
    "Roll No":24,
    "Std":"3rd B"
}
for index,items in enumerate(Students.items()):
    print(index,items)
#O/P
'''
0 ('Name', 'Pritam Singh')
1 ('Roll No', 24)
2 ('Std', '3rd B')
'''