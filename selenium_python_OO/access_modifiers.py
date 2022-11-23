'''

public,

protected - _var , def _method()


, private - __var , def __method()


default é public
'''


class Car:
    public_var = 9
    _protected_ar = 10
    __private_var = 11

    def __init__(self):
        print('Inside Car constructor')

    def public_method(self):
        print('calling public method')

    def _protected_method(self):
        print('calling protected method')

    def __private_method(self):
        print('calling private method')

