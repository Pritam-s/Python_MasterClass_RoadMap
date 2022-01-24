''''
1. Writing and Appending to a file -

    i) 'w' mode -
        w stands for write. After opening or creating a files, a function , f.write() is used to insert text int ht he files. The tet is written to the write m ode of the opening file that it overrides the existing data in the file. For a newly created file, it does no harm, but in case of already exisiting files, the previous data is lost as f.write() overrides it.

    ii) 'a' mode -
        a stands for append mode. 'Append' meand adding more content at the end of the existing file unlike 'w' mode which means adding something anywhere to the file. The same function, f.write() is used to add text to the file in append mode.

    iii) 'r+' mode -
        Reading and Writing a file simultaneously. Well, r+ mode is more of a combination of "reading" and "append" than read and write. By opening a file in this mode, we can print the existing content on to the screen by printing f.read() function and adding or appending text to it using f.write() function. 

NOTE :- If you are writing in append mode, start your text by putting a blank space or newline character (\n) else the compiler will start the line from the last word or full stop without any blank space because the curser in case of append mode is placed right after the last character.    
'''


#Examples :-
'''
#. Write Mode
p =  open("FileAppend.txt", "w")
a = p.write("This is a file created for the 22th chapter\n")
print(a) #gives 44
p.close()

'''

'''
# Read Mode
f = open("FileAppend.txt", "a")
a = f.write("Pritam is a good boy\n")
print(a) #gives 21
f.close()

O/P
'''

'''
#Read + Write mode
x = open("FileAppend.txt", "r+")
print(x.read())
x.write("This will append to the end of the content of the file")
'''

'''
Final output in the 'FileAppend.txt'

This is a file created for the 22th chapter
Pritam is a good boy
This will change the content of the file
'''
