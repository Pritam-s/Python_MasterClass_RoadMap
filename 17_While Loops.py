'''
1. While Loop -

    "A while loop in python runs a bunch of code or statements again and again until the given condition is true. When the condition become false, the loop  terminates its repetition."


2. Syntax for 'while' loop -

        while codition_is_true:
            Code inside the loop body  


3. Usecase for 'while' loop - 

      a) A 'while' statement runs until the condition becomes false.

      b) A 'while' statement is used for areas whereas the number of iterations are unknown.
   
'''



'''
#Example -1
i = 1

while (i<=20):
    print(i)
    i = i+1

#O/P
1
2 
3 
4 
5 
6 
7 
8 
9 
10
11
12
13
14
15
16
17
18
19
20 
'''


#Example 2 - with break statement
'''
i = 1 
while i<10:
    print(i)
    if i == 6:
        break
    i=i+1

#The break statement stops the loop even if the while conndition is true. So, here the loop is stopped at number 6.

#O/P - 
1
2
3
4
5
6
'''

#Example 3 - with continue statement
i = 0
while i<10:
    i=i+1
    if i == 6:
        continue
    print(i)

#The continue statement stops the current iteration and continue with the next. So, here the number 6 is skipped and the next iteration is continued.

#O/P -
1
2
3
4
5
7
8
9
10
