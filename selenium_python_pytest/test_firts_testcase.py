import pytest


# Before class
def setup_module(module):
    print('Creating DB Connection')


# After class
def teardown_module(module):
    print('Closing DB Connection')


# equivalente ao Before do Java
def setup_function(function):
    print('launching browser')


# equivalente ao After do Java
def teardown_function(function):
    print('Quitting the browser')


def test_do_login():
    print('Executing login test')


def test_user_reg():
    print('Executing user reg test')
