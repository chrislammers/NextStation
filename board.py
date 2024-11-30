# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:40:22 2024

@author: chris
"""


# the board:

import numpy as np

class Board:
    def __init__(self):
        self.stationType = np.array([[5,3,4,0,3,1,0,3,0,1],
                                    [0,5,0,4,0,0,5,0,4,5],
                                    [1,0,0,3,0,0,4,0,0,3],
                                    [4,0,5,0,3,2,1,1,0,4],
                                    [0,3,4,0,5,4,0,0,5,0],
                                    [5,0,4,0,1,0,0,1,0,0],
                                    [0,0,0,5,3,0,4,3,0,3],
                                    [1,0,4,1,0,5,0,0,1,5],
                                    [0,1,0,0,0,0,5,0,3,0],
                                    [3,4,0,5,1,3,0,1,0,4]])
    
    
        self.stationStart = np.array([[0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,3,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,1,0,0],
                                     [0,0,0,0,0,0,0,0,0,0],
                                     [0,0,4,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,5,0,0,0,0],
                                     [0,0,0,0,0,0,0,0,0,0]])
        
        self.touristStations = np.array([[0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,1,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0],
                                        [1,0,0,0,0,1,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,1],
                                        [0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,1,0,0,0,0,0]])
        
        
        
    # def displayBoard(self):
        
    def get_board_coords(self, board):
        
    def get_board_shapes(self, shape):
        if 1 > shape > 6:
            print("1: Circle, 2: '?', 3: Triangle, 4: Square, 5: Pentagon, 6: Tourist")
            return 0
        
        if shape == 6:
            return self.touristStations
        
        return [self.stationType == shape]
        



# print(stationStart.shape)