numbers = (0, 1, 2, 3, 4, 5)  # tupla


# print(numbers, sep=';')
# print(*numbers, sep=';') #unpack the values
# print(0, 1, 2, 3, 4, 5, sep=';')


def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)
print()
test_star()