import random


def get_integer(prompt: str) -> int:
    """
    Gets an integer from Standard Input(stdin).

    The function will continue looping , and prompting
    the ser, until a valid 'int' is entered.

    :param prompt: The String that the user will see, when
             there prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print(' {} is a invalid number'.format(temp))

#para imprimir o DocString de uma função
print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer)
flag = True

guess = 0
count = 1
print("Please guess number between 1 and {}: ".format(highest))
while flag:
    guess = get_integer(": ")
    if guess == answer:
        print("Well done, you guessed it")
        flag = False
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        count = int(input('Continue ? 0 no 1 yes : '))
        if count != 0:
            continue
        else:
            break
