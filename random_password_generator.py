import string
import random

character = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def generate_password():
    password_length = int(input('How long would you like your password to be? '))
    print('')

    random.shuffle(character)

    password = []

    for x in range(password_length):
        password.append(random.choice(character))

    random.shuffle(password)
    password = ''.join(password)

    print(password + '\n')

while True:
    option = input('Do you want to generate a password? (Y/N): ')
    print('')

    if option.lower() == 'y' or option.lower() == 'yes':
        generate_password()
    elif option.lower() == 'n' or option.lower() == 'no':
        print('Program ended' + '\n')
        quit()
    else:
        print('Invalid input, please try again!' + '\n')