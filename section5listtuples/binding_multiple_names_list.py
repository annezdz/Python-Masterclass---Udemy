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
print(another_list)

a = b = c = d = another_list
print('Adding cream')
b.append('cream')
print(c)
print(d)
print(shopping_list)