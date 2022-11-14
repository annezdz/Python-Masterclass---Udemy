# Podemos usar aspas simples ou duplas, porém precisamos usar sempre a mesma para finalizar a String
print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')

print("hello" + " world")

greeting = "Hello"
#Usando a função input do teclado

name = input("Please enter your name: ")

print(greeting + ' ' + name)

age = 24
print(age)

# Descobrir o tipo da variável
print(type(greeting))
print(type(age))

age_in_words = "2 years"

# TypeError: can only concatenate str (not "int") to str
# Python não converte o int em String (como o Java faz nesse caso)
print(name + f" is  {age}  years old")
print(type(age))


