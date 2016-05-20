def new_board():
    return [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]


def print_board(board):
    print "     |     |     "
    print " {0} | {1} | {2} ".format(board[0], board[1], board[2])
    print "-----|-----|-----"
    print " {0} | {1} | {2} ".format(board[3], board[4], board[5])
    print "-----|-----|-----"
    print " {0} | {1} | {2} ".format(board[6], board[7], board[8])
    print "     |     |     "


def play_turn(shape, pos, board):
    print shape, pos
    print pos-1
    board[pos-1] = shape
    return board



if __name__ == '__main__':
    my_board = new_board()
    print_board(my_board)
    shape = " X "
    while True:
        pos = raw_input("\n Player {0}! Please enter your position: ".format(shape))
        #play_turn(shape, int(pos), my_board)
        print_board(play_turn(shape, int(pos), my_board))

        #alternate player
        if shape == " X ":
            shape = " 0 "
        else:
            shape = " X "
