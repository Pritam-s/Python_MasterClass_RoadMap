'''
1. Dictionaries - { }

    a) Python Dictionaries is an unordered collection of items. Each of the dictionary items has a key and a value pair. i.e Key-value pair.

    b) Every programming language has it's distinct key feature. Python's one out-of-the-box feature is "Dictionaires".

    c) Special properties / features of dictionaries :-

        * It is unordered
        * It is mutable
        * It is indexed (after the Python 3.7th update, the compiler stores the entries in the order they are created)
        * No duplication of data allowed

'''

#Examples :-

dict1 = { 
    "Name" : "Pritam Singh",
    "Age" : 25,
   "Bike" : "RTR 180 ABS",
    "Alias" : "Olof",
    "Cc" : 180,
    "Passing" : 2015
}

dict2 = {
    "food" : "Chicken BBQ",
    "Drink" : "Dextrose Monohydrate"
}

print('\nThis is the fromkeys() method and the result is',dict1.fromkeys(dict1,dict2)) #fromkeys method

print('\nThis is the get() method and the result is',dict1.get("Alias")) #get() method

print('\nThis is the items() method and the result is',dict1.items()) #items() method

print('\nThis is the values() method and the result is',dict1.values()) #values() method


#O/P - Output

    '''
    This is the fromkeys() key and the result is {'Name': {'food': 'Chicken BBQ', 'Drink': 'Dextrose Monohydrate'}, 'Age': {'food': 'Chicken BBQ', 'Drink': 'Dextrose Monohydrate'}, 'Bike': {'food': 'Chicken BBQ', 'Drink': 'Dextrose Monohydrate'}, 'Alias': {'food': 'Chicken BBQ', 'Drink': 'Dextrose Monohydrate'}, 'Cc': {'food': 'Chicken BBQ', 'Drink': 'Dextrose Monohydrate'}, 'Passing': {'food': 'Chicken BBQ', 'Drink': 'Dextrose Monohydrate'}}

    This is the get() key and the result is Olof

    This is the items() method and the result is dict_items([('Name', 'Pritam Singh'), ('Age', 25), ('Bike', 'RTR 180 ABS'), ('Alias', 'Olof'), ('Cc', 180), ('Passing', 2015)])

    This is the values() method and the result is dict_values(['Pritam Singh', 25, 'RTR 180 ABS', 'Olof', 180, 2015])
    '''

