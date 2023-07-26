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
                move = int(move)-1 
                row = move // 3
                col = move % 3
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
            if(count==2):
                if(1,1) in make_list_of_free_fields(board):
                    board[1][1] = 'X'
                    break
                else:
                    count +=1
                    continue
            else:    
                row = random.choice([0, 2]) 
                col = random.choice([0, 2])
                count += 1
            if(row,col) in make_list_of_free_fields(board):
                board[col][row] = 'X'
                break
            else:
                continue



def make_list_of_free_fields(board):
    lst = []
    for j in range(3):
        for i in range(3):
            if(board[i][j] != 0 and board[i][j] != 'X'):
                lst.append((j,i))

    return lst        
def match_result(var):
    if(var == 0):
        print("You won!")
    else : print("You lost!")    


def match_state(board):
    for i in range(3):
        if(board[0][i] == board[1][i] and board[2][i] == board [1][i]):
            match_result (board[0][i])
            return 1
        if(board[i][0] == board[i][1] and board[i][2] == board [i][1]):
            match_result(board[i][0])
            return 1
    if(board[0][0] == board[1][1] == board[2][2]):
        match_result(board[0][0])  
        return 1 
    if(board[2][0] == board[1][1] == board[0][2]):
        match_result(board[2][0])    
        return 1
    return check_draw(board)
    
def check_draw(board):
    if(len(make_list_of_free_fields(board))>0):
        return 0
    else:
        print("Draw!")
        return -1
def main():
    board = [[j for j in range(3)] for i in range(3)]
    count = 1
    for j in range(3):
        for i in range(3):
            board[i][j] = count
            count +=1
    print("Who will start?:")
    inp = input('Print YES to start first: ') 
    if(inp != 'YES'):
        enter_move(board, 1)
    while(True):        
        display_board(board)
        res = match_state(board)
        if(res == 1 or res == -1):break   
        enter_move(board, 0) 
        display_board(board) 
        res = match_state(board)
        if(res == 1 or res == -1):break  
        enter_move(board, 1)
main()    
input()
