def update_board(player, input_option, my_list):
    #check index to see if it already has an 'x' or 'o'
    index_option = input_option - 1
    if my_list[index_option] == 'X' or my_list[index_option] == 'O':
        input_option = int(input("That space has already been taken. Please choose a square (1-9): "))
    
    #if player X, change selection to X
    if player == "X":
        for i in range(len(my_list)):
            if input_option == my_list[i]:
                my_list[i] = "X"
        return my_list

    #if player O, change selection to O
    elif player == "O":
        for i in range(len(my_list)):
            if input_option == my_list[i]:
                my_list[i] = "O"           
        return my_list
