'''
1. Open(), os.remove() ,Read(), Readline() for Reading files.

    a) Python has a built-in function called 'Open()' to open a file.
    b) The syntax of the function is :- open("File_name", "mode")

2. To open a file two things has to be specified -
    a) Name of the file and it's extension
    b) File Access mode ( r, a, w, b, t, x, + )

3. The files are opened in "rt" mode by default.

4. The open function returns a file object. We store this   file object into a variable which is generally called as a file pointer/ file handler.

5. We can then use this file pointer variable to access the available functions and methods of file operations and perform the modifications to the files.

6. It is always the best practice to close the file after we have done the modifications. Python has a built-in method called 'close()' to close a file.

7. Also, Python runs a garbage collector to clean p the unused objects, but as a good programmers, we must not rely on it and rather close the file using the close() method.

8. To delete a file, python OS module has to be used.
'''

#Examples :-

# 1. open()
f = open("RandomFile.txt", "rb") #Here, the file pointer 'f' is created using which we can do the modifications. changing the defaut file-mode from "rt" to "rb" changes the "read-text mode to read-binary"


# 2. read()
#print(f.read()) # The read() method reads the whole file by default.
'''
2. O/P - 
This is a random file.
This is made to test Python Files IO.
r, a, w, b, t, x, +

'''

# 3. read(size) method
#print(f.read(13)) # We can use the read(size) method where you can specify how many characters we want to return
'''
3. O/P - 
This is a ran
'''


# 4. readline() - readline() method to read individual lines of a file. By calling readline() a second time, you will get the next line.
#print(f.readline()) # O/P - This is a random file.
#print(f.readline()) # O/P - This is made to test Python Files IO.
#print(f.readline()) # O/P - r, a, w, b, t, x, +


# 5. readlines() - readlines() method reads until the end the file ends and returns a list of lines of the entire file. It does not read more than one line.   
#print(f.readlines())
''' O/P -
['This is a random file.\n', 'This is made to test Python Files IO.\n', 'r, a, w, b, t, x, +\n'] '''

# 6. binary mode - binary mode reads the file in binary mode rather than the default text mode. To do that we need to change the mode to "rb" in the open() method.
#print(f.read())
''' 
O/P -

b'This is a random file.\r\nThis is made to test Python Files IO.\r\nr, a, w, b, t, x, +\r\n'
'''

#Important - close() is the built-in method to close a file.
f.close()


#Deleting a file
#Creating a random file named 'newfile.txt'
'''
new1 = open("newfile.txt", "r+")
new1.write("This is the new file which will be deleted using OS module.")
new1.close()
'''

#Later on deleting the same file named 'newfile.txt' using os module.
'''
import os
os.remove("newfile.txt")
'''