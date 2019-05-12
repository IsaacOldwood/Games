import random
import pause

def main():
    welcomeMessage()

    while True:
        print('')
        playerChoice=playerChoose().capitalize()
        aiChoice=aiChoose()
        outcome=checkWinner(playerChoice,aiChoice)
    
        print(outcomeMessage(outcome))
        pause.seconds(1)
        input('Play Again?')

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

def outcomeMessage(outcome):
    if outcome!= 'Draw':
        return 'You '+ outcome
    else:
        return "It's A Draw"

def welcomeMessage():
    print("""  ____            _      ____                         ____       _                        
 |  _ \ ___   ___| | __ |  _ \ __ _ _ __   ___ _ __  / ___|  ___(_)___ ___  ___  _ __ ___ 
 | |_) / _ \ / __| |/ / | |_) / _` | '_ \ / _ \ '__| \___ \ / __| / __/ __|/ _ \| '__/ __|
 |  _ < (_) | (__|   <  |  __/ (_| | |_) |  __/ |     ___) | (__| \__ \__ \ (_) | |  \__ \\
 |_| \_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_|    |____/ \___|_|___/___/\___/|_|  |___/
                                   |_|                                                     """)

    print('By Isaac Oldwood')

if __name__=="__main__":
    main()