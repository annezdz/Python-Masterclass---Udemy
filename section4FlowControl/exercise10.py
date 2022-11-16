# Modify the code so that it stops printing when it reaches a number greater than zero that's
# exactly divisible by 11. That number should be the last value printed.
for i in range(0, 100, 7):
    if i > 0 and i % 11 == 0:
        print(i)
        break
    print(i)
#
# Write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5.
# Zero is considered divisible by everything (zero should not appear in the output).
print()
for i in range(0, 20):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
