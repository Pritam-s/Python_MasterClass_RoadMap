#Prime Numbers 

num = int(input('Please enter the number to find the prime number till that number - '))
start = 1

for items in range(start, num+1):
    count = 0
    for row2 in range(start, num+1):
        if (items%row2 == 0):
            count = count+1
    if (count == 2):
        print(items)


# O/P :-
'''
#1)

Please enter the number to find the prime number till that number - 40
2
3
5
7
11
13
17
19
23
29
31
37

#2)

Please enter the number to find the prime number till that number - 10
2
3
5
7

'''
