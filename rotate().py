import sys
from copy import deepcopy

def rotate(state,n):

    successor=[]
    dropPiece=[]
    for col in range(0,n):
        new_state = deepcopy(state)
        # SHIFTING EACH ELEMENT
        if new_state[(n+3)-1][col]!=".":
            removed_element = new_state[(n+3)-1][col]
            dropPiece.append(-(col+1))
            new_state[(n+3) - 1][col] = "."
            for i in range((n+3)-1, 0, -1):
                if new_state[i - 1][col] != ".":
                    new_state[i][col] = new_state[i - 1][col]
                    new_state[i - 1][col] = "."

            # DROPPING REMOVED PEBBLE
            for j in range((n+3) - 1, 0, -1):
                flag = 0
                if new_state[j][col] == ".":
                    new_state[j][col] = removed_element
                    flag = 1
                    break
            if flag == 0:
                new_state[0][col] = removed_element

            successor.append(new_state)

    print successor
    print dropPiece



state=[['.','.','.','x'],['x','.','.','x'],['o','.','o','o'],['x','.','o','x'],['x','x','x','x'],['o','o','o','o'],['x','o','x','o']]
print "Initial board is: {}".format(state)
rotate(state,4)

#
#
# # TAKING INPUTS AS COMMANDLINE
# n=int(sys.argv[1])
# state_string=sys.argv[2]
#
# # CONVERTING STRING TO A GAME BOARD
# sublist=[]
# initial_board=[]
# k=0
# for j in range(n+3):
#     sublist=[]
#     for j in range(k,k+n):
#         sublist.append(state_string[j])
#     initial_board.append(sublist)
#     k+=n
# print "Initial board is: {}".format(initial_board)
# rotate(initial_board,n)