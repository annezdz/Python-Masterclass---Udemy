'''Set:
1. It is similar to list
2 - it can store different type of values (objects) string, int, float,, bool, etc
3 - Set cannot have duplicate values
4 - Set are definex {}
5 - It is a collection which is unordered and undexed'''

s1 = {'Selenium', 'Appium', 'Cypress', 100, True, 100.1}
print(s1)
print(type(s1))#<class 'set'>
print(len(s1))

for i in s1:
    print(i)

#add

s1.add('Dudu')
print(s1)

s1.remove('Appium') #se o valor nao existir, lança excessão
print(s1)


s1.discard('Selenium')#se o valor nao existir, nao lanca excessao
print(s1)

# print(s1 * 2)#unsupported operand type(s) for *: 'set' and 'int'

#copiando um set
s3 = s1.copy()
print('************')
print(s3)
s1.clear()
print(s3)
print(s1)#set()