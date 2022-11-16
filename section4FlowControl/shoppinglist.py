shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', "rice"]

# for item in shopping_list:
#     if item != 'spam':
#         print("Buy " + item)

# o continue, quando acha o spam, volta para o for , ou seja, continua ate o final do loop pulando o spam
# for item in shopping_list:
#     if item == 'spam':
#         continue
#     print("Buy " + item)
#
for item in shopping_list:
    if item == 'spam':
        break
    print("Buy " + item)

print('*' * 30)
item_to_find = 'milk'
fount_at = None # o none é uma constante que não tem valor

# len nos dá o tamamnho da lista
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         fount_at = index
#         break
if item_to_find in shopping_list:
    fount_at = shopping_list.index(item_to_find)

if fount_at is not None:
    print('Item found at index {}'.format(fount_at))
else:
    print('{} not found'.format(item_to_find))
