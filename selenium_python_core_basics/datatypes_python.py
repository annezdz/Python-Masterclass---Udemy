"""
Datatypes:

Numeric: int, float and complex
Text - str
boolean - bool
Sequence - list, tuple, range
map - dict
set - set and frozenset
binary - bytes, bytearray, memoryview


"""
import random
from cmath import pi

x = 100

y = 100j  # complex number

z = "Anne"

a = ['Anne', 'dudu', 'Edu']  # list
b = {'Anne', 'dudu', 'Edu'}  # set
# c=froozenset({'Anne', 'dudu', 'Edu'}) # froozenset
d = {'firstname': 'Anne'}  # dict
print(type(x))
print(type(y))
print(type(z))

print(type(a))
print(type(b))  # set
print(type(d))
print(isinstance(x, int))

print(random.randrange(1, 20))
print(10 > 5)
print(10 == 5)

print(pi)
print(type(pi))
print(5 % 2)
print(10 // 5)
