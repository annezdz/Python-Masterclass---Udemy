#Write a small program that assigns the value 5 to one variable, called x, and the value 7 to another, called y.
x = 5
y = 5

if x < y:
    print('{0} is greater than {1}'.format(y, x))
elif x > y:
    print('{0} is smaller than {1}'.format(y, x))
else:
    print('{0} equals {1}'.format(y, x))
