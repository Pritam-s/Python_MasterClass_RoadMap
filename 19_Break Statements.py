'''
1. Break Statement -
    In English, the word 'break' means interrupting.
    The break statement STOPS THE LOOP even if the while condition is satisfied.

    i.e. In short, it puts a break on the loop and doesn't allow to iterate further.


2. Defining break statement, break statement alters the normal functionality of the loops by terminating or exiting the loop containing it. The compiler then moves on to the code that is placed after the body of the loop. The syntax of break is only a single word, i.e., “break”.
'''

'''
#Example :-
#a. while(True) or while(1) - Infinite
i=0
while(True):
    print(f'The value of i is : {i}')
    i=i+1 #Infinite Loop (If you do not provide any increment to the i, it gets stuck in an infinite loop)
    if(i>10):
        break #Breaking the loop at 10.

#a) Output :-
The value of i is 1
The value of i is 2
The value of i is 3
The value of i is 4
The value of i is 5
The value of i is 6
The value of i is 7
The value of i is 8
The value of i is 9
The value of i is 10

'''
#b. While(i<100) 
i=1
while(i<=14):
    print(f'The value of i is {i}')
    i=i+1 #Remember to put the increment value or the loop continues forever.
    if(i==5):
        break

'''b) Output :-
The value of i is 1
The value of i is 2
The value of i is 3
The value of i is 4
'''