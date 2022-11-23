pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)
print(letter)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
#aqui criamos uma lista ordenada
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

#aqui retorna none pois nao podemos chamar o sort() em uma nova lista
another_list_sorted = numbers.sort()
print(another_list_sorted)
# aqui ordenamos a lista original
numbers.sort()
print(numbers)

# usando o key=str.casefold o T nao aparece mais no inicio
missing_letter = sorted("The quick brown fox jumps over the lazy dog", key=str.casefold)
print(missing_letter)

names = ['Graham',
         'John',
         'terry',
         'eric',
         'michale',
         'ana']

names.sort(key=str.casefold)
print(names)