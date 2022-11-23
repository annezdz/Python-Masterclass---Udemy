"""
If statement -
"""

a = 20
b = 30

if a > b:
    print(a)
    print('A is greater')
else:
    print(b)
    print('B is greater')

mark = int(input('Enter marks: '))
section = input('Enter the section: ')
if mark == 100:
    if section == 'A':
        print('Brilliant class')
    grade = 'A+'
    print(grade)
elif 80 < mark < 100:
    print('B')
elif 60 < mark < 80:
    print('C')
else:
    print('Student is failed')
