# Python program to display the Fibonacci sequence

# Using for loop 
nterms = int(input("How many terms ? "))
n1, n2 = 0,1
count = 0

if nterms <=0:
    print('Please enter a positive integer')
elif nterms == 1:
    print(f'Fibonacci sequence upto {nterms}')
    print(n1)
else:
    print(f'Fibonacci sequence upto {nterms} terms : ')
    for items in range(n1,nterms):
        if count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth



# Using while loop
nterms = int(input("How many terms ? "))
n1, n2 = 0,1
count = 0

if nterms <=0:
    print('Please enter a positive integer')
elif nterms == 1:
    print(f'Fibonacci sequence upto {nterms}')
    print(n1)
else:
    print(f'Fibonacci sequence upto {nterms} terms : ')
    while(count < nterms):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count+1



# Using Recursion :-
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