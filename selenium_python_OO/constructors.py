'''
Constructors
They are called as a first function of the class

syntax: __init__()

All classes have this fucntion which is always executed when the class is being initiated or an object
of the class is created

PYTHON DONT HAVE OVERLOADING CONSTRUCTOR
'''


class Practice:

    def __init__(self):
        print('Inside constructor')

    def add(self):
        print('Adding something')


a = Practice()
a.add()


class Emp:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f'Name is {self.name}')
        print(f'ID is {self.id}')


e = Emp('Anne', 2)
e.display()
