import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ['rock', 'paper', 'scissors']
    user_input = input('Choose rock, paper, scissors or exit: ')
    computer_input = random.choice(options)

    if user_input.lower() == 'exit':
        print('Game ended.')
        print('Your won a total score is ' + str(user_points) +' and computer total score is '+ str(computer_points))
        exit = True

    if user_input.lower() == 'rock':
        if computer_input == 'rock':
            print('Your input is rock.')
            print('Computer input is rock.')
            print('It is tie!')
        elif computer_input == 'paper':
            print('Your input is rock.')
            print('Computer input is paper.')
            print('Computer wins!')
            computer_points += 1
        elif computer_input == 'scissors':
            print('Your input is rock.')
            print('Computer input is scissors.')
            print('You win!')
            user_points += 1

    elif user_input.lower() == 'paper':
        if computer_input == 'rock':
            print('Your input is paper.')
            print('Computer input is rock.')
            print('You win!')
            user_points += 1
        elif computer_input == 'paper':
            print('Your input is paper.')
            print('Computer input is paper.')
            print('It is tie!')
        elif computer_input == 'scissors':
            print('Your input is paper.')
            print('Computer input is scissors.')
            print('Computer wins!')
            computer_points += 1

    elif user_input.lower() == 'scissors':
        if computer_input == 'rock':
            print('Your input is scissors.')
            print('Computer input is rock.')
            print('Computer wins!')
            computer_points += 1
        elif computer_input == 'paper':
            print('Your input is scissors.')
            print('Computer input is paper.')
            print('You win!')
            user_points += 1
        elif computer_input == 'scissors':
            print('Your input is scissors.')
            print('Computer input is scissors.')
            print('It is tie!')
    
    elif user_input.lower() != " rock" or user_input.lower() != "paper" or user_input.lower() != "scissors" or user_input.lower() != "exit":
        print("Invalid Input")
