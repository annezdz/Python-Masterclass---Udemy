menu = ('''
Please choose your option from the list below:
1. Learn Python
2. Learn Java
3. Go swiming
4. Have dinner
5. Go to bed
0. Exit''')
print(menu)
choice = int(input())

while choice != 0:
    if choice == 1 or choice == 2:
        print('Well done')
    elif choice == 3:
        print('Swimming')
    elif choice == 4:
        print('Good dinner')
    elif choice == 5:
        print('Good night')
    else:
        print('Invalid choice, please ' + menu )
    print(menu)
    choice = int(input())
else:
    print('Goodbye')