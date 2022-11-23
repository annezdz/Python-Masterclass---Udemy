'''
Imutaveis: int, float, bool, str, tuple, frozenset, bytes
Mutáveis:
'''

# result = True
# anoter_result = result
#
# # retorna o id do objeto (memory address)
# print(id(result))
# print(id(anoter_result))
#
# result = False
# print(id(result))

result = 'Correct'
another_result = result
print(id(result))
print(id(another_result))

result += ' ish'
print(id(result))
print(id(another_result))