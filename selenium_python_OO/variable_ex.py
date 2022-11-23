class Dog:
    legs = 4 #global variable, static variable

    def __init__(self):
        self.name = 'Milo'
        self.color = 'brown'


d1 = Dog()
d2 = Dog()

d2.color = 'White'
d2.name = 'Bruno'

print(d1.name, d1.color, d1.legs)
print(d2.name, d2.color, d2.legs)

print(d1.name, d1.color, Dog.legs)
print(d2.name, d2.color, Dog.legs)
