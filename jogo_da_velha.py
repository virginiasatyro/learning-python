def display_instructions():
    print(" ")
    print("---------------- TIC TAC TOE ----------------")
    print(" ")
    print("7 | 8 | 9")
    print("-   -   -")
    print("4 | 5 | 6")
    print("-   -   -")
    print("1 | 2 | 3")
    print(" ")
	
# functions that prints the board 
def print_board():
    lin = len(board)    # counts the number of lines 
    col = len(board[0]) # counts the number os elements in a line 
    for i in range(lin):
        for j in range(col):
            if(j == col - 1):
                print("%d" %board[i][j])
            else:
                print("%d" %board[i][j], end = " | ")
        print(" -   -   -")
    print(" ")


# change the player (1 or -1)
def change_player(p): # p is for player
    if (p == 1):
        p = -1
    else:
        p = 1
    return p # return the player

# function to choose the space on the board
def choose_space(choice, p):
    L = []
    for i in L:
        if i == choice:
            print("Space already taken! Choose another one!")
            return 0
        else:
            L.append(choice)
    if choice   == 7: board[0][0] = p
    elif choice == 8: board[0][1] = p
    elif choice == 9: board[0][2] = p
    elif choice == 4: board[1][0] = p
    elif choice == 5: board[1][1] = p
    elif choice == 6: board[1][2] = p
    elif choice == 1: board[2][0] = p
    elif choice == 2: board[2][1] = p
    elif choice == 3: board[2][2] = p
    else:
        print("This move is not valid! Choose another one!")	
        return 0	
    return 1
	
# function that verifies if the game is won
def game_win():
    # winnning by lines
    sum = board[0][0] + board[0][1] + board[0][2] 
    if check_sum(sum) == 1: return 1
    sum = board[1][0] + board[1][1] + board[1][2]
    if check_sum(sum) == 1: return 1
    sum = board[2][0] + board[2][1] + board[2][2]
    if check_sum(sum) == 1: return 1
	
    # winnning by columns
    sum = board[0][0] + board[1][0] + board[2][0]
    if check_sum(sum) == 1: return 1
    sum = board[0][1] + board[1][1] + board[2][1] 
    if check_sum(sum) == 1: return 1
    sum = board[0][2] + board[1][2] + board[2][2]  
    if check_sum(sum) == 1: return 1
	
	# winnning by diagonal
    sum = board[0][0] + board[1][1] + board[2][2]
    if check_sum(sum) == 1: return 1
    sum = board[0][2] + board[1][1] + board[2][0]
    if check_sum(sum) == 1: return 1
    
# checks the sum os numbers in columns - winners always get 3 or -3
def check_sum(sum):
    if(sum == 3):
        return 1
    elif(sum == -3):
        return 1
    else:
        return 0
# function that verifies if the game is over without a winner
# def game_over(): 
 
 
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # create the game board 
 
display_instructions()
playing = 1 # indicates if the game is being played 
choice = 0
player = 1 # player 1 always iniciates the game 	

while(playing == 1): 
    choice = choice + 1
    if(choose_space(choice, player) == 0):
        playing = 0
    print_board()
	
    if game_win() == 1:
        print("Vitoria")
        playing = 0
    else:
        print("Jogo continua...")
		
    player = change_player(player)
# playing = 0 # ends the game