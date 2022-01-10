'''
1. If_Else & Elif Conditionals :-

    a) Definition -
       "If else and elid statement can be defined as a multiway decision take by our program due to ther cerain conditions in our code."

    b) What is 'if & else' ?
        'if and else' are known as decision-making statements for our program. They are very similar to the decision-making we apply in our day-to-day life that depends on certain conditions.

    c) What is 'elif' ?
        In English the word 'Elif' means - honest. 
        But as same as in other programming languages having 'else-if', the word 'elif' is same as 'else-if'.  


2. Working of the if-elif-else :-

    a) Our compiler will execute the 'if' statement ot check whether it is true or false: now if the 'if' statement is true, the compiler will execute the code in the 'if' section and skip the bunch of code written after it i.e. the 'elif' and 'else' section.

    b) But, If the 'if' condition is false. Then the compiler will move towards the elif section and keep on running the code until it finds a true statement (there could be multiple elif statements).

    c) If none of the 'elif' statements turns out to be true, the compiler will simply execute the 'else' condition.


3. Must have in if-elif-else :-

    a) An 'if' statement is a must because without an if, we cannot apply 'else' or 'elif' statements. 
    
    b) On the other hand else or else if statement is not necessary because if we have to check between only two conditions, we use only 'if and else'.

    c) And even though if we require code to run only when the statement is true and do nothing if it returns false, at such times the 'else' statement is not required at all.


4. Technical issues related to the working of 'Decision making statements' :-

    a) There is no limit to the number of conditions that we could use in our program. We can apply as many 'elif' statements as we want. But we can only use one 'else' and only one 'if' statement.

    b) We can use nested if statements.

    c) Decision statements can be written using logical coditions :- 
        * Equal to ==
        * Not equal to !=
        * less than <
        * greater than >
        * greater than equal to >=
        * less than equal to <=

    d) We can also use :-
        * Boolean
            Or
        * custom-made conditions too


NOTE :-

    * As we know 'if' is necessary, but incase we have a very large program and suppose it's required to remove the 'if' part of the code. 
    At such times, we can use "pass" in place of the code of the if section.

    * Using continue passes for the next iteration of the for loop
    Using pass just does nothing.

    So when using continue the print won't happen (because the code continued to next iteration)
    And when using pass it will just end the if peacefully (doing nothing actually) and do the print as well.
              
'''


# Example :-

var1 = 69
var2 = 420
var3 = int(input("Please enter a number :-\n"))

if var3>var1 and var3>var2:
    print("The number entered is greater than 69 and 420")
elif var3>var1 and var3<var2:
    print("The number entered is greater than 69 but lesser than 420")
else:
    print("The number is smaller than both 69 and 420")

# O/P :-

''' 
Please enter a number :-
18
The number is smaller than both 69 and 420

Please enter a number :-
80
The number entered is greater than 69 but lesser than 420

Please enter a number :-
500
The number entered is greater than 69 and 420

'''