'''
Polymorphism

1 - Operator overloading
2 - Method Overloading / Overriding
3 - Constructor Overloading - Overriding

1 - Operator overloading
<operand><operator<operand>

'''


class OperatorOverloading:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):  # (obj1 + obj2) mesma coisa o __add__
        total_pages = self.pages - other.pages
        return total_pages


obj1 = OperatorOverloading(10)
obj2 = OperatorOverloading(5)

print(obj1 + obj2)

'''class A:

     def add():
         print('Addition of X and Y')
    
    class B(A):
      
      def add():
         print('Different definition') #Overriding
    
2 . method Overloading

In Python method Overloading is not possible
Constructor overloading is not possible in Python
'''


class MethodOverloading:

    def __init__(self):
        print('inside constructor')

    def __init_(self, name):
        self.name = name
        print('Inside constructor')

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# obj3 = MethodOverloading()
# print(obj3.add(10, 20))
# print(obj3.add(10, 20, 30)) #TypeError: MethodOverloading.add() missing 1 required positional argument: 'c'
# obj4 = MethodOverloading('Anne')
