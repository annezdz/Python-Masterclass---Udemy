'''
Tuples
1 - It is used to store the sequence of IMMUTABLE objects
2 -Mostly all the others operations are similar to a List
'''

t1 = ('Anne', 12, 1.45)
print(type(t1))  # <class 'tuple'>

print(t1)

'''
Tuple slicing / Indexing

'''

t2 = (0, 1, 2, 3, 4, 5)
print(t2[0:])  # (0, 1, 2, 3, 4, 5)
print(t2[:])  # (0, 1, 2, 3, 4, 5)
print(t2[2:4])  # (2, 3)
print(t2[1:3])  # (1, 2)
print(t2[:4])  # (0, 1, 2, 3)

# delete

# del t2[3]#cannot delete function call
print(t2)

'''Tuple Operations

1 - Repetation
2 - Concatenation
3 - Membership
4 - Iterations'''

t3 = (1, 'Anne')
print(t3 * 2)
# concatenation
t4 = (2, 'Dudu')
print(t3 + t4)

print('Anne' in t3)
print('Anne' in t4)

for i in (1, 2, 3, 4):
    print(i)
