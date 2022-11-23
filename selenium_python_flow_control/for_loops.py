'''
Iterative statements
1 - For loop
2 - While loop
'''

sequence = 'Anne'
i = 0
for x in sequence:
    print('The character present at {}. index {}'.format(i, x))
    i += 1

for x in range(10):
    print('Way2Automation')

for x in range(1, 11):
    print(x)

for x in range(2, 30, 3):
    print(x)

n = int(input('Enter the number: '))
for i in range(1, 11):
    print(n, ' * ', i, ' = ', n * i)


List = eval(input('Enter the numbers for addition: '))

total = 0
for x in List:
    total += total + x
print('The sum is : ', total)

string = 'My name is Anne'
s = string.split(" ")
for x in s:
    print(x)