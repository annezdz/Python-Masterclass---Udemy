
# método é o mesmo que funcao, porem é vinculado a um objeto, ou seja,
# precisamos de um objeto para chamar o método
# exemplos de funcoes sao o max, min, len, count

shopping_list = [ 'milk',
                  'pasta',
                  'eggs',
                  'bread',
                  'rice']

another_list = shopping_list
print(id(another_list))
print(id(shopping_list))

shopping_list += ['cookies']
print(shopping_list)
print(id(another_list))
print(id(shopping_list))