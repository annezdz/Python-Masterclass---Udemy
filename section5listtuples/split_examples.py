panagram = 'The quick brown fox jumps over the lazy dog'

words = panagram.split()
print(words)

numbers = '9,223,333,999,666,222,877'
print(numbers.split(','))

generated_list = ['9', ' ',
                  '2', '2', '3', '']

values = ''.join(generated_list)
print(values)
values_list = values.split()
print(values_list)


#replace the values in place

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)

#create a new list

integer_values = []
for value in values_list:
    integer_values.append(int(value))
print(integer_values)