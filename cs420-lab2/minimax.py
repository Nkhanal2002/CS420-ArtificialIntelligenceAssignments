# Tic-tac-toe minimax bot

# CS420 - Assignment 2
#  Name: Narayan Khanal


import random
from tttlib import *


def minimaxBot(mySpaces:set,opponentSpaces:set,emptySpaces:set):
    '''Returns an integer 1-9 to indicate current move, based on this board layout:
                1 | 2 | 3
                ---+---+---
                4 | 5 | 6
                ---+---+---
                7 | 8 | 9
       Each argument (mySpaces, opponentSpaces, and emptySpaces)
         is a set of integers, indicating the spaces taken by me,
         by my opponent, and untaken spaces on the board.
       Uses minimax algorithm to find optimal move at each turn.
    '''
    
    if len(emptySpaces) == 9: return 1
    bestVal = -100000
    for availableSpace in emptySpaces:
        actionVal = minimax(mySpaces|{availableSpace}, opponentSpaces, emptySpaces - {availableSpace})
        
        if actionVal > bestVal:
            bestAction = availableSpace
            bestVal = actionVal
        
    return bestAction

def minimax(mySpaces:set,opponentSpaces:set,emptySpaces:set, maximizingPlayer = False):
    
    if playerWins(mySpaces): #player wins
        return 1
    if playerWins(opponentSpaces): #player lose
        return -1
    if len((emptySpaces)) == 0: # game draw
        return 0
    
    if maximizingPlayer:
        val = -100000
        for availableSpace in emptySpaces:
            val = max(val, minimax(mySpaces|{availableSpace}, opponentSpaces, emptySpaces-{availableSpace}, False))
            
        return val
    
    else: #minimizing player
        val = 100000
        for availableSpace in emptySpaces:
            val = min(val, minimax(mySpaces|{availableSpace}, opponentSpaces, emptySpaces-{availableSpace}, True))
            
        return val
    


