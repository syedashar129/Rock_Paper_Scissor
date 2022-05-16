import random

while True:
    user = input('Please select "r", "p", or "s" : ')
    print('User has chosen ' + user)

    computer = random.choice(['r', 'p', 's'])
    print('Computer has chosen ' + computer + '\n')

    def Userwin(user,computer):
        if user == 'r' and computer == 's' or user == 'p' and computer == 'r' or user == 's' and computer == 'p':
            return True
        else:
            return False


    if Userwin(user, computer):
        print("User has won. \n")
    else:
        print("Computer has won. \n")

    cont = input('If you want to quit type "q"... \n To continue press enter...')
    if cont == 'q':
        print("You have decided to quit the game.")
        break