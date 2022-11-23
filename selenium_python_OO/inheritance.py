'''

Inheritance:

Class A -> Base class / Parent Class - Single Level Inheritance

def add(self):

Class B -> Derived Class / Child Class

so from inheritance we can access members, properties and methods from the another class
PYTHON SUPORTS MULTYPLE INHERITANCE
A <--- B <--- C - Multilevel Inheritance
A   B
  C ->  Multiple Inheritance
'''


class AnimalParent():

    def ap(self):
        print('Inside Anima Parent class')

    def hello(self):
        print('Hello from Animal Parent class')


class Animal():
    name = 'Orangotango'

    def a(self):
        print('I am inside Animal Class')

    def hello(self):
        print('Hello from Animal class')


class Mamals(Animal, AnimalParent):
    def b(self):
        print('I am inside Mamals Class')


mam = Mamals()
mam.b()
mam.a()
print(mam.name)
mam.ap()
mam.hello() #Hello from Animal class class Mamals(Animal, AnimalParent): vai imprimir o que está herdando primeiro, no caso de haver o mesmo metodo em duas classes herdadas