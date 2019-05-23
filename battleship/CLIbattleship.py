import random
import pause

def main():
    print(welcomeMessage())
    print('\n\n')

    playerSetup()

def setupVariables():
    #Co-ordinnate followed by Player (P) grid or Opponent (O) grid.

    #Player Grid
    A1P=A2P=A3P=A4P=A5P=A6P=A7P=A8P=A9P=A10P=' '
    B1P=B2P=B3P=B4P=B5P=B6P=B7P=B8P=B9P=B10P=' '
    C1P=C2P=C3P=C4P=C5P=C6P=C7P=C8P=C9P=C10P=' '
    D1P=D2P=D3P=D4P=D5P=D6P=D7P=D8P=D9P=D10P=' '
    E1P=E2P=E3P=E4P=E5P=E6P=E7P=E8P=E9P=E10P=' '
    F1P=F2P=F3P=F4P=F5P=F6P=F7P=F8P=F9P=F10P=' '
    G1P=G2P=G3P=G4P=G5P=G6P=G7P=G8P=G9P=G10P=' '
    H1P=H2P=H3P=H4P=H5P=H6P=H7P=H8P=H9P=H10P=' '
    I1P=I2P=I3P=I4P=I5P=I6P=I7P=I8P=I9P=I10P=' '
    J1P=J2P=J3P=J4P=J5P=J6P=J7P=J8P=J9P=J10P=' '

    #Opponent Grid
    A1O=A2O=A3O=A4O=A5O=A6O=A7O=A8O=A9O=A10O=' '
    B1O=B2O=B3O=B4O=B5O=B6O=B7O=B8O=B9O=B10O=' '
    C1O=C2O=C3O=C4O=C5O=C6O=C7O=C8O=C9O=C10O=' '
    D1O=D2O=D3O=D4O=D5O=D6O=D7O=D8O=D9O=D10O=' '
    E1O=E2O=E3O=E4O=E5O=E6O=E7O=E8O=E9O=E10O=' '
    F1O=F2O=F3O=F4O=F5O=F6O=F7O=F8O=F9O=F10O=' '
    G1O=G2O=G3O=G4O=G5O=G6O=G7O=G8O=G9O=G10O=' '
    H1O=H2O=H3O=H4O=H5O=H6O=H7O=H8O=H9O=H10O=' '
    I1O=I2O=I3O=I4O=I5O=I6O=I7O=I8O=I9O=I10O=' '
    J1O=J2O=J3O=J4O=J5O=J6O=J7O=J8O=J9O=J10O=' '

def welcomeMessage():
    return"""  ____        _   _   _           _     _       
 | __ )  __ _| |_| |_| | ___  ___| |__ (_)_ __  
 |  _ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                         |_|    
                                         
  By Isaac Oldwood                                       """

def playerSetup():
    print('Setup Your Ships')
    print('================\n')

    print('Aircraft Carrier: AAAAA')
    print('Battleship: BBBB')
    print('Cruiser: CCC')
    print('Submarine: SSS')
    print('Destroyer: DD\n\n')

    print('The Grid:')
    print('=========')
    print(grid())

    print("\nEnter Co-ordinates in the style: 'B5,C5,D5,E5,F5'\n")

    input('Aircraft Carrier Co-ordinates: ')


def grid():
    return """\n   +---+---+---+---+---+---+---+---+---+---+ \nA  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+\nB  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+\nC  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+\nD  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+\nE  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+\nF  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+\nG  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+\nH  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+\nI  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+\nJ  |   |   |   |   |   |   |   |   |   |   |
   +---+---+---+---+---+---+---+---+---+---+
     1   2   3   4   5   6   7   8   9   10"""

if __name__ == "__main__":
    main()