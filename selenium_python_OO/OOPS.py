'''

OOPS Concept /Prodecural language
1 - Classes
2 - Objects
3 - Encapsulation
4 - Abstraction
5 - Inheritance
6 - Polymorphism

What is a class?

1 - A class can be defined as a blueprint or template woch describes the state / behavior of it's object

class<classname>:
    statements

    self - a key word through which we cab access the attributes and methods of a class in Python
    A instance of that class
'''


class Human:
    eyes = 'blue'
    nose = 'large'

    def eyes_function(self, color):
        print(f'This is a function to see - {color}')

    def nose_function(self, size):
        print(f'This is a function to smell - {size}')

    def ear_function(self, color):
        print(f'This is a function to hear - {color}')


# a = Human()
# a.eyes_function()
# a.ear_function()
# a.nose_function()
# print('****************')

b = Human()
b.eyes_function('Black')
b.ear_function('White')
b.nose_function('Large')