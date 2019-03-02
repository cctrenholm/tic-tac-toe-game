#! /usr/bin/python

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print bcolors.HEADER + "Welcome to two player Tic Tac Toe!" + bcolors.ENDC
print bcolors.HEADER + "Select the number to place an X or O in the box" + bcolors.ENDC
print bcolors.HEADER + "Player 1 is X" + bcolors.ENDC


box = []

for i in range (0, 9) :
    box.append(str(i + 1))

playerMove = True
winner = False

def printBoard() :
    print bcolors.BOLD +( '\n -----') + bcolors.ENDC
    print bcolors.BOLD +( '|' + box[0] + '|' + box[1] + '|' + box[2] + '|') + bcolors.ENDC
    print bcolors.BOLD +( ' -----')
    print bcolors.BOLD +( '|' + box[3] + '|' + box[4] + '|' + box[5] + '|') + bcolors.ENDC
    print bcolors.BOLD +( ' -----') + bcolors.ENDC
    print bcolors.BOLD +( '|' + box[6] + '|' + box[7] + '|' + box[8] + '|') + bcolors.ENDC
    print bcolors.BOLD +( ' -----\n') + bcolors.ENDC

while not winner :
    printBoard()

    if playerMove :
        print bcolors.OKBLUE + ( "Player 1:") + bcolors.ENDC
    else :
        print bcolors.OKGREEN + ( "Player 2:") + bcolors.ENDC

    try:
        selection = int(input(">> "))
    except:
        print("Sorry, that won't work.  Try again.")
        continue
    if box[selection - 1] == 'X' or box [selection-1] == 'O':
        print("That space is already taken.")
        continue

    if playerMove :
        box[selection - 1] = 'X'
    else :
        box[selection - 1] = 'O'

    playerMove = not playerMove

    for x in range (0, 3) :
        y = x * 3
        if (box[y] == box[(y + 1)] and box[y] == box[(y + 2)]) :
            winner = True
            printBoard()
        if (box[x] == box[(x + 3)] and box[x] == box[(x + 6)]) :
            winner = True
            printBoard()

    if((box[0] == box[4] and box[0] == box[8]) or 
       (box[2] == box[4] and box[4] == box[6])) :
        winner = True
        printBoard()

print bcolors.HEADER + "The winner is player: " + str(int(playerMove + 1)) + bcolors.ENDC