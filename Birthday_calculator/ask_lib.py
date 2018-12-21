import datetime

def ask_name():
    name = raw_input("Please enter your name: ")
    if name is not "":
        print('Thank you, ' + name + ".")

        return  name
    else:
        print('Name not valid. Retrying...')
        ask_name()

def ask_age(name):
    age = raw_input("Please enter your age: ")
    if age is not "":
        print('Thanks again, ' + name + "!")
        return age
    else:
        print('Name not valid. Retrying...')
        ask_name()


def ask_100_birthday(name, age):
    answer = raw_input("Would you like to know when you're 100th Birthday is, " + name + "? (yes/no): ")
    if answer == 'yes' :
        print('No probs.')
        now = datetime.datetime.now()
        this_year = now.year

        years_until_100_bithday = 100 - int(age)
        year_of_100_birthday = this_year + years_until_100_bithday

        print(name + " your 100th birthday will be in the year " + str(year_of_100_birthday) + ".")

    elif answer == 'no':
        print("No problem.  Can't handle the truth, huh?")
        exit(0)

    else:
        print("Please type 'yes' or 'no' this time!")
        ask_100_birthday(name, age)



def multiply_nums(num1, num2):
    answer = num1*num2
    return answer