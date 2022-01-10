'''
1. For Loops In Python :-

    a) "Loop is also just a programming function that iterates a statement or a number of statements based on specific boundaries under certain conditions."

    b) The statement that the loop iterated must be present inside the body of the loop.

    c) Iteration means going through some chuck of code again and again. 
    In English language the word Iteration means - The act of repeating again and again.


2. Uses of Loops :-

    a) Loop is useful in areas whereas lot of data has to be printed on the screen, manually doing this work would require alot of time and efforts.

    b) Loops are also helpful in searching date from lists, dictionaries, tuples, sets.


3. Why do we use Loops ?

    * Complex problems can be simplified using loops.

    * Less amount of code required for our program.

    * Lesser code so lesser chance or error.

    * Saves a lot of time and effort.

    * Can write code that is practically impossible to      write.

    * Searching and sorting algorithms that require too many iterations can be simplified using loops.


4. Advantages of Loops.

    * The reusability of code is ensured.

    * We do not have to repeat the code, again and again, we just have to write in one time.

    * We can transverse through data structures like list, dictionary, tuples.

    * We apply most of the findings algorithms through loops.

'''


#Example_1
list1 = [1,343,543534,623,234,64,"Pritam", "Hello", 545.13,"N250", True, None, {"timepass", "Value", 43, 78},(float, str,int)]

for items in list1:
    if str(items).isnumeric() and items>300 :
        print(items)
'''
#O/P_1 -
343
543534
623 
'''



#Example_2
list2 = [["Pritam","RTR 180", 2015], ["Awdhoot","Pulsar 220", 2012], ["Anirudha","NS 200", 2014], ["Darsh","RTR 200", 2021]]

# 2a
for names in list2:
    print(names)
    print(type(names))

'''
# O/P - 2a
['Pritam', 'RTR 180', 2015]
<class 'list'>
['Awdhoot', 'Pulsar 220', 2012]
<class 'list'>
['Anirudha', 'NS 200', 2014]   
<class 'list'>
['Darsh', 'RTR 200', 2021]     
<class 'list'>
'''

# 2b
for names, bikes, year in list2:
    print(names, bikes, year)

'''
# O/P - 2b
Pritam RTR 180 2015
Awdhoot Pulsar 220 2012        
Anirudha NS 200 2014
Darsh RTR 200 2021
'''

#Example_3
num1 = ("Hello", "World", "How are you", 234,4234.223, 65, 34, 4231, 9869, True, None, str, float, tuple, dict)

#3a
for items in num1:
    if str(items).isnumeric() and items>200:
        print(items)

'''
# O/P - 3a :-

234
4231
9869
'''

#3b
sets2 = set(num1)

for items in sets2:
    print(items)

'''
# O/P - 3b :-

65
34   
Hello
True 
4231 
None 
<class 'str'>
234
4234.223
<class 'float'>
9869
<class 'tuple'>
World
How are you
<class 'dict'>
'''

    