import random
import pause

def main():
    playerGridDict,opponentGridDict=setupVariables()
    print(welcomeMessage())
    print('\n\n')

    playerSetup(playerGridDict)

def setupVariables():
    #Co-ordinnate followed by Player (P) grid or Opponent (O) grid.

    #Player Grid
    playerGridDict={'A1':' ', 'A2':' ', 'A3':' ', 'A4':' ', 'A5':' ', 'A6':' ', 'A7':' ', 'A8':' ', 'A9':' ', 'A10':' ',
    'B1':' ', 'B2':' ', 'B3':' ', 'B4':' ', 'B5':' ', 'B6':' ', 'B7':' ', 'B8':' ', 'B9':' ', 'B10':' ',
    'C1':' ', 'C2':' ', 'C3':' ', 'C4':' ', 'C5':' ', 'C6':' ', 'C7':' ', 'C8':' ', 'C9':' ', 'C10':' ',
    'D1':' ', 'D2':' ', 'D3':' ', 'D4':' ', 'D5':' ', 'D6':' ', 'D7':' ', 'D8':' ', 'D9':' ', 'D10':' ',
    'E1':' ', 'E2':' ', 'E3':' ', 'E4':' ', 'E5':' ', 'E6':' ', 'E7':' ', 'E8':' ', 'E9':' ', 'E10':' ',
    'F1':' ', 'F2':' ', 'F3':' ', 'F4':' ', 'F5':' ', 'F6':' ', 'F7':' ', 'F8':' ', 'F9':' ', 'F10':' ',
    'G1':' ', 'G2':' ', 'G3':' ', 'G4':' ', 'G5':' ', 'G6':' ', 'G7':' ', 'G8':' ', 'G9':' ', 'G10':' ',
    'H1':' ', 'H2':' ', 'H3':' ', 'H4':' ', 'H5':' ', 'H6':' ', 'H7':' ', 'H8':' ', 'H9':' ', 'H10':' ',
    'I1':' ', 'I2':' ', 'I3':' ', 'I4':' ', 'I5':' ', 'I6':' ', 'I7':' ', 'I8':' ', 'I9':' ', 'I10':' ',
    'J1':' ', 'J2':' ', 'J3':' ', 'J4':' ', 'J5':' ', 'J6':' ', 'J7':' ', 'J8':' ', 'J9':' ', 'J10':' '}

    #Opponent Grid
    opponentGridDict={'A1':' ', 'A2':' ', 'A3':' ', 'A4':' ', 'A5':' ', 'A6':' ', 'A7':' ', 'A8':' ', 'A9':' ', 'A10':' ',
    'B1':' ', 'B2':' ', 'B3':' ', 'B4':' ', 'B5':' ', 'B6':' ', 'B7':' ', 'B8':' ', 'B9':' ', 'B10':' ',
    'C1':' ', 'C2':' ', 'C3':' ', 'C4':' ', 'C5':' ', 'C6':' ', 'C7':' ', 'C8':' ', 'C9':' ', 'C10':' ',
    'D1':' ', 'D2':' ', 'D3':' ', 'D4':' ', 'D5':' ', 'D6':' ', 'D7':' ', 'D8':' ', 'D9':' ', 'D10':' ',
    'E1':' ', 'E2':' ', 'E3':' ', 'E4':' ', 'E5':' ', 'E6':' ', 'E7':' ', 'E8':' ', 'E9':' ', 'E10':' ',
    'F1':' ', 'F2':' ', 'F3':' ', 'F4':' ', 'F5':' ', 'F6':' ', 'F7':' ', 'F8':' ', 'F9':' ', 'F10':' ',
    'G1':' ', 'G2':' ', 'G3':' ', 'G4':' ', 'G5':' ', 'G6':' ', 'G7':' ', 'G8':' ', 'G9':' ', 'G10':' ',
    'H1':' ', 'H2':' ', 'H3':' ', 'H4':' ', 'H5':' ', 'H6':' ', 'H7':' ', 'H8':' ', 'H9':' ', 'H10':' ',
    'I1':' ', 'I2':' ', 'I3':' ', 'I4':' ', 'I5':' ', 'I6':' ', 'I7':' ', 'I8':' ', 'I9':' ', 'I10':' ',
    'J1':' ', 'J2':' ', 'J3':' ', 'J4':' ', 'J5':' ', 'J6':' ', 'J7':' ', 'J8':' ', 'J9':' ', 'J10':' '}

    return playerGridDict , opponentGridDict

def welcomeMessage():
    return"""  ____        _   _   _           _     _       
 | __ )  __ _| |_| |_| | ___  ___| |__ (_)_ __  
 |  _ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                         |_|    
                                         
  By Isaac Oldwood                                       """

def playerSetup(playerGridDict):
    print('Setup Your Ships')
    print('================\n')

    print('Aircraft Carrier: AAAAA')
    print('Battleship: BBBB')
    print('Cruiser: CCC')
    print('Submarine: SSS')
    print('Destroyer: DD\n\n')

    print('The Grid:')
    print('=========')
    print(grid(playerGridDict))

    print("\nEnter Co-ordinates in the style: 'B5,C5,D5,E5,F5'\n")

    rawPlayerCarrierCoords=input('Aircraft Carrier Co-ordinates: ')
    splitPlayerCarrierCoords=rawPlayerCarrierCoords.split(',')
    for coord in splitPlayerCarrierCoords:
        playerGridDict[coord]='A'


def grid(gridDict):
    return f"""\n   +---+---+---+---+---+---+---+---+---+---+ \nA  | {gridDict['A1']} | {gridDict['A2']} | {gridDict['A3']} | {gridDict['A4']} | {gridDict['A5']} | {gridDict['A6']} | {gridDict['A7']} | {gridDict['A8']} | {gridDict['A9']} | {gridDict['A10']} |
   +---+---+---+---+---+---+---+---+---+---+\nB  | {gridDict['B1']} | {gridDict['B2']} | {gridDict['B3']} | {gridDict['B4']} | {gridDict['B5']} | {gridDict['B6']} | {gridDict['B7']} | {gridDict['B8']} | {gridDict['B9']} | {gridDict['B10']} |
   +---+---+---+---+---+---+---+---+---+---+\nC  | {gridDict['C1']} | {gridDict['C2']} | {gridDict['C3']} | {gridDict['C4']} | {gridDict['C5']} | {gridDict['C6']} | {gridDict['C7']} | {gridDict['C8']} | {gridDict['C9']} | {gridDict['C10']} |
   +---+---+---+---+---+---+---+---+---+---+\nD  | {gridDict['D1']} | {gridDict['D2']} | {gridDict['D3']} | {gridDict['D4']} | {gridDict['D5']} | {gridDict['D6']} | {gridDict['D7']} | {gridDict['D8']} | {gridDict['D9']} | {gridDict['D10']} |
   +---+---+---+---+---+---+---+---+---+---+\nE  | {gridDict['E1']} | {gridDict['E2']} | {gridDict['E3']} | {gridDict['E4']} | {gridDict['E5']} | {gridDict['E6']} | {gridDict['E7']} | {gridDict['E8']} | {gridDict['E9']} | {gridDict['E10']} |
   +---+---+---+---+---+---+---+---+---+---+\nF  | {gridDict['F1']} | {gridDict['F2']} | {gridDict['F3']} | {gridDict['F4']} | {gridDict['F5']} | {gridDict['F6']} | {gridDict['F7']} | {gridDict['F8']} | {gridDict['F9']} | {gridDict['F10']} |
   +---+---+---+---+---+---+---+---+---+---+\nG  | {gridDict['G1']} | {gridDict['G2']} | {gridDict['G3']} | {gridDict['G4']} | {gridDict['G5']} | {gridDict['G6']} | {gridDict['G7']} | {gridDict['G8']} | {gridDict['G9']} | {gridDict['G10']} |
   +---+---+---+---+---+---+---+---+---+---+\nH  | {gridDict['H1']} | {gridDict['H2']} | {gridDict['H3']} | {gridDict['H4']} | {gridDict['H5']} | {gridDict['H6']} | {gridDict['H7']} | {gridDict['H8']} | {gridDict['H9']} | {gridDict['H10']} |
   +---+---+---+---+---+---+---+---+---+---+\nI  | {gridDict['I1']} | {gridDict['I2']} | {gridDict['I3']} | {gridDict['I4']} | {gridDict['I5']} | {gridDict['I6']} | {gridDict['I7']} | {gridDict['I8']} | {gridDict['I9']} | {gridDict['I10']} |
   +---+---+---+---+---+---+---+---+---+---+\nJ  | {gridDict['J1']} | {gridDict['J2']} | {gridDict['J3']} | {gridDict['J4']} | {gridDict['J5']} | {gridDict['J6']} | {gridDict['J7']} | {gridDict['J8']} | {gridDict['J9']} | {gridDict['J10']} |
   +---+---+---+---+---+---+---+---+---+---+
     1   2   3   4   5   6   7   8   9   10"""

if __name__ == "__main__":
    main()