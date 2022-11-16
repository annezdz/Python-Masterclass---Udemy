available_exists = ['north', 'south', 'east', 'west']

#read file or data stream
choose_exit = ''
while choose_exit not in available_exists:
    choose_exit = input('Please choose a direction: ')
    #casefold converte para minusculo

    if choose_exit.casefold() == 'quit':
        print('Game over')
        break
print('arent you glad you got out of there')