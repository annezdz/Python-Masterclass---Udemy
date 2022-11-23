a = b = c = d = e = f = 12
print(c)
x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print('Unpacking a tuple')
data = 1, 2, 76

x, y, z = data

print(x)
print(y)
print(z)

print('Unpacking a list')
data_list = [12, 13, 14]

p, q, r = data_list
print(p)
print(q)
print(r)

# for index, character in enumerate('abcdefgh'):
#     print(index + 1, character)

for t in enumerate('abcdefgh'):
    index, character = t
    print(index, character)