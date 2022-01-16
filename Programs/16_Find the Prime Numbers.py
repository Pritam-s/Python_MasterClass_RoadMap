#Prime Numbers 

num = int(input('Please enter the number to find the prime number '))
start = 1

for items in range(start, num+1):
    count = 0
    for row2 in range(start, num+1):
        if (items%row2 == 0):
            count = count+1
    if (count == 2):
        print(items)
