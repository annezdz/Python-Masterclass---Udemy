'''
Datatypes
1 - List
2 - Tuple
3 - Dictionary

List - Its just a consecutive collection of related items / words
Represents a group of values as a single entity, order is very important
It allows duplicated values as well
it is represented by square bracket []
values are separated by commas

'''

a = []  # empty list
b = [1, 2.3, 'Anne', True, 3 + 2j]
print(type(b))  # <class 'list'>
print(b)

# order is preserved
print(b[2])

# List allow duplicated values
b = [1, 2.3, 'Anne', True, 3 + 2j, 'Anne']
print(b)

# List us mutable in nature
b.append('Cory')
print(b)

emp = ['Anne', 102, 'Brasil']
dep1 = ['IT', 10]
dep2 = ['Elec', 11]

print(f'Name is {emp[0]}, Department is {emp[1]} and country is `{emp[2]}')

'''

List slicing

'''

c = [0, 1, 2, 3, 4, 5, 6]
print(c[0:])  # [0, 1, 2, 3, 4, 5, 6]
print(c[:])  # [0, 1, 2, 3, 4, 5, 6]
print(c[2:4])  # [2, 3]
print(c[:4])  # [0, 1, 2, 3]

# updating values in list

d = [1, 2, 3, 4, 5, 6]
print(d)
d[3] = 7
print(d)
d[1:4] = ['Anne', 'Dudu', 10]
print(d)

# delete

del d[4]
print(d)

e = ['a', 'e', 'o', 'i', 'u']
print(e)
e.sort()
print(e)

'''List operations
1 - repetition operation
2 - Concatenation operation
3 - Membership operation
4 - Iterations
5 - Length function'''

#Repetition
l1 = [1, 2, 3, 'Anne', True]
l1 = l1 * 2
print(l1 * 2)

#concatenation

l2 = [5, 6, 7, 'Dudu', False]
print(l1 + l2)

print('Edu' in l1) #false
print('Dudu' in l2) #true

for i in l1:
    print(i)

#tamanho
print(len(l1))
print(len(l2))

l3 = [1, 99, 2, 3, 88]
print(max(l3))
print(min(l3))

string = 'Eduardo'
print(list(string))#['E', 'd', 'u', 'a', 'r', 'd', 'o']