'''
1. tell() function -

    a) tell() function is used to know the position of the file(read/write) pointer.
    b) f.tell() returns an integer giving the file pointercurrent position.
    c) File pointer/file handler is likea a cursor, which defines from where the data has to be read or written in the file.

2. seek() function -

    a) seek() function is used to the change the position of the file pointer/file handler.
    b) When we open a file, the system points to the beginning of the file. Any read or write will happen from thre start. To change the file object's position, use "seek(offset, whence)" function.
    c) If we want to read the file but skip the first 5 bytes, open the file, use function seek(5) to move to where you want to start reading, and then continue reading the file.
'''

f=open("RandomFile.txt", "rt")
print(f.readline()) # O/P - This is a random file.  
print(f.tell()) # O/P -  24
print(f.seek(12)) # O/P - 12
print(f.readline()) # O/P - ndom file.
f.close() # closes the file.