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
        print(Winner + " Won .")
    elif Winner == None :
        print("Tie !")

# Handle a Single turn of an arbitary player
def handleTurn(player):
    print (player + "s Turn !")
    position = input("Chose a Position from 1 to 9 : ")
    if position not in ["1","2","3","3","4","5","6","7","8","9"] :
        position = input("Invalid input . Choose a position from 1 - 9 :")
    position = int(position) - 1 

    board[position] = player 

    display_board()

def checkIfGameOver():
    checkForWinner()
    checkIfDraw()

def checkForWinner():
    #set a global variable
    global Winner 
    # Check rows
    row_Winner = checkRows()
    # Check Columns
    column_Winner = checkColumn()
    # Check Diagonal
    diagonal_Winner = checkDiagonal()

    if row_Winner :
        Winner = row_Winner
    elif column_Winner :
        Winner = column_Winner
    elif diagonal_Winner :
        Winner = diagonal_Winner
    else :
        Winner = None

    return

def checkRows():
    #set up global variable
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"  

    if row_1 or row_2 or row_3 :  
        game_still_going = False
    if row_1 :
        return board[0]
    elif row_2 :
        return board[3]
    elif row_3 :
        return board[6]
    return

def checkColumn():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"  

    if column_1 or column_2 or column_3 :  
        game_still_going = False
    if column_1 :
        return board[0]
    elif column_2 :
        return board[1]
    elif column_3 :
        return board[2]
    return

def checkDiagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2 :
        game_still_going = False
    if diagonal_1 :
        return board[0]
    elif diagonal_2 :
        return board[6]
    return

def checkIfDraw():
    global game_still_going
    if "-" not in board :
        game_still_going = False
    return

def flipPlayer():
    global currentPlayer
    if currentPlayer == "X" :
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return

playGame()