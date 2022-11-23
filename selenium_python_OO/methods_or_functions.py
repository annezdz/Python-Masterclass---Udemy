'''

3 types of methods / functions

1 - Instance Method - use to access instance variable of the class
2 - Class method - use to access static of the class
3 - Static Method - standalone method

'''


class Dog:
    legs = 4  # global variable, static variable

    def __init__(self):
        self.name = 'Milo'
        self.color = 'brown'

    def getDogName(self):
        print(self.name)

    @classmethod  # para chamarmos um método da classe precisamos colocar essa anotação
    def getLegsCount(cls):
        print(cls.legs)

    @staticmethod  # para um método ser estático precisamos dessa anotação
    def generalInformation():  # static method
        print('Beware of Dogs')


d1 = Dog()
d1.getDogName()  # Milo

d1.getLegsCount()

Dog.getLegsCount()  # Dog.getLegsCount() missing 1 required positional argument: 'cls'

Dog.generalInformation()
