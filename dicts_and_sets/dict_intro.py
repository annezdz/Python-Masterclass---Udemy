vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph'
}

#usando a chave como indice
my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

#usando o método get

learner = vehicles.get('er5')
print(learner)


#adicionando um novo dict
vehicles['starfighter'] = 'Lockheed F-104'
vehicles['learjet'] = 'Bombardier Learjet 75'
vehicles['toy'] = 'glider'


#removendo um registro

del vehicles['dream']

# del vehicles['f1']
# pop com um valor default nao quebra o codigo e tenta deletar a chave passada.
# caso ela nao exista, devolve none
vehicles.pop('f1', None)
result = vehicles.pop('f1', None)
print(result)
print()

plane = vehicles.pop('learjet')
print(plane)
print()
bike = vehicles.pop('tener', 'not present')
print(bike)
print()

#usando o método get caso a chave nao exista, ele retorna um None.
# Se usarmos uma indexação erradao, ele retorna um erro

# none = vehicles.get('VIRAGO')
# print(none)
# error = vehicles['DREAM']
# print(error)



#alterando um registro existente
vehicles['virago'] = 'Yamaha 1234'

#imprimindo chave
for key in vehicles:
    print(key)

#imprimindo valor
for key in vehicles:
    print(vehicles[key])

#imprimindo chave e valor
for key in vehicles:
    print(key, vehicles[key], sep='; ')

for key, value in vehicles.items():
    print(key, value, sep=', ')

