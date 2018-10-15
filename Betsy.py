import sys
from copy import deepcopy

# METHOD TO ROTATE THE BOARD
def rotate(state,n):
    successor = []
    dropPiece = []
    for col in range(0, n):
        new_state = deepcopy(state)
        # SHIFTING EACH ELEMENT
        if new_state[(n + 3) - 1][col] != ".":
            removed_element = new_state[(n + 3) - 1][col]
            dropPiece.append(-(col + 1))
            new_state[(n + 3) - 1][col] = "."
            for i in range((n + 3) - 1, 0, -1):
                if new_state[i - 1][col] != ".":
                    new_state[i][col] = new_state[i - 1][col]
                    new_state[i - 1][col] = "."

            # DROPPING REMOVED PEBBLE
            for j in range((n + 3) - 1, 0, -1):
                flag = 0
                if new_state[j][col] == ".":
                    new_state[j][col] = removed_element
                    flag = 1
                    break
            if flag == 0:
                new_state[0][col] = removed_element

            successor.append(new_state)
    return dropPiece,successor

# METHOD TO DROP THE BOARD
def drop(state,n, turn):
    new_state=deepcopy(state)
    finalList=[]
    addPiece=[]
    for i in range(n+2,-1,-1):
        for j in range(n-1,-1,-1):
            if(state[i][j]=="." and j not in addPiece):
                new_state[i][j]=turn
                addPiece.append(j)
                finalList.append(new_state)
                new_state=deepcopy(state)
    return addPiece,finalList

# SUCCESSOR RETURNS ALL THE SUCCESSORS OF THE CURRENT STATE
def successor(board,n,turn):
    succ=[]
    move=[]
    move1,l1=rotate(board,n)
    move2,l2=drop(board,n,turn)
    for r in l1:
        succ.append(r)
    for d in l2:
        succ.append(d)
    for m1 in move1:
        move.append(m1)
    for m2 in move2:
        move.append(m2)

    return succ,move

# METHOD TO CHECK IF THE CURRENT STATE IS A GOAL STATE
def isGoal(board,n):
    # CHECKING ALL ROWS
    i=0
    for row in board:
        if all(element == 'x' for element in row)==True and i<n:
            return True
        elif all(element == 'o' for element in row) == True and i<n:
            return True
        i += 1

    # CHECKING ALL COLUMNS
    lcol=[]
    for i in range(0,n):
        del lcol[:]
        for j in range(0,n):
            lcol.append(board[j][i])
        if all(element == 'x' for element in lcol) == True or all(element == 'o' for element in lcol) == True:
            return True

    # CHECKING ALL DIAGONALS
    leftdiag=[]
    rightdiag=[]
    for i in range(0,n):
        for j in range(0,n):
            leftdiag.append(board[i][j]) if i==j else False
            rightdiag.append(board[i][j]) if i+j==n-1 else False
    if all(element == 'x' for element in leftdiag) == True or all(element == 'o' for element in leftdiag) == True:
        return True
    if all(element == 'x' for element in rightdiag) == True or all(element == 'o' for element in rightdiag) == True:
        return True

# MINIMAX ALGORITHM Include time as well
def minimax(state,n,depth,alpha,beta, player):
    if depth ==0 or isGoal(state,n):
        # return heuristic value
        return 50
    if player=="x":
        maxEval=-100000000
        for child in successor(state,n,"x"):
            eval=minimax(child,n,depth-1,alpha,beta,"o")
            maxEval=max(maxEval,eval)
            alpha=max(alpha,eval)

            if beta<=alpha:
                break
        return maxEval
    else:
        minEval=100000000
        for child in successor(state,n,"o"):
            eval = minimax(child,n, depth - 1, alpha, beta, "x")
            minEval=min(minEval,eval)
            beta=min(beta,eval)
            #print(minEval)
            if beta<=alpha:
                break
        return minEval



# TAKING INPUTS AS COMMANDLINE
n=int(sys.argv[1])
state_string=sys.argv[2]

# CONVERTING STRING TO A GAME BOARD
sublist=[]
initial_board=[]
k=0
for j in range(n+3):
    sublist=[]
    for j in range(k,k+n):
        sublist.append(state_string[j])
    initial_board.append(sublist)
    k+=n


# WILL RETURN TRUE IF GOAL FOUND OTHERWISE FALSE OR NONE
a,b=successor(initial_board,n,'x')
print a
print b
#print isGoal(initial_board,n)
#print minimax(initial_board,n,3,-100000000,100000000,"x")