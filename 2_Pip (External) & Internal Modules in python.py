'''
There are 2 types of modules in python - 
1. Internal Modules
2. External Modules

Internal Modules - They are built-in modules which are already installed & present in Python. 
eg :- Math, OS, Calendar, random, etc.
eg :- import Math, import OS, etc.



External Modules - These are modules which are not pre-installed and are not available built-in inside python.
eg :- Flask, Pandas, TensorFlow, NumPy, etc.

a. We use Pip to install the external modules.
b. we simply open the CMD or Powershell and just write - pip install flask, pip install pandas, etc. and the module will be installed in our computer. ('we can also intall the module in a particular folder by opening cmd or powershell in that particular folder and use pip for that folder)
c. we then simply import that module in the same way we import the internal modules.
eg :- import flask, import pandas, etc


'''

# Internal modules
import math
print(math.asin(0.60)) #asin only takes number between -1 to 1


# External modules
# import flask
