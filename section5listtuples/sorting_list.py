even = [2, 4, 6, 8]
odd = [1,3, 5, 7, 9]

#agrupar duas listas
even.extend(odd)
print(even)

#sort nao cria uma nova lista, ele ajusta a lista original
even.sort()
print(even)

another_even = even
print(another_even)
even.sort(reverse=True)
print(even)
print(another_even)

