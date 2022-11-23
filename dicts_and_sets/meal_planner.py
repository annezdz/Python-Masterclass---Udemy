from contents import pantry, recipes

# display_dict = {str(index + 1):meal for index, meal in enumerate(recipes)}

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # display a menu of the recipes we know how to cook
    print('Please choose your recipe')
    print('*' * 30)
    for key, value in display_dict.items():
        print(f'{key} - {value}')
    choice = input(' > ')
    if choice == '0':
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f'You have selected: {selected_item}')
        print('Checking ingredients...')
        ingredients = recipes[selected_item]
        print(ingredients)
        print('Verify pantry')
        for item in ingredients:
            if item in pantry:
                print(f'Item {item} in stock')
            else:
                print(f'Item {item} must buy')
        # for key, value in pantry.items():
        #     for item in ingredients:
        #         if item in key:
        #             print(f'Item {item} in stock')
