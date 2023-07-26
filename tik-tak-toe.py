import random
def display_board(board):
    for j in range(3):
        print("+-------+-------+-------+")
        for i in range(3):
            print("|       |       |       |")
            if(i == 1):
                print("|  ",board[i-1][j],"  |  ",board[i][j],"  |  ",board[i+1][j],"  |")
    print("+-------+-------+-------+")


def enter_move(board, bot = 0):
    if(bot == 0):
        while True :
            move = input("Enter number of cell:")
            if  len(move) == 1 and move > '-1' and move <= '9' :
                # Convert the move to zero-based index for list indexes
                move = int(move)-1 
                row = move // 3
                col = move % 3
                # Check if the selected cell is already taken
                if (row,col) not in make_list_of_free_fields(board):
                    print("Tile already taken, try again")
                    continue
                else:
                    board[col][row] = 0
                    return
            else: 
                print("Wrong input, try again")    
                continue                       
    else:
        count = 1
        while True :
            if(count>2):
                row = random.randint(1,10) 
                col = random.randint(1,10)
            else:    
                # Bot tries to place 'X' at the corners if available in two first moves
                row = random.choice([0, 2]) 
                col = random.choice([0, 2])
                count += 1
            # Update the board with the bot's move    
            if(row,col) in make_list_of_free_fields(board):
                board[col][row] = 'X'
                break
            else:
                continue


# Collect all free cells (not marked with 0 or 'X') into a list
def make_list_of_free_fields(board):
    lst = []
    for j in range(3):
        for i in range(3):
            if(board[i][j] != 0 and board[i][j] != 'X'):
                lst.append((j,i))

    return lst    

# Display the result based on the value of var (0 for player win, 'X' for bot win)    
def match_result(var):
    if(var == 0):
        print("You won!")
    else : print("You lost!")    


def match_state(board):
    # Check rows and columns for a match
    for i in range(3):
        if(board[0][i] == board[1][i] and board[2][i] == board [1][i]):
            match_result (board[0][i])
            return 1
        if(board[i][0] == board[i][1] and board[i][2] == board [i][1]):
            match_result(board[i][0])
            return 1
    # Check diagonals for a match    
    if(board[0][0] == board[1][1] == board[2][2]):
        match_result(board[0][0])  
        return 1 
    if(board[2][0] == board[1][1] == board[0][2]):
        match_result(board[2][0])    
        return 1
    # If no match, check for a draw
    return check_draw(board)
    
def check_draw(board):
    # If no free cells left, it's a draw
    if(len(make_list_of_free_fields(board))>0):
        return 0
    else:
        print("Draw!")
        return -1
    

def main():
    board = [[j for j in range(3)] for i in range(3)]
    count = 1
    # Initialize the board with numbers from 1 to 9
    for j in range(3):
        for i in range(3):
            board[i][j] = count
            count +=1
    # If the player dont want to start first, let the bot make the first move        
    print("Who will start?:")
    inp = input('Print YES to start first or anything else if you want bot to start: ') 
    if(inp != 'YES'):
        enter_move(board, 1)
    while(True):        
        display_board(board)
        res = match_state(board)
        # If the game is won or drawn, break the loop
        if(res == 1 or res == -1):break   
        enter_move(board, 0) 
        display_board(board) 
        res = match_state(board)
        if(res == 1 or res == -1):break  
        enter_move(board, 1)
main()
input()














