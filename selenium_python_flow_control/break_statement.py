'''
Break and continue

'''

for i in range(10):
    if i == 7:
        print('Executing break')
        break
    print(f'Printing the value as {i}')
print('Outside the for loop')

print('Print odd numbers')

for i in range(10):
    if i % 2 == 0:
        print(f'Number {i} is even')
        continue
    print(f'Odd numbers is {i}')

print('--------------')
for i in range(10):
    if i == 7:
        print(i)
        break
    elif i == 5:
        continue
    print(i)

cart = [10, 20, 30, 40, 50, 550, 70]
for item in cart:
    if item > 500:
        print('This item is not allowed')
        continue
    print(item)
else:
    print('All items are successfully processed..')
