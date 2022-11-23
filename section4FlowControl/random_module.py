import random

highest = 1000
answer = random.randint(1, highest)
print(answer)
flag = True

guess = 0
count = 1
print("Please guess number between 1 and {}: ".format(highest))
while flag:
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
        flag = False
    else:
        count = int(input('Continue ? 0 no 1 yes : '))
        if count != 0:
            if guess < answer:
                print("Please guess higher")
            else:
               print("Please guess lower")
        else:
           break
# guess = int(input())
# if guess == answer:
#     print("Well done, you guessed it {}")
# else:
#     print("Sorry, yout have guessed correctly")


#Tim,s solution
while guess != answer:
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")