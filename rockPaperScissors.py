import random

def main():
    print('Welcome To Rock Paper Scissors!\n')
    playerChoice=playerChoose().capitalize()
    aiChoice=aiChoose()
    outcome=checkWinner(playerChoice,aiChoice)

    print('You ' +outcome)

def playerChoose():
    return input('Choose Your Weapon: ')

def aiChoose():
    return random.choice(['Rock','Paper','Scissors'])

def checkWinner(playerChoice,aiChoice):
    if playerChoice == 'Rock':
        if aiChoice == 'Rock':
            return 'Draw'
        elif aiChoice == 'Paper':
            return 'Lose'
        elif aiChoice == 'Scissors':
            return 'Win'
    elif playerChoice == 'Paper':
        if aiChoice == 'Rock':
            return 'Win'
        elif aiChoice == 'Paper':
            return 'Draw'
        elif aiChoice == 'Scissors':
            return 'Lose'
    elif playerChoice == 'Scissors':
        if aiChoice == 'Rock':
            return 'Lose'
        elif aiChoice == 'Paper':
            return 'Win'
        elif aiChoice == 'Scissors':
            return 'Draw'


if __name__=="__main__":
    main()