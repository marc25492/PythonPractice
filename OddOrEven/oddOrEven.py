
##Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

number = raw_input('Enter a number: ')

remainder = int(number) % 2

if remainder != 0:
    print("You've entered an Odd Number!")
else:
    print("You've entered an Even Number!")