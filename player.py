# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 23:53:13 2022

@author: rijuj
"""

from evaluator import Evaluator
from config import WHITE, BLACK
from minimax import Minimax
import random
import qTable
import numpy as np


def change_color(color):
    if color == BLACK:
        return WHITE
    else:
        return BLACK


class Human:

    """ Minimax player at the moment, but can be configured for human, random and self AI also"""

    def __init__(self, gui, color="black"):
        self.color = color
        self.gui = gui
        #self.color = color
        self.previousMove = (-1,-1)
        self.previousReward = 0
        self.reward = 0
        self.qTable = qTable.QTable()
        self.winCount = 0
        self.loseCount = 0
        self.drawCount = 0
        self.depthLimit = 3
        evaluator = Evaluator()
        self.minimaxObj = Minimax(evaluator.score)
        
    def win(self):
        self.winCount += 1
        
    def lose(self):
        self.loseCount += 1    
        
    def draw(self):
        self.drawCount += 1
    
    def getWin(self):
        return self.winCount
    
    def getLose(self):
        return self.loseCount
    
    def getDraw(self):
        return self.drawCount
        
    def get_color(self):
        return self.color
    

    def get_move(self): #, currentTable):
        """ Uses gui to handle mouse
        """
        ######################
        # CODE FOR RANDOM AI #
        ######################
        #validMoves = self.current_board.get_valid_moves(self.color)
        
        #this is code for  getting mouse input. to play manually. 
        ##while True:
        ##    move = self.gui.get_mouse_input()
        ##    if move in validMoves:
        ##        break
        ##move = random.sample(validMoves, 1)
        ##self.current_board.apply_move(move[0], self.color)
        ##return self.current_board
        return self.minimaxObj.minimax(self.current_board, None, self.depthLimit, self.color,
                                       change_color(self.color))


    def get_current_board(self, board):
        self.current_board = board


class Computer(object):

    def __init__(self, color):
        self.color = color
        self.previousMove = (-1,-1)
        self.previousReward = 0
        self.reward = 0
        self.qTable = qTable.QTable()
        self.winCount = 0
        self.loseCount = 0
        self.drawCount = 0
        
    def win(self):
        self.winCount += 1
        
    def lose(self):
        self.loseCount += 1    
        
    def draw(self):
        self.drawCount += 1
    
    def getWin(self):
        return self.winCount
    
    def getLose(self):
        return self.loseCount
    
    def getDraw(self):
        return self.drawCount
        
    def get_color(self):
        return self.color

    def get_current_board(self, board):
        self.current_board = board

    def get_move(self, epsilon):
        validMoves = self.current_board.get_valid_moves(self.color)
        highest = -500
        """checking whether to take random move or make own decision"""
        if np.random.random() <= epsilon:
            randMove = random.randrange(len(validMoves))
            move = validMoves[randMove]
        else:
            """if not random, then choose the possible move that has the highest value in the Qtable"""
            qTableInstance = self.qTable.get_qTable()
            for (x,y) in validMoves:
                if qTableInstance[x][y] > highest:
                    highest = qTableInstance[x][y]
                    move = (x,y)
        """update the Qtable with new reward knowledge"""
        self.previousReward = self.reward
        self.reward = self.current_board.apply_move(move, self.color) *2
        (x,y) = move
        self.qTable.qTable_update(x, y, 0.5, 0.9, self.previousMove, self.previousReward)
        self.previousMove = move
        
        
        return self.current_board
        


class RandomPlayer (Computer):

    def get_move(self):
        x = random.sample(self.current_board.get_valid_moves(self.color), 1)
        return x[0]
