'''
1. Time module and datetime module with different classes.

    Uses of time modules:

           a) In games where missions depend on a certain time limit.

           b) To check the execution time a certain part of our code is taking.

           c) To print the date or local time onto the screen
           
           d) To suspend the execution of python thread.
        
           e) To measure the efficiency of the code.


2. We use time modules to handle time related tasks.

3. We also use time module to calculate and record the execution time of a program. The execution time of a program is defined as "the system's time to execute the task".

4. Some important time functions :- 

    a) time.time()
    b) time.sleep()
    c) time.localtime()
        more in below examples ....
'''



# Example 1 - Displaying the local Date and Time.
import time
#print(dir(time))

localtime = time.asctime(time.localtime(time.time())) 
print(localtime) #O/P- Mon Jan 31 18:31:09 2022

localtime2 = time.asctime() 
print(localtime2) #O/P- Mon Jan 31 18:31:09 2022

localtime3 = time.ctime() 
print(localtime3) #O/P- Mon Jan 31 18:31:09 2022

time4 = time.strftime("%d/%m/%y, %H:%M:%S %p, %A %B %Y") 
print(time4) #O/P - 31/01/22, 18:33:08 PM, Monday January 2022



# Example 2 - time.sleep() in a for loop and execution time calculation of for loop.
import time
initial_time = time.time()
print(initial_time)

for items in range(1,11):
    print(items)
    time.sleep(0.50)
print(time.time() - initial_time)


# Example 3 - 'date class' of 'datetime module'
from datetime import date
d1 = date.today()
print(d1) # O/P - 2022-01-31


# Example 4 - 'datetime class' of 'datetime module'
from datetime import datetime 
d2 = datetime.now() 
print(d2) # O/P - 2022-01-31 19:03:09.957012


