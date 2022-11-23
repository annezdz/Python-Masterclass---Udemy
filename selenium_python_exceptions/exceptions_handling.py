'''

Exceptions / Errors

exceptions are simply disruptions to the flow of program

'''

# print('Result is = ' .format(c)) //ZeroDivisionError: division by zero

'''


Try and Except block

try:
    {----}
except:
    {----}
    
'''

try:
    a = int(input('Enter the value for first number: '))
    b = int(input('Enter the value for second number: '))

    c = a / b

    print('Result is = {}'.format(c))

except (ZeroDivisionError, ValueError):
    print('Please enter a valid number')
else:
    print('This is inside else block')
finally:
    print('I am always executed')
# print('This is outside Try Except block')


'''
Python exception Hierarchy
Base exception
1 - Exception 
    a - attribute exception / error
    b - arithmetic exception / error
    c - EOF exception (end of file)
    d - Name exception
2 - System Exit
3 - Generator Exit
4 - Keyboard Interrupt

'''