import random

def function():
    
    def roll_dice():

        dice_drawing = {
            1: (
                "------",
                "|     |",
                "|  o  |",
                "|     |",
                "------",
            ),
            2: (
                "------",
                "|o    |",
                "|     |",
                "|    o|",
                "------",
            ),
            3: (
                "------",
                "|o    |",
                "|  o  |",
                "|    o|",
                "------",
            ),
            4: (
                "------",
                "|o   o|",
                "|     |",
                "|o   o|",
                "------",
            ),
            5: (
                "------",
                "|o   o|",
                "|  o  |",
                "|o   o|",
                "------",
            ),
            6: (
                "------",
                "|o   o|",
                "|o   o|",
                "|o   o|",
                "------",
            ),

        }
        
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print('Dice rolled: {} and {}'.format(dice1, dice2))
        print('\n'.join(dice_drawing[dice1]))
        print('\n'.join(dice_drawing[dice2]))

    roll = input('Roll the dice? (Y/N): ')

    while  True:

        if roll.lower() == 'y' or roll.lower() == 'yes':
            roll_dice()
            roll = input('\n' + 'Roll again? (Y/N): ')
        elif roll.lower() == 'n' or roll.lower() == 'no':
            print('\n' + 'Program ended' + '\n')
            quit()
        else:
            print('\n' + 'Invalid input, please try again!' + '\n')
            function()
function()

