# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 23:53:13 2022

@author: rijuj
"""


class QTable:
    
    def __init__(self):
        """QTable is now loaded with the latest data after training with Minimax AI"""
        self.qTable = [[-1.28, -0.99,  1.34, -0.01,  0.89,  4.25, -1.85, -0.88],
 [-3.34,  1.66,  1.93,  0.13,  0.71, -0.09, -0.02, -0.32],
 [ 5.18,  0.39,  2.82, -0.77,  1.78,  3.85, -0.09, -1.19],
 [ 8.99,  2.92,  2.33,  1.,    1.,   -0.75,  2.82,  0.8 ],
 [-1.73, -0.72,  1.81,  1.,    1.,   -0.04,  4.35, -0.14],
 [-2.63,  1.4,   1.42,  1.56,  1.53,  0.84,  1.58,  0.22],
 [ 1.86, -0.73,  1.7,   0.69,  0.9,   0.66,  4.76,  0.96],
 [ 3.17,  1.86,  0.93, -1.8,   2.69, -1.03,  0.95,  6.44]]
        


        
    def qTable_update(self, x, y, lr, df, previousMove, previousReward):
        """ updates the qValue of the previous move with the accummulated reward from current state"""
        newPreviousMoveTargetValue = previousReward + df* self.qTable[x][y]
        prevX, prevY = previousMove
        if prevX != -1:
            newPreviousMoveCurrentValue = self.qTable[prevX][prevY] + lr * (newPreviousMoveTargetValue - self.qTable[prevX][prevY])
            self.qTable[prevX][prevY] = round((newPreviousMoveTargetValue - newPreviousMoveCurrentValue),2)
        
    def get_qTable(self):
        return self.qTable
        
        