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
    e) max()
    f) min()
    etc ....

3. Slicing of strings.
    a) In python, string slicing s[n:m] for a string is done as characters of s from n to m-1. 
    syntax :- word[n:m]
    b) Sometimes, we need to skip some value. By default the skip value is 1.
    syntax :- word[n:m:skip value]
    c) we can also put -negative skip value. 
        * Never put -negative skip value lesser than -1.

4. Some Important string methods :-

    string.endswith(): 

    string.count(): 

    string.capitalize(): 

    string.upper(): 

    string.lower()

    string.find(): 

    string.replace(“old_word”, “new_word”): 


5. List of all available String Methods :-

    Method	Description
    
    capitalize()	Converts the first character to upper case

    casefold()	Converts string into lower case

    center()	Returns a centered string

    count()	Returns the number of times a speci
    fied value occurs in a string

    encode()	Returns an encoded version of the string

    endswith()	Returns true if the string ends with the specified value

    expandtabs()	Sets the tab size of the string

    find()	Searches the string for a specified value and returns the position of where it was found

    format()	Formats specified values in a string

    format_map()	Formats specified values in a string

    index()	Searches the string for a specified value and returns the position of where it was found

    isalnum()	Returns True if all characters in the string are alphanumeric

    isalpha()	Returns True if all characters in the string are in the alphabet

    isdecimal()	Returns True if all characters in the string are decimals

    isdigit()	Returns True if all characters in the string are digits

    isidentifier()	Returns True if the string is an identifier

    islower()	Returns True if all characters in the string are lower case

    isnumeric()	Returns True if all characters in the string are numeric

    isprintable()	Returns True if all characters in the string are printable

    isspace()	Returns True if all characters in the string are whitespaces

    istitle()	Returns True if the string follows the rules of a title

    isupper()	Returns True if all characters in the string are upper case

    join()	Joins the elements of an iterable to the end of the string

    ljust()	Returns a left justified version of the string

    lower()	Converts a string into lower case

    lstrip()	Returns a left trim version of the string

    maketrans()	Returns a translation table to be used in translations

    partition()	Returns a tuple where the string is parted into three parts

    replace()	Returns a string where a specified value is replaced with a specified value

    rfind()	Searches the string for a specified value and returns the last position of where it was found

    rindex()	Searches the string for a specified value and returns the last position of where it was found

    rjust()	Returns a right justified version of the string

    rpartition()	Returns a tuple where the string is parted into three parts

    rsplit()	Splits the string at the specified separator, and returns a list

    rstrip()	Returns a right trim version of the string

    split()	Splits the string at the specified separator, and returns a list

    splitlines()	Splits the string at line breaks and returns a list

    startswith()	Returns true if the string starts with the specified value

    strip()	Returns a trimmed version of the string

    swapcase()	Swaps cases, lower case becomes upper case and vice versa

    title()	Converts the first character of each word to upper case

    translate()	Returns a translated string

    upper()	Converts a string into upper case

    zfill()	Fills the string with a specified number of 0 values at the beginning

'''



var1 = "Pritam Singh is a good guy"
print(var1[3:15:2]) # Slicing 
print("This is the hash of",var1,hash(var1)) #Hash() Function
print(type(var1)) #type() class function
print(len(var1)) #len() function

#Some important Methods :-
print(var1.upper()) #upper() method
print(var1.find("good")) #endswith() method
print(var1.replace("good", "awesome")) #replace() method
print(var1.count("i")) #count() method
print(var1.lower()) #lower() method
print(var1.endswith("girl")) #endswith() method - returns true or false.
print(var1.title()) #title() method - Capitalized 1st character of each word.

