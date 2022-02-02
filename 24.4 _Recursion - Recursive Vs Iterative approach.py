'''
1. What is Recursive Vs Iterative approach :-

    In pyhsical world - 
        A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively. 
    
    In programming world -
        "Recursion occurs when a function calls itself."

    Mostly both recursion and iteration are used in association with loops, but both are very different from each other. In both recursion and iteration, the goal is to execute a statement again and again until a specific condition is fulfilled. An iterative loop ends when it has reached the end of its sequence; for example, if we are moving through a list, then the loop will stop executing when it reached the end of the list. But in the case of recursion, the function stops terminating when a base condition is satisfied.



2. Recursion (LIFO data structure) :-

    There are two essential and significant parts of a recursive function. The first one is the base case, and the second one is the recursive case. In the base case, a conditional statement is written, which the program executes at the end, just before returning values to the users. In the recursive case, the formula or logic the function is based upon is written. A recursive function terminates to get closer to its base case or base condition.

    in recursion that if the base case is not met in the call, the function will repeatedly run, causing the system to crash.

    In case of recursion, each recursive call is stored into a stack until it reaches the base condition, then the stack will one by one return the calls printing a series or sequence of numbers onto the screen. 
    
    NOTE :- 
        It is worth noting that stack is a LIFO data structure i.e., last in first out. This means that the call that is sent into the stack at the end will be executed first, and the first one that was inserted into the stack will be executed at last.



3. Recursion Vs Iteration comparison :-

    Recursion can only be applied to a function, while iteration can be used for any number of lines of code, we want to repeat.

    Lesser coding has to be done in case of recursion than iteration.

    Back tracing or reverse engineering in case of recursion can be difficult.

    In the case of recursion, if the condition is not met, the system will repeat a few times and then crash while in case of iteration it will continue to run endlessly.

    Even though less coding has to be written in case of recursion, it is still slower in execution because the function has to be called again, and again, storing data into the stack also increases the time of execution.



4. Inshort, Disadvantages of Recursion
    
    Sometimes the logic behind recursion is hard to follow through.
    
    Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    
    Recursive functions are hard to debug.


5. Conclusion :-

    For smaller programs where there are lesser lines of codes, we should use a recursive approach and in complex programs, we should go with iteration to reduce the risk of bugs.
'''



# 1 Example 
def countdn1(n):
     print(n)
     if n == 0:
        return # Terminate recursion
     else:
        countdn1(n - 1)
countdn1(10)


#CWH - Find the nth Fibonacci number
# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


number = int(input("Enter then number"))
print(fibonacci(number))



# Python program to display the Fibonacci sequence
# Print all the Fibonacchi numbers till nth number. Using Recursion :-
nterms = int(input("Please enter a number : "))
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for items in range(nterms):
       print(recur_fibo(items))

