
import random

def display_board(board):
    print('\n'*100)
    lines = {'a':f'|  {board[6]}  |  {board[7]}  |  {board[8]}  |  ','b':f'|  {board[3]}  |  {board[4]}  |  {board[5]}  |  ','c':f'|  {board[0]}  |  {board[1]}  |  {board[2]}  |  ','d':'-------------------'}
    print(lines['d'] + '\n' + lines['a'] + '\n'+ lines['d'] + '\n' + lines['b'] + '\n' + lines['d']+ '\n' + lines['c'] + '\n'+ lines['d'] )

def player_input():
    player1 = ''
    player2 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input("Player 1, please pick a marker. X or O: ")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return(player1,player2)

def place_marker(board, marker, position):
    #Places marker on board
    board[position - 1] = marker

def win_check(board, marker):
    return ((board[0] == board[1] == board[2] == marker) or 
    (board[3] == board[4] == board[5] == marker) or 
    (board[6] == board[7] == board[8] == marker) or
    (board[0] == board[3] == board[6] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[0] == board[4] == board[8] == marker) or
    (board[2] == board[4] == board[6] == marker))

def space_check(board, position):
    #Returns True if space is open
    return board[position - 1] == ' '

def choose_first():
    #Randomly select first player
    if random.randint(1,2) == 1:
        return('Player 1')
    else:  
        return('Player 2')
        
def full_board_check(board):
    #Returns True if board is full
    return not ' ' in board

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Where would you like your marker? (1-9): '))
    return position

def replay():
    #asks player if they want to play again
    replay = input('Do you want to play again? Yes or No: ')
    return replay == 'Yes'


print('Welcome to Tic Tac Toe')

while True:
    the_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1,player2 = player_input()
    current_player = choose_first()

    print(current_player + ' will go first')
    
    play_game = input('Ready to play? y or n: ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if current_player == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1,position)
            if win_check(the_board,player1):
                display_board(the_board)
                print('Player 1 wins!')
                game_on == False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game ends in a tie')
                    game_on == False
                    break
                else:
                    current_player = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2,position)
            if win_check(the_board,player2):
                display_board(the_board)
                print('Player 2 wins!')
                game_on == False
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game ends in a tie')
                    game_on == False
                    break
                else:
                    current_player = 'Player 1'
    if not replay():
        break
