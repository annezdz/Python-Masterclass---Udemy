available_exists = ['north', 'south', 'east', 'west']

#read file or data stream
choose_exit = ''
while choose_exit not in available_exists:
    choose_exit = input('Please choose a direction: ')
    if choose_exit.casefold() == 'quit':
        print("Gameover")
        break
else:
    print('arent you glad you got out of there')