#!/usr/bin/env python
# coding: utf-8

# In[103]:


from IPython.display import clear_output

def print_board(board_list):
    clear_output()
    print('    |      |   ')
    print(board_list[7],"  | ",board_list[8],"  | ",board_list[9])
    print('----------------')
    print('    |      |   ')
    print(board_list[4],"  | ",board_list[5],"  | ",board_list[6])
    print('----------------')
    print('    |      |   ')
    print(board_list[1],"  | ",board_list[2],"  | ",board_list[3])
    
        


# In[148]:


print_board(board_list)


# In[108]:


def user_input(current_input):
    user_input = 'wrong'
    
    while user_input.isdigit() == False or int(user_input) not in [*range(1,10)] or int(user_input) in current_input:
        user_input = input('To select your next position, please enter a number from 0-9: ')
        if user_input.isdigit() == False:
            print('Please enter a numerical digit')
            continue
        elif int(user_input) not in [*range(1,10)]:
            print('Please enter within the range of 0-9.')
            continue
        elif int(user_input) in current_input:
            print('This position is already filled, please enter a new number.')
            continue
    return int(user_input)    
    


# In[121]:


def player_assign():
    player1 = ''
    while player1 not in ['X','O','x','o']:
        player1 = input('Player 1 choose your sign: ')
        continue
    player1 = player1.upper()
    if player1 == 'X':
        print('Player 2 your sign is O.')
        player2 = 'O'
    else:
        print('Player 2 your sign is X')
        player2 = 'X'
    return [player1, player2]


# In[124]:


player_assign()


# In[139]:


def victory_cond(board_list):
    if board_list[1]==board_list[2]==board_list[3] != ' ':
        return True
    elif board_list[4]==board_list[5]==board_list[6] != ' ':
        return True
    elif board_list[7]==board_list[8]==board_list[9] != ' ':
        return True
    elif board_list[1]==board_list[4]==board_list[7]!= ' ':
        return True
    elif board_list[2]==board_list[5]==board_list[8]!=' ':
        return True
    elif board_list[3]==board_list[6]==board_list[9]!=' ':
        return True
    elif board_list[1]==board_list[5]==board_list[9]!= ' ':
        return True
    elif board_list[3]==board_list[5]==board_list[7]!= ' ':
        return True
    else:
        return False


# In[149]:


victory_cond(board_list)


# In[136]:


def winner():
    if victory_cond(board_list) == True:
        pass


# In[131]:


def replacement(user_input,board_list,player_turn,player_sign):
    if player_turn == 1:
        board_list[user_input] = player_sign[0]
    else:
        board_list[user_input] = player_sign[1]
    
    return board_list


# In[132]:


replacement(2,board_list,1,['X','O'])


# In[154]:


def player_turn(current_player):
    player =[1,2]
    if current_player == 1:
        return player[1]
    else:
        return player[0]
    


# In[168]:


victory_condition = False

board_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
inp = []
game_on = True
player_sign = player_assign()
current_player = 0
while victory_condition is False and game_on is True:
    current_player = player_turn(current_player)
    print('This is the turn of Player ', current_player)
    current_inp = user_input(inp)
    inp.append(current_inp)
    board_list = replacement(current_inp,board_list,current_player,player_sign)
    print_board(board_list)
    victory_condition = victory_cond(board_list)
    if victory_condition == True:
        print(' ')
        print('The winner is player ',current_player)
        break
    cont_play=''
    while cont_play not in ['Y','N']:
        cont_play = input('Do you want to continue playing? Y or N ').upper()
    if cont_play == 'Y':
        pass
    elif cont_play == 'N':
        break
    


# In[ ]:




