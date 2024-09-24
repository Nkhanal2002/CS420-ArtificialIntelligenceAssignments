# Tic-tac-toe Minimax assignment
#   
#   Board spaces are identified by integers 1-9, as follows:
#       1 | 2 | 3
#      ---+---+---
#       4 | 5 | 6
#      ---+---+---
#       7 | 8 | 9
#


import sys
from tttlib import *
from players import *
from minimax import minimaxBot


HELP = '''
You must have 2 arguments after the name of this script:
the first argument is the identity of the first player (X's),
and the second argument is the identity of the second player (O's).

Player identity must be one of the following:
 human (or H)
 random (or R)
 minimax (or M)
'''

BOTS = {
    'H': humanPlayer,
    'R': randomBot,
    'O': oneBot,
    'M': minimaxBot,
    'human': humanPlayer,
    'random': randomBot,
    'one': oneBot,
    'minimax': minimaxBot
}




###########################################
## start
if __name__=='__main__':
    if len(sys.argv)==3 and (sys.argv[1] in BOTS) and (sys.argv[2] in BOTS):
        play(BOTS[sys.argv[1]],BOTS[sys.argv[2]])
    else:
        print(HELP)

