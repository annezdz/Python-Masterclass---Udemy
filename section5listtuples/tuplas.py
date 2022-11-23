welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# tuplas sao imutaveis
'''
Protege a integridade do dado
Usar em casos que nao vai haver mudanças. ajuda a prevenir bugs
tuplas podem fazer o unpacking com sucesso, listas da erro
# '''
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])


# metallica2 = list(metallica)
# print(metallica2)
# metallica2[0] = 'teste'
# print(metallica2)

title, artist, year = metallica
print(artist)
print(title)
print(year)

table = ('Coffee table', 200, 100, 75, 34.50)
name, lenght, width, height, price = table
# print(table[1] * table[2])
print(lenght * height)
