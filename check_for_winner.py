

def check_winner(my_list, winner):
    #check to see if the top row is the same
    if my_list[0] == my_list[1] and my_list[1] == my_list[2]:
        winner = True
        
    #check to see if the middle row is the same
    elif my_list[3] == my_list[4] and my_list[4] == my_list[5]:
        winner = True
  
    #check to see if the bottom row is the same
    elif my_list[6] == my_list[7] and my_list[7] == my_list[8]:
        winner = True

    #check to see if the left column is the same
    elif my_list[0] == my_list[3] and my_list[3] == my_list[6]:
        winner = True

    #check to see if the center column is the same
    elif my_list[1] == my_list[4] and my_list[4] == my_list[7]:
        winner = True
   
    #check to see if the right column is the same
    elif my_list[2] == my_list[5] and my_list[5] == my_list[8]:
        winner = True

    #check to see if diagonal_1 is the same
    elif my_list[0] == my_list[4] and my_list[4] == my_list[8]:
        winner = True
    
    #check to see if diagonal_1 is the same
    elif my_list[2] == my_list[4] and my_list[4] == my_list[6]:
        winner = True
   
    else:
        winner = False

    return winner