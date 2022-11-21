def calc_even(n):
    total = 0
    for index in range(0, n):
        total += n - index
    print(total)


calc_even(7)


def sum_eo(n, t):
    if t == 'e':
        return calc_resto(n, 0)
    elif t == 'o':
        return calc_resto(n, 1)


def calc_resto(n, resto):
    total = []
    for index in range(n):
        if index % 2 == resto:
            total.append(index)
    return total


print(sum_eo(5, 'e'))
print(sum_eo(5, 'o'))
print(sum_eo(3, 'o'))
print(sum_eo(3, 'e'))