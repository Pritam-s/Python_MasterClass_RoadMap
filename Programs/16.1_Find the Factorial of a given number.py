#Write a Program to find the Factorial a of given number.

num = int(input(f"Please enter a number to find it's factorial - "))
start = 1
fact = 1

for items in range(start, num+1):
    fact = fact * items
print(f'The factorial of the number {items} is {fact}.')