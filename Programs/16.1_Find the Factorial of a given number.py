#Write a Program to find the Factorial a of given number.

num = int(input("Please enter a number to find it's factorial - "))
start = 1
fact = 1

for items in range(start, num+1):
    fact = fact * items
print(f'The factorial of the given number {items} is {fact}.')

# O/P :-
'''
#1)
Please enter a number to find it's factorial - 4
The factorial of the given number 4 is 24.

#2)
Please enter a number to find it's factorial - 5
The factorial of the given number 5 is 120.

#3)
Please enter a number to find it's factorial - 6
The factorial of the given number 6 is 720.
'''