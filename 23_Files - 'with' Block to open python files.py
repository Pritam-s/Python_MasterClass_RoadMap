'''
1. Using 'With' blocks to open python files -

    a) There is more than one method to open and close files. 'with' block is another yet a better & straightforward approach to open and close a file, including syntax and benfits.

    b) Opening a file is important, but closing the file is also similarly very important. 
    If we do not close our file after we are done using it, then the file object will keep on consuming processor memory, and also, there will be more chances of exceptions as the file is still open hence, more chances of bugs.


2. Syntax of with block -

    With open("File_name.txt") as f:

    where, f is the object of the file.
    There is no close() function required here.


3. Benefits of with block - 

    What opening a file with "With block" actually does is to create a context manager that automatically closes a file after processing it. 
    Another benefit of using a “With block” is that we can open multiple files in a single block by separating them using a comma. All the files could have different modes of opening. 
    For example, we can access one file for reading and another one for writing purposes. Both files should have different objects referring to them.


4. Bried advantages of 'with' block -

    a) Multiple files can be opened.

    b) The files that are opened together can have different modes.

    c) Automatically closes file.

    d) Saves processing power by opening and closing file only when running code inside the block.

    e) Creates a context manager, so lesser chances of an exception occurring.
'''


# Examples -

with open("RandomFile.txt") as p:
    a = p.readlines()
    print(a)