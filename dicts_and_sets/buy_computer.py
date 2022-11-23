available_parts = {'1': 'computer',
                   '2': 'monitor',
                   '3': 'keyboard',
                   '4': 'mouse',
                   '5': 'mouse mat',
                   '6': 'hdmi',
                   '7': 'dvd',
                   }
#quando usamos o in em um dicionario, ele olha as chaves
current_choice = None
while current_choice != '0':
    print('Choice a valid option or 0 to exit')
    current_choice = input(' > ')
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f'Adding {chosen_part}')
    elif current_choice not in available_parts and current_choice != '0':
        for key, value in available_parts.items():
            print(key, value, sep=': ')
            continue


