import numpy as np

board = np.array([
    ["","",""],
    ["","",""],
    ["","",""]
    ])

player = "X"
comp = "O"

def won(board):
    # Check if player has won horizontally
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return True, row[0]
    2
    # Check if player has won vertically
    for col in board.T:
        if col[0] == col[1] == col[2] and col[0] != "":
            return True, col[0]

    # Check if player has won diagonally
    if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != "":
        return True, board[1][1]

    return False, ""


def game_over(board):
    for row in board:
        if "" in row:
            return False
    return True



def minimax(position, depth, maxP):
    
    has_won, winner = won(board)
    if has_won and winner == comp:
        return 10
    elif has_won and winner == player:
        return -10
    elif game_over(board):
        return 0

    if maxP:
        maxEval = -10000
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                if board[i][j] == "":
                    board[i][j] = comp
                    eval = minimax(board,depth+1, False)
                    board[i][j] = ""
                    return max(maxEval, eval)

    else:
        minEval = 10000
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                if board[i][j] == "":
                    board[i][j] = player
                    eval = minimax(board, depth+1, True)
                    board[i][j] = ""
                    return min(minEval, eval)

def findBestMove(board):
    bestVal = -1000
    bestMove = (-1,1)

    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == "":
                board[i][j] = comp

                moveVal = minimax(board, 0, False)
                board[i][j] = ""
                if(moveVal > bestVal):
                    bestMove = (i,j)
                    bestVal = moveVal
    return bestMove


def disp_board(board):
    for row in board:
        print(row)

winner = ""

while 1:
    row = int(input("Enter row(1-3): "))
    col = int(input("Enter column(1-3): "))
    row -= 1
    col -= 1
    if board[row][col] == "" and row < 3 and col < 3:
        print("You played: ")
        board[row][col] = player
        print(board)
        
        has_won, winner = won(board)
        if has_won:
            print("{} won the game".format(winner) )
            break
        elif game_over(board) and not has_won:
            print("Draw")
            break

        c_i, c_j = findBestMove(board)
        board[c_i][c_j] = comp
        print("Computer Played:")
        print(board)

        has_won, winner = won(board)
        if has_won:
            print("{} won the game".format(winner) )
            break
        elif game_over(board) and not has_won:
            print("Draw")
            break
    else: 
        print("Invalid move")

