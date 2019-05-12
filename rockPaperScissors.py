import random
import pause

def main():
    welcomeMessage()

    while True:
        print('')
        playerChoice=playerChoose().capitalize()
        displayPlayerChoice(playerChoice)
        pause.seconds(1)
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

def displayPlayerChoice(playerChoice):
    print('')
    if playerChoice=='Rock':
        rockImage()
    elif playerChoice=='Paper':
        paperImage()
    elif playerChoice=='Scissors':
        scissorsImage()

def rockImage():
    print("""          `....`              
  ```````..--:/:.`            
 .---.------:/+//:.           
 -//:::++++oso+++//-          \n`-///:/+oydddhs++///-         \n`:------:/+osho+/////-        \n.-:://+///++ohs+///+++-``     \n.-.-:///++osyso++/++++/:--.`  \n.::://///++yyo+++++++++//::--.\n`:/++o++++/+s+++++++++++///:::\n `-///////+o+/////+++++++/////\n   `--::::///////+++++++//////\n             `.:/++++/////////
                 .-///////////""")

def paperImage():
    print("""                  .``:-.      
                `:/-++:--`    
             --:+//+o/://-`   
           `:/:o/:+o/::+:-`   
          .//:++/+o++oo:-.    
         -//:++//o/:+s/:-`    
       .://::/::+/+so/:-.     
      .//::--::-::/+o/:-`     
     `::::::://:///:---`   `  
     :::-----:::://:::. .:::-.
    `::-------:::--.-/-/+/:-` 
    -::----::::::-../:-:::-`  
   -//::::::::::--------.`    
 `/////////::::-----:-`       \n.//////////////::-.`          \n///////++++++:-.`             """)

def scissorsImage():
    print("""
                -:.`           
              ./:-`           
              `::-.            
             .::-`         `` 
             :/:.`      `.::-`
     ```.```./:--`   `.-::--. 
   .-----.-////:-``.-::---.   
  -::-..-:://////::::::.`     
 -///:-.-ssso//:///::-`       \n./o+::-..osso+/::::-`         
 `:/:/:-.-:::/:::-`           
  :::/:-...-::--.`            
  ::://:--..---`              """)

if __name__=="__main__":
    main()