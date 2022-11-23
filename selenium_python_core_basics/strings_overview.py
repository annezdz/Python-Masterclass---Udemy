print(type('This is a String'))

a = 'Welcome to W2A'
print(a)

b = 'Welcome to W2A'
print(b)

e = 'Hey,' \
    'my name is ' \
    'Anne'

print(e)

g = '''
Hey,
my name is
Anne'''

print(g)

print("This is Rahul's \"New\" house")
name = 'Rahul'
print(name[0])

#slicing
print(name[1:4:2])
print(name[::2])

#reverse string
print(name[::-1])
#tamanho string
print(len(name))

abc = '   Hello, Anne   '
print(abc.strip()) # equivale ao trim
print(name.lower()) #minusculo
print(name.upper())#maiusculo

b = abc.split(', ')
print(b)
print(b[0].strip())

#concatenacao

ab = 'Hi'
cd = ' Way2Automation'
print(ab + cd)

# print(10 + '10') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('10' + '10')

a = '10' * 4
print(a)

print('ba' + 'na' * 2)

city = ' New Delhi'
print('Hey, I live in' + city)

age = 35
id = 10

#f-string
print(f'Hey, I live in {city} , My age is {age} and id is {id}')

#format
print('Hey, I love in {} and my age is {} and id is {}'.format(city, age, id))

#%
print('Hey, I love in %s and my age is %d and id is %f'%(city, age, id))