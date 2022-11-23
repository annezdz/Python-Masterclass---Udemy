i = 0
while i < 10:
    print('Hello ', i)
    i += 1


#sum of first numbers
n = int(input('Enter a number: '))
sum = 0;
i = 1
while i <= n:
    sum += sum + i
    i += 1

print(f'Sum is {sum}')