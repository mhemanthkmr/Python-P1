# --------- Global Variables -----------
# Game Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# If Game is still going

game_still_going = True

# Who won or tie ?

Winner = None 

# Who's Turn is it ?

currentPlayer = "X"

# --------- End of Global Variables ----------

# Functions are Starting 

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def playGame() :
    # Display the initial Board 
    display_board() 

    # While the game is still going
    while game_still_going :

        #handle a single turn player of an arbitary player
        handleTurn(currentPlayer)

        # check if the game has ended
        checkIfGameOver()

        # Flip to the other player
        flipPlayer()
    if Winner == "X" or Winner == "O" :
        print(Winner + "Won")
    elif Winner == None :
        print("Tie !")

# Handle a Single turn of an arbitary player
def handleTurn(player):
    position = input("Chose a Position from 1 to 9 : ")
    position = int(position) - 1 

    board[position] = "X" 

    display_board()

def checkIfGameOver():
    checkIfWin()
    checkIfDraw()

def checkIfWin():
    # Check rows
    # Check Columns
    # Check Diagonal
    return

def checkIfDraw():
    return

def flipPlayer():
    return

playGame()