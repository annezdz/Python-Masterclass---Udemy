'''Dictionary
Key and value pair
1 - Key - Number, String, Tuples
2 - Value - Python Object'''

D1 = {
    'Name': 'Anne',
    'Age': 37
}

print(type(D1))
print(D1)

d2 = {
    'Name': 'Edu',
    'Age': 44,
    'Salary': 1000,
    'Organization': 'Teste',
    'Is_Married': True
}

# print('Name - {}'.format(d2['Name']))
# print('Age - {}'.format(d2['Age']))
# print('Salary - {}'.format(d2['Salary']))
# print('Organization - {}'.format(d2['Organization']))
# print('Is married - {}'.format(d2['Is_Married']))
#
# d2['Name'] = input('Enter name : ')
# d2['Age'] = input('Enter age : ')
# d2['Salary'] = input('Enter salary : ')
# d2['Organization'] = input('Enter organization : ')
# d2['Is_Married'] = input('Enter is married : ')

print(d2)

# delete

del d2['Is_Married']
print(d2)

# Iterate a dictionary

# printing all key values

for a in d2:
    print(a)

# printing all values
for b in d2:
    print(d2[b])

print('----Values --------')
for c in d2.values():
    print(c)

print('----Keys and values--------')
for c in d2.items():
    print(c)

item = {
    'fruits': ['Apple', 'Mango', 'Banana'],
    'price': 100,
    'size': 10.5
}

print(item['fruits'])
print(item['fruits'][0])

item1 = {
    'location': 'India',
    'fruits': {'name': 'apple', 'price': 100}
}
print(item1['fruits'])
print(item1.get('fruits'))
print(item1.get('fruits').get('price'))

print(type(item1.get('fruits')))
print(item1['fruits']['name'])

#lenght
print(len(item1))

print(item1.keys())#dict_keys(['location', 'fruits'])