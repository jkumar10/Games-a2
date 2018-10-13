# Betsy

A popular game in a certain exotic, far-of land1 is called Betsy. It's played on a vertical board that is
n squares wide and n + 3 squares tall (where n is often 5 for beginners, but can grow quite large in the
professional tournaments). The board starts an empty, with each of the two players (red and blue) given
1
2n * (n + 3) pebbles of their own color. Blue goes first, choosing one of two possible types of moves.
• Drop: Choose one of the n columns, and drop a blue pebble into that column. The pebble falls to
occupy the bottom-most empty square in that column. The player is not allowed to choose a column
that is already full (i.e., already has n + 3 pebbles in it).
• Rotate: Choose one of the n columns, remove the pebble from the bottom of that column (whether
red or blue) so that all pebbles fall down one square, and then drop that same pebble into the top of
that column. The player is not allowed to choose an empty column for this type of move.
After making a move, blue checks the top n rows of the board to see if they have completed a row of n blue
pebbles, a column of n blue pebbles, or one of the two diagonals of blue pebbles. The bottom three rows
of the board are ignored during this check. If a row, column, or diagonal has been completed in blue, blue
wins! Otherwise, red makes the same check and wins if any row, column, or diagonal has been completed
with red. Note this means that if blue completes a row, column, or diagonal of blue pebbles, they win even
if they have also completed a row, column, or diagonal of red. If no one has won, player red takes their turn,
either dropping a red pebble into an incomplete column or rotating a non-empty column. Figure 1 shows
several sample moves from a game in progress, with n = 3.
Your task is to write a Python program that plays Betsy well. Use the minimax algorithm with alpha-beta
search and a suitable heuristic evaluation function.
Your program should accept a command line argument that gives the value of n, and the current state of the
board as a string of n  (n + 3) characters (from top to bottom and left to right, i.e. in row-major order),
each of which is one of: . for an empty square, x for blue pebble, and o for a red pebble. For example, the
encoding of the board in Figure 1(a) would be:
...x..o.ox.oxxxoxo
More precisely, your program will be called with three command line parameters: (1) the value of n, (2) the
current player (x or o), (3) the state of the board, encoded as above, and (4) a time limit in seconds. Your
program should then decide a recommended single move for the given player from the given current board
state, and display the recommend move and the new state of the board after making that move, within the
number of seconds specied, in a format like this:
move new board
where move is either a positive number indicating a column (ranging from 1 to n) in which to drop a pebble,
or a negative number indicating a column to rotate (e.g., -3 means to rotate column 3). Displaying multiple
lines of output is ne as long as the last line is the recommended move and board state.
For example, two runs of your program (corresponding to the rst two moves of Fig. 1) might look like:2
[djcran@macbook]$ ./betsy.py 3 o ...x..o.ox.oxxxo.o 5
Shhh... I'm thinking!
Hey, in the time it takes you to read this sentence, I'll have considered
5 billion board positions. But it's cute that you're still trying to beat me...
I'd recommend dropping a pebble in column 2.
2 ...x..o.oxooxxxoxo
[djcran@macbook]$ ./betsy.py 3 x ...x..o.oxooxxxoxo 5
Shhh... I'm thinking!
Sure, you could unplug me, but within 500ms I can command every computer on Earth
to delete any trace that you ever existed. You're welcome.
I'd recommend rotating column 1
-1 ...o..x.ooooxxxxxo
