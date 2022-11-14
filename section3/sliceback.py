letters = "abcdefghijklmnopqrstuvxwz"
print(letters[25::-1])
print(letters[::-1])

#qpo
print(letters[16:13:-1])

#edcba
print(letters[4::-1])

#last 8 chars
print(letters[25:25-9:-1])
print(letters[:-9:-1])

# imprimir as ultimas letras o valor comeca com um valor negativo
print(letters[-4:])
print(letters[-1:])
#para imprimir os valores iniciais, numero positivo no meio
print(letters[:1])
print(letters[0])

letters2 = ""
print(letters2[0]) #IndexError: string index out of range
