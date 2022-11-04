player1 = "X"
player2 = "O"
currentPlayer = " "
gameRunning = True
choice = 0
round = 1
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def printBoard():
    print(
    '''
    ''' + board[0] + ''' | ''' + board[1] + ''' | ''' + board[2] + '''
   ===+===+===
    ''' + board[3] + ''' | ''' + board[4] + ''' | ''' + board[5] + ''' 
   ===+===+===
    ''' + board[6] + ''' | ''' + board[7] + ''' | ''' + board[8] + '''
    '''
    )
    print("Round: " + str(round))

def winMsg():
    print("Player " + currentPlayer + " won!")

while gameRunning:

    if(round % 2) == 0:
        currentPlayer = player2
    if(round % 2) != 0:
        currentPlayer = player1

    printBoard()
    print('''
    Player ''' + currentPlayer + ''' turn.
    '''
    )

    # Validate Input.
    while True:
        try:
            print("Select a number between 0 and 8")
            choice = abs(int(input('Choose tile: ')))

            if (board[choice] == " "):
                board[choice] = currentPlayer
                break

            print("Tile already taken!")

        except ValueError:
            print("Please enter a whole number.")
        except IndexError:
            print("Invalid Number")

    # Check win condition.
    if(board[0] == currentPlayer and board[1] == currentPlayer and board[2] == currentPlayer):
        winMsg()
        break
    if(board[3] == currentPlayer and board[4] == currentPlayer and board[5] == currentPlayer):
        winMsg()
        break
    if(board[6] == currentPlayer and board[7] == currentPlayer and board[8] == currentPlayer):
        winMsg()
        break
    if(board[0] == currentPlayer and board[3] == currentPlayer and board[6] == currentPlayer):
        winMsg()
        break
    if(board[1] == currentPlayer and board[4] == currentPlayer and board[7] == currentPlayer):
        winMsg()
        break
    if(board[2] == currentPlayer and board[5] == currentPlayer and board[8] == currentPlayer):
        winMsg()
        break
    if(board[0] == currentPlayer and board[4] == currentPlayer and board[8] == currentPlayer):
        winMsg()
        break
    if(board[2] == currentPlayer and board[4] == currentPlayer and board[6] == currentPlayer):
        winMsg()
        break
    if " " not in board:
        print("Draw!")
        break

    round+=1
printBoard()