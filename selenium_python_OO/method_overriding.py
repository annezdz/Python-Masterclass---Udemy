'''
Method overriding



'''


class MethodOverridingBase:

    def __init__(self):
        print('Base class constructor')

    def a(self):
        print('Inside Base class')


class MethodOverridingDerived(MethodOverridingBase):

    def __init__(self):
        super().__init__()  #chamando o construtor da classe pai e imprimindo o construtor da classe filha
        print('Child class constructor')


    def b(self):
        print('Inside derived class')

    # def a(self):
    #     print('Inside derived class')  #Overriding

    def a(self):
        super().a() #vai chamar o método da classe Pai e tambem imprimir o método override
        print('Inside derived class')


obj1 = MethodOverridingDerived()
obj1.a()
