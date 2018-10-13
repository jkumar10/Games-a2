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






n=5
initial_board=[
                [0,0,0,0,0],
                [0,0,0,0,0],
                ['x','x','x','x','x'],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]

            ]

print isGoal(initial_board,5)