"""
1 - Arithmetic
2 - Comparison
3 - Equality
4 - Logical
5 - Bitwise
6 - Shift
7 - Assignment
8 - Ternary
9 - Membership
10 - Identity

"""

# exponencial (**) floor division (//)

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# Comparators

print(a > b)
print(a < 5)
print(a >= b)
print(a <= b)

s1 = 'Cat'.casefold()
s2 = 'Dog'.casefold()

print(s1 > s2)
print(s1 >= s2)
print(s1 < s2)
print(s1 <= s2)

# retorna numero unicode
print(ord('C'))
print(ord('c'))

print('apple' > 'apple')
print('apple' >= 'apple')
print('apple' < 'apple')
print('apple' <= 'apple')

# relational operating chaine
print(10 < 20 < 30 < 40)

# equality operators

c = 10
d = 20

print(c == d)
print(c != d)
print(1 == True)  # T
print(0 == True)  # F
print(0 == False)  # T
print(10 == 10.0)  # T
print('Way2Automation' == 'Way2Automation')  # T

# Logical Operators

print(True and True)
print(1 and 0)

'''
if the value x False then the result is the value x, else the value is y '''

print(10 and 20)
print(0 and 20)

print(10 or 20)
print(0 or 10)

# username = input('Enter the username')
# password = input('Enter the password')
# if username == 'way2automation' and password == 'test':
#     print('Valid user')
# else:
#     print('Invalid user')

print(not True)
print(not False)

'''

Bitwise Operators
Bitwise And &
Bitwise Or |
Bitwise XOR ^
Bitwise complement 

'''
print(bin(16))
print(bin(18))
print(16 & 18)
print(16 | 18)
print(16 ^ 18)
print(~(-3))

# shift operators
# left (<<)
# right(>>)

print(10 << 2)
print(10 >> 2)

# assignment operator
#   = , += , -= , *=

x = 20
print(x)
x += 10
print(x)

x *= 2
print(x)
x -= 10
print(x)
#Python does not suport increment decrement operators
# print(x++)

'''

Ternary Operators

It is a conditional operator
There us no specific keyword for ternary operator
var = First value if condition else second value

'''

a = 10
b = 20
c = 30 if a > b else 40
print(c)

a = int(input('Enter a = '))
b = int(input('Enter b = '))
minimo = a if a < b else b
print(minimo)


'''Identity operators
1 is
2 is not
'''

a = 10
b = 10

print(a is b)
print(a is not b)

''' 
Membership operator

'''


a = [10, 20, 30, 55, 'abc']

print(10 in a)
print(20 not in a) #f
print(21 not in a) #t
print(22 in a)#f