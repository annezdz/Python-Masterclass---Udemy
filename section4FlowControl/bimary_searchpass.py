low = 1
high = 1000
print('Please think of a number between {} and {}'.format(low, high))

input('Press ENTER to start')

guesses = 1
while low != high:
    print("\t Guessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower ? Enter h ou l or c "
                     "if my guess was correct - ".format(guess).casefold())

#pass um espaço de codigo futuro e continua a execucao

    if high_low == 'h':
        low = guess + 1
    elif high_low == 'l':
        high = guess - 1
    elif high_low == 'c':
        print('I got it in {} guesses!'.format(guesses))
        break
    else:
        print('Please enter h, l or c')
    guesses = guesses + 1
else:
    print("Yout thought of the number {}".format(low))
    print('I got it in {} guesses!'.format(guesses))