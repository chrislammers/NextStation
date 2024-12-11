# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:40:22 2024

@author: chris
"""


# the board:

import numpy as np
import stations

class Board:
    def __init__(self):
        # List of all Station objects fo this board
        self.station_list = []
        
        
        # these three arrays describe the entire board
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
        
        # basic station index for the station_type to text
        self.station_index = {1: "Circle", 2: "All", 3: "Triangle",
                              4: "Square", 5: "Pentagon"}
        
        self.boardShape = self.stationType.shape
        
        
    # def display_board(self):
        
    def get_board_coords(self):
        # Loop through stationType
        # create a Station object for each non-zero
        #   check touristStations
        # Use Station.createConnections
        for yy in range(len(self.stationType)):
            for xx in range(len(self.stationType[yy])):
                if self.stationType[xx][yy] != 0:
                    new_station = stations.Station(xx,yy,
                                                   self.stationType[xx][yy],
                                                   self.touristStations[xx][yy]
                                                   )
                    self.station_list.append(new_station)
        return
        
    def get_board_shapes(self, shape):
        if 1 > shape > 6:
            print("Error: pick a number between 1 and 6")
            print("1: Circle, 2: '?', 3: Triangle, 4: Square, 5: Pentagon, 6: Tourist")
            return [[0]]
        
        if shape == 6:
            return self.touristStations
        
        return [self.stationType == shape]
    
    def draw(self,screen,x=0,y=0):
        # print(self.stationType.shape)
        # Use the Station.draw() function!
        
        return
        
        
# print(stationStart.shape)