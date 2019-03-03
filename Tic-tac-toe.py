import random


def printBoard():
    print "--------------"
    for i in range(3):
        print board[i*3]," | ",board[i*3+1]," | ",board[i*3+2]
        print "--------------"

def playersTurn(symbol):
    printBoard()
    changeBoard(getInput(symbol)-1,symbol)
    check = checkBoard(symbol)
    if check == 1:
        winGame(symbol)
    if check == -1:
        tieGame()


def getInput(symbol):
    choose = -1
    while choose < 1 or choose > 9:
        print "It is ", symbol, "s turn to make a move"
        choose = int(input("Please select a number from 1 to 9 to mark your space :"))
        if choose>0 and choose<9 and board[choose-1]!=' ':
            choose = -1
    return choose

def changeBoard(place, symbol):
    board[place]=symbol

def checkBoard(symbol):
    for i in range(3):
        if board[i*3] == symbol and board[i*3+1] == symbol and board[i*3+2] == symbol:
            return 1
        elif board[i] == symbol and board[i+3] == symbol and board[i+6] == symbol:
            return 1
    if board[0] == symbol and board[4] == symbol and board[8]==symbol:
        return 1
    if board[2] == symbol and board[4] == symbol and board[6]==symbol:
        return 1
    fullBoard = True
    for i in range(9):
        if board[i]==' ':
            fullBoard = False
    if(fullBoard):
        return -1
    return 0


def computerPlay():
    num = smartplay()
    if num != -1:
        changeBoard(num,'O')
    else:
        num = random.randint(0,8)
        while(board[num] != ' '):
            num = random.randint(0,8)
        changeBoard(num,'O')
    check = checkBoard('O')
    if check == 1:
        winGame('O')
    if check == -1:
        tieGame()


def checkForTwo(symbol):
    for i in range(3):
        char = 0
        space = 0
        if board[i*3] == symbol:
            char += 1
        elif board[i*3] == ' ':
            space += 1
        if board[i*3+1] == symbol:
            char += 1
        elif board[i*3+1] == ' ':
            space += 1
        if board[i*3+2] == symbol:
            char += 1
        elif board[i*3+2] == ' ':
            space += 1
        if space == 1 and char == 2:
            if board[i*3] == ' ':
                return i*3
            if board[i*3+1] == ' ':
                return i*3+1
            if board[i*3+2] == ' ':
                return i*3+2

    for i in range(3):
        char = 0
        space = 0
        if board[i] == symbol:
            char += 1
        elif board[i] == ' ':
            space += 1
        if board[i+3] == symbol:
            char += 1
        elif board[i+3] == ' ':
            space += 1
        if board[i+6] == symbol:
            char += 1
        elif board[i+6] == ' ':
            space += 1
        if space == 1 and char == 2:
            if board[i] == ' ':
                return i
            if board[i+3] == ' ':
                return i+3
            if board[i+6] == ' ':
                return i+6
    return -1




def smartplay():
    if random.randint(0,10)<2:
        return -1;
    if checkForTwo('O') != -1:
        return checkForTwo('O')
    if checkForTwo('X') != -1:
        return checkForTwo('X')
    return -1;

def winGame(symbol):
    printBoard()
    print symbol," Has won the game!"
    playAgain()

def tieGame():
    printBoard()
    print "The game was a tie! the board is full"
    playAgain()

def playAgain():
    answer = -1
    while answer != 0 and answer != 1:
        answer = input("Would you like to play again? 0  or 1 ? :")
    if answer == 0:
        quit()
    elif answer == 1:
        for i in range(9):
            board[i] = ' '



def main():
    players = 0
    while players < 1 or players > 2:
        players = input("Is there only 1 player or 2? :")
    game = True
    printBoard();
    print "use 1 to 9 to select a spot!"
    for i in range(9):
        board[i] = ' '
    while game:
        playersTurn('X')
        if game:
            if players == 2:
                playersTurn('O')
            else:
                computerPlay()


board = ['1','2','3','4','5','6','7','8','9']


if __name__ == '__main__':
    main()
