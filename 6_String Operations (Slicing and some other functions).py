'''
1. Strings -

    a) Strings are a combination or collection of characters enclosed in quotes.
    b) Primarily there are three types of strings in python -
        i)      Single Quote string - 'Single Quote'
        ii)     Double Quote string - "Double Quote"
        iii)    Triple Quote string - "'Triple Quote"'


2. Some Functions() to be used with Strings.

    a) len() Function.
    b) input() 
    c) str()
    d) hash()
    etc ....

3. Slicing of strings.
    a) In python, string slicing s[n:m] for a string is done as characters of s from n to m-1. 
    syntax :- word[n:m]
    b) Sometimes, we need to skip some value. By default the skip value is 1.
    syntax :- word[n:m:skip value]
    c) we can also put -negative skip value.

4. Some Important string methods :-

    string.endswith(): 

    string.count(): 

    string.capitalize(): 

    string.upper(): 

    string.lower()

    string.find(): 

    string.replace(“old_word”, “new_word”): 
    
'''



var1 = "Pritam Singh is a good guy"
print(var1[3:15:2]) # Slicing 
print("This is the hash of",var1,hash(var1)) #Hash() Function
print(type(var1)) #type() class function
print(len(var1)) #len() function