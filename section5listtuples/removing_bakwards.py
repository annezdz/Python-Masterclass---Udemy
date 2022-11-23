data = [104, 1201, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200
other_data = sorted(data)
# for index in range(len(data) -1, -1, -1):
#
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]
# print(data)

for index in range(len(data) -1, -1, -1):

    if other_data[index] < min_valid or other_data[index] > max_valid:
        print(index, other_data)
        del other_data[index]
print(other_data)