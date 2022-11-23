'''
Functions:
1 - Block of code used to perform a specific action
2 - Reusable block
3 - Can have parameters
4 - Collection of multiple functions create a program
5 - Pre defined functions print() sort() etc
def function_name():
    statement / code to be executed
'''


def print_my_name():
    print('My name is Anne')


print_my_name()


def print_my_name_as(name):
    # print("My name is " + name)
    return "My name is " + name


print_my_name_as('Anne')

name = print_my_name_as('Anne')
print(name)


def get_user_details(name, age, salary):
    return 'Name is - ' + name + ' Salary is: ' + str(salary) + ' Age is ' + str(age)


print(get_user_details('Anne', 37, 500))

'''Types of arguments:
1 - Required arguments
2 - Keyword arguments
3 - Default arguments
4 - Variable lenght arguments'''


def req_arguments(a, b):
    print(a + b)


# req_arguments(10) TypeError: req_arguments() missing 1 required positional argument: 'b'
# req_arguments(10, 20, 30) TypeError: req_arguments() takes 2 positional arguments but 3 were given
req_arguments(10, 20)

# 2 - Keyword arguments
# get_user_details(name1 = 'Dudu', salary1 = 200, age1 = 2) TypeError: get_user_details() got an unexpected keyword argument 'name1'
get_user_details(name='Dudu', salary=200, age=2)


# 3 - Default arguments

def def_argument(name, school='Oxford'):
    print('Name - {}'.format(name))
    print('School - {}'.format(school))


def_argument('Anne')
def_argument('Anne', 'Thiago Anzini')

get_user_details(name='Rahul', salary='1000', age=37)


def var_argument(school, *name):
    print(school)
    for i in name:
        print(i)


var_argument('Anne', 'Cory', 'Tom', 'Silvia')
print('**************************')
var_argument('Anzini', 'Anne', 'Cory', 'Tom', 'Silvia')
print('**************************')
var_argument('Anzini', 'Anne', 'Cory', 'Tom', 'Silvia', 12)

