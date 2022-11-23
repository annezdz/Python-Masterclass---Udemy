empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

#criando uma lista concatenada de outras listas

numbers = even + odd
print(numbers)


sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted('432985617')
print(digits)

digits_list = list('432985617')
print(digits_list)
## varias maneiras de criar copias de listas
# more_numbers = list(numbers)
# print(more_numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)

print(numbers is more_numbers) #False não são a mesma lista
print(numbers == more_numbers) #True são listas iguais