#libraries

# import only system from os
from os import system, name

'''
The position is based of numpad of keyboards
[
 ['7','8','9']
 ['4','5','6']
 ['1','2','3']
]
 
The first player is asked if he/she wants to chose 'X' or 'O'.
The second player is assigned the value not chosen by first player.

The first player is asked a position where he/she wants to place their choice.
Then the second player is asked for chosing a position and so on until one of them wins the game.
After one of them wins the game, we ask if they want to play again

Things to consider:
1. The choice entered by player should be valid
2. After every move we should check if one of them have won the game
3. Display the board after every move
'''

# define our clear function to clear out terminal 
def clear_terminal():
  
    # for windows
    if name == 'nt':
        _ = system('cls')


#ask player_1 if he/she wants to chose 'X' or 'O'
def player_symbol_choice():
    
    #initalizing the choice variable
    choice='WRONG'   
    
    while choice not in ['X','O']:
        #asking player 1 for symbol choice
        choice=input("Player One --> Chose X or O\t:")
        
        if choice not in ['X','O']:
            
            #if choice entered by player 1 is invalid, print a message asking for valid choice
            print("Please enter a valid choice")
    if choice=="X":
        return(choice,'O')
    else:
        return('O','X')


def display_board(tic_tac_toe_board):
    #clearing the previous output
    
    clear_terminal()
    
    print("**********TIC TAC TOE BOARD**********\n\n")
    count=0
    for row in tic_tac_toe_board:
        count+=1
        print(("\t|\t").join(row))
        if count!=3:
            print("--------------------------------------\n")   
        else:
            print("\n\n")


#filled position is a set of position that has already been chosen by players
#it checks that choice entered by players are valid
def ask_position(filled_position,numpad):
    #variable initialization
    choice = "WRONG"
    
    while choice not in numpad.keys():
        choice = input("Please enter a number between [1-9] that has not been chosen\t")
        if choice in numpad.keys():
            if choice not in filled_position:
                return choice
            choice="WRONG"


#enters the player choice on the board
#player_1 is boolean value
#if player_1 == True, move is made by player_1 else it is made by player_2
def player_move(tic_tac_toe_board, player_1, position_choice, player_1_symbol, player_2_symbol):
    if player_1==True:
        tic_tac_toe_board[position_choice[0]][position_choice[1]]=player_1_symbol 
    else:
        tic_tac_toe_board[position_choice[0]][position_choice[1]]=player_2_symbol
    return tic_tac_toe_board


#player_1 == bolean value (as mentioned in above cell)
def check_if_won(tic_tac_toe_board,player_1):
    has_won=False
    if player_1==True:
        for row in tic_tac_toe_board:
            if row[0]==row[1]==row[2] and row[0]!='':
                print("Player_1 has won")
                has_won=True
                return has_won
        for itr in range(3):
            if tic_tac_toe_board[0][itr]!= '' and tic_tac_toe_board[0][itr] == tic_tac_toe_board[1][itr] == tic_tac_toe_board[2][itr]:
                print("Player_1 has won")
                has_won=True
                return has_won
        if tic_tac_toe_board[0][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][2] and tic_tac_toe_board[2][2]!='':
            print("Player_1 has won")
            has_won=True
            return has_won
        if tic_tac_toe_board[2][0] == tic_tac_toe_board[1][1] ==tic_tac_toe_board[0][2] and tic_tac_toe_board[1][1]!='':
            print("Player_1 has won")
            has_won=True
            return has_won
    else:
        for row in tic_tac_toe_board:
            if row[0]==row[1]==row[2] and row[0]!='':
                print("Player_2 has won")
                has_won=True
                return has_won
        for itr in range(3):
            if tic_tac_toe_board[0][itr] == tic_tac_toe_board[1][itr]== tic_tac_toe_board[2][itr] and tic_tac_toe_board[2][itr]!='':
                print("Player_2 has won")
                has_won=True
                return has_won
        if tic_tac_toe_board[0][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][2] and tic_tac_toe_board[2][2]!='':
            print("Player_2 has won")
            has_won=True
            return has_won
        if tic_tac_toe_board[2][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[0][2] and tic_tac_toe_board[1][1]!='':
            print("Player_2 has won")
            has_won=True
            return has_won
        
    return has_won


def replay():
    choice="Wrong"
    while choice not in ['Yes','No']:
        choice = input("\nDo you want to play again?\tEnter Yes or No\t")
        if choice not in ['Yes','No']:
            print('Enter a valid choice ie. Yes or No\t')
        else:
            return choice


#game Logic
def game():
    player_1_symbol,player_2_symbol=player_symbol_choice()

    #numpad is a dictionary that has postion on numpad as key and index on 2d list as value
    numpad={'7':[0,0],'8':[0,1],'9':[0,2],'4':[1,0],'5':[1,1],'6':[1,2],'1':[2,0],'2':[2,1],'3':[2,2]}

    #empty tic_tac_toe_board
    tic_tac_toe_board=[['','',''],['','',''],['','','']]

    #filled_position is a set 
    filled_position=set()

    has_won = False     #checks if somebody has won the game
    display_board(tic_tac_toe_board)
    player_1 = True     #boolean value to keep track of player
    while has_won == False and len(filled_position)!=9:
        position=ask_position(filled_position,numpad)        #we get numpad value
        filled_position.add(position)                        #add that value to filled_position set
        ttt_position=numpad[position]                        #position on tic_tac_toe_board
        tic_tac_toe_board=player_move(tic_tac_toe_board,player_1,ttt_position,player_1_symbol,player_2_symbol)  #move is added tothe board
        clear_terminal()

        display_board(tic_tac_toe_board)
        has_won=check_if_won(tic_tac_toe_board,player_1)
    
        player_1=not player_1
    if has_won==False:
        print("MATCH DRAW")
    replay_choice = replay()
    return replay_choice


#driver code
replay_choice='Yes'
while replay_choice=='Yes':
    clear_terminal()
    replay_choice=game()
print("\n\t**********GAME OVER**********\t\n")