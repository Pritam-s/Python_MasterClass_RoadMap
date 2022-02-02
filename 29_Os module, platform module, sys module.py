'''
1. OS Module :-

    OS module provides our code with a direct connection to the operatin system. We can use its different functions to interact and do activities on our operating system. 
    
    For example, if we want to create such a software that needs to store or access file from a directory or folder, we can use the OS module to perform the task for us. 

    To use OS module, simply import it.


2. OS module :- 

    Some built-in OS functions -

    NOTE :- We can use print(help(function_name, Object)) to get all the details of that particular object.


    print(dir(os))
    It gives us a list of all the functions the OS module is composed of.


    os.getcwd( ):
    Here cwd is a short form for the current working directory. The function returns us the path of the directory we are currently in. It is important to know about our directory because when we are trying to import a file in python, the compiler searches for it in our current directory.


    os.chdir( ):
    It is used in case we want to change our directory. The new path is sent inside the parenthesis. If we want to access some files or folders from some other directory, we can use it.


    os.listdir( ):
    If we want to output the names of all the directories at a certain location, we can use this function.


    os.mkdir( ):
    To create a new directory or folder. The name is sent as a parameter inside the parenthesis.


    os.makedirs( ):
    To make more than on directory simultaneously.


    os.rename( ):
    To rename an already existing directory, we use this. We send the current name and new name of our directory as parameters.


    os.rmdir()
    It deletes an empty directory.


    os.removedirs()
    We can remove all directories within a directory by using removedirs(). 


    os.environ.get()
    It will return us the environment variable. The environment variable must be set, or the function will return null.


    os.path.join()
    It joins one or more path components. We can join the paths by simply using a + sign, but the benefit of using this function is that we do not have to worry about extra slashes between the components. So less accuracy still provides us with the same result.


    os.path.exists( ):
    It returns us a Boolean value, i.e., either true or false. It is used to check whether a path exists or not. If it does, then the output will be true, otherwise false.


    os.path.isfile( ):
    It returns true if the path is an existing regular file.


    os.path.isdir( ): 
    It returns true if the path is an existing directory.


3. platform module :- 
    
    Some important platform modules in-built functions -

    platform.architecture()

    platform.system()

    platform.platform()

    platform.machine()

    platform.node()

    platform.processor()

    platform.python_build()

    platform.python_compiler()

    

4. Some important sys modules in-built -

    print(help(sys))

    sys.version 

    sys.platform 

    sys.winver

    sys.getwindowsversion()

    sys.modules

    sys.getrefcount("pritam")

    sys.path

    sys.stderr

    sys.stdin

    sys.stdout
'''

#Examples :-

import os

print(dir(os))

print(f'This is the initial working dir {os.getcwd()}')

os.chdir('X:\Desktop_Reloaded\F2_WebDevolpment Projects\Python_MasterClass_RoadMap\Programs')

print(f'This is the current working dir {os.getcwd()}')

print(os.listdir())

print(os.path.isfile("X:\Desktop_Reloaded\F2_WebDevolpment Projects\Python_MasterClass_RoadMap\\FileAppend.txt"))



# Platform module
import platform
print('Platform Architecture ',platform.architecture())
print('Platform System ',platform.system())
print('Platform platform ',platform.platform())
print('Platform machine ',platform.machine())
print('Platform node ',platform.node())
print('Platform processor - ', platform.processor())
print('Platform python build - ',platform.python_build())
print('Platform python compiler', platform.python_compiler())


#sys module
import sys
print(help(sys))
print(sys.version)
print(sys.platform)
print(sys.winver)
print(sys.getwindowsversion())
print(sys.modules)
print(sys.getrefcount("pritam"))
print(sys.path)
sys.stderr
sys.stdin
sys.stdout
