numbers = [
]

count = 0
while count < 3:
    numbers.append(int(input('Digite numero {} :'.format(count + 1))))
    count += 1
print(numbers)
for index in range(len(numbers)):
    total = numbers[0] + numbers[1] - numbers[2]
print(total)