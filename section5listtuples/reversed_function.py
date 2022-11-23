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
top_index = len(data) -1
for index, value in enumerate(reversed(data)):
        if value < min_valid or value > max_valid:
                del data[top_index - index]
                print(top_index - index, value)

print("this")
print( data)

for index, value in enumerate(reversed(data)):
        if value < min_valid or value > max_valid:
                del data[index - 1]
                print(index - 1, value)
print("that")
print(data)