class Student:
    std = "10th"
    div = "B"
    age = 16

Pritam = Student()
print(f'Age of Pritam is {Pritam.age}.')
print(f'Division of Pritam is {Pritam.div}.')

Vicky = Student()
print(f'Age of Vicky is {Vicky.age}.')

Vicky.age = 25
print(f'New Age of Vicky is {Vicky.age}.')

print(Student.__dict__)
Student.age = 30
print(Student.__dict__)
print(f'New Age of Student is {Student.age}.')

