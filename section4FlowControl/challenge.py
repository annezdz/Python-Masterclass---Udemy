name = input("What's your name ?")
age = int(input("What's your age? "))


if age >= 18 and age <= 30:
    print("Welcome {0} to the holiday".format(name))
else:
    print("Hey {0}, you're not alowed".format(name))