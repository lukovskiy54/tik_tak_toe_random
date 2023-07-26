import random

def display_board(board):
    for j in range(3):
        print("+-------+-------+-------+")
        for i in range(3):
            print("|       |       |       |")
            if i == 1:
                print(
                    "|  ",
                    board[i - 1][j],
                    "  |  ",
                    board[i][j],
                    "  |  ",
                    board[i + 1][j],
                    "  |",
                )
    print("+-------+-------+-------+")

def enter_move(board, is_bot=0):
    if is_bot == 0:
        while True:
            # Get the move input from the user
            move = input("Enter number of cell:")
            if len(move) == 1 and move > "-1" and move <= "9":
                # Convert the move for indexes of list
                move = int(move) - 1
                row = move // 3
                col = move % 3
                if (row, col) not in make_list_of_free_fields(board):
                    # Check if the selected cell is already taken
                    print("Tile already taken, try again")
                    continue
                else:
                    # Update the board with the player's move
                    board[col][row] = 0
                    return
            else:
                print("Wrong input, try again")
                continue
    else:
        count = 1
        while True:
            if count >= 2:
                # Bot tries to place 'X' at the center if available after two moves
                if (1, 1) in make_list_of_free_fields(board):
                    board[1][1] = "X"
                break
            else:
                # Bot makes a random move 
                row = random.choice([0, 2])
                col = random.choice([0, 2])
                count += 1
            if (row, col) in make_list_of_free_fields(board):
                # Update the board with the bot's move
                board[col][row] = "X"
                break
            else:
                continue

def make_list_of_free_fields(board):
    lst = []
    for j in range(3):
        for i in range(3):
            # Collect all free cells (not marked with 0 or 'X') into a list
            if board[i][j] != 0 and board[i][j] != "X":
                lst.append((j, i))

    return lst

def match_result(var):
    # Display the result based on the value of var (0 for player win, 'X' for bot win)
    if var == 0:
        print("You won!")
    else:
        print("You lost!")

def match_state(board):
    for i in range(3):
        # Check rows and columns for a match
        if board[0][i] == board[1][i] == board[2][i] or board[i][0] == board[i][1] == board[i][2]:
            match_result(board[i][0])
            return True
    # Check diagonals for a match
    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
        match_result(board[1][1])
        return True
    # If no match, check for a draw
    return check_draw(board)

def check_draw(board):
    if len(make_list_of_free_fields(board)) > 0:
        return 0
    else:
        # If no free cells left, it's a draw
        print("Draw!")
        return -1

def main():
    board = [[j for j in range(3)] for i in range(3)]
    count = 1
    for j in range(3):
        for i in range(3):
            # Initialize the board with numbers from 1 to 9
            board[i][j] = count
            count += 1
    print("Who will start?:")
    inp = input("Print YES to start first: ")
    if inp != "YES":
        # If the player doesn't start first, let the bot make the first move
        enter_move(board, 1)
    while True:
        display_board(board)
        res = match_state(board)
        if res == 1 or res == -1:
            # If the game is won or drawn, break the loop
            break
        enter_move(board, 0) 
        display_board(board)
        res = match_state(board)
        if res == 1 or res == -1:
            break
        enter_move(board, 1)

if __name__ == "__main__":
    main()
