
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def playGame() :
    # Display the initial Board 
    display_board() 
    while game_still_going :
        handleTurn()

def handleTurn():
    position = input("Chose a Position from 1 to 9 : ")
    position = int(position) - 1 

    board[position] = "X" 


playGame()
