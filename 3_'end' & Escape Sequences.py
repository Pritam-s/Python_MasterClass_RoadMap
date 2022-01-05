'''
1. 'end' argument.
2. Escape Sequence

end argument -
a) 'end' arguments allows us to put something at the end of the line after it is printed.
b) In simple words, it allows us to continue the  line with "" or ',' or anything we want to put insdie these quotes of the end.
c) It simply joins two different print statements using some string or even by space.
'''
print("Pritam is a good human being", end=".^@&*")


'''
Escape Sequence - 
a) An Escape sequence character in python is a sequence of characters that represents a single character.
b) It doesn't represent itself when used inside string literal or character.
c) It is composed of two or more characters starting with backslash \ but acts as a single character. eg - \n depicts a new line character.

Escape Sequences	Description 
\n 	Inserts a new line in the text at the point.

\\	Inserts a backslash character in the text at the point.

\"	Inserts a double quote character in the text at that point.

\'	Inserts a single quote character in the text at that point.

\t	Inserts a tab in the text at that point.

\f	Inserts a form feed ln the text at that point.

\r	Inserts a carriage return in the text at that point.

\b	Inserts a backspace in the text at that point.

'''
print("\nThis world\n\tis so\t beautiful")
