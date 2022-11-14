parrot = "Norwegian Blue"
print(parrot)

print()
print(parrot[-1]) # vai para o final da String  e imprime a ultima letra
print(parrot[-14])
win = "win"


print(parrot[3]) #imprimindo uma letra
print(parrot[4])
print()

# Slicing
print(parrot[0:6]) # nao inclui a posicao 6
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:])
print(parrot[10:14])
print()
print(parrot[:6])
print(parrot[6:])
print()
print(parrot[:6] + parrot[6:])
print(parrot[:]) # fatia do inicio ao fim, pois não tem um ponto de parada

#slicing with negative numbers

print(parrot[-4:2]) # nesse caso nao imprime nada pois não pode retroceder
print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[-14:-8])
print(parrot[-4:-1])

#using steps in slice

print(parrot[0:14:2])
print(parrot[0:14:3])

number = "9,223;372:036 854,775;807"
print(number[1::4]) #,,,,,, não coloca o final e pega a cada 4
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])


# for i in range(win.__sizeof__()):
#     print(win[i])
#
# print()
# for i in range(win.__sizeof__() - 14):
#     print(win[i])
