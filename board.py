# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:40:22 2024

@author: chris
"""


# the board:

import numpy as np
import stations

# Defaults (these represent the Next Station: London original map)
stationTypeArray = np.array([[5,3,4,0,3,1,0,3,0,1],
                            [0,5,0,4,0,0,5,0,4,5],
                            [1,0,0,3,0,0,4,0,0,3],
                            [4,0,5,0,3,2,1,1,0,4],
                            [0,3,4,0,5,4,0,0,5,0],
                            [5,0,4,0,1,0,0,1,0,0],
                            [0,0,0,5,3,0,4,3,0,3],
                            [1,0,4,1,0,5,0,0,1,5],
                            [0,1,0,0,0,0,5,0,3,0],
                            [3,4,0,5,1,3,0,1,0,4]])

stationStartArray = np.array([[0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,3,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,4,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,5,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0]])

stationAttractionsArray = np.array([[0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,1,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [1,0,0,0,0,1,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,1],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,1,0,0,0,0,0]])

stationRegionArray = np.array([[0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0],
                                [1,1,1,1,0,0,0,0,0,0],
                                [1,1,1,1,1,0,0,1,1,1],
                                [1,1,1,1,1,1,1,1,1,1],
                                [1,1,1,1,1,1,1,1,1,1],
                                [1,1,1,1,1,1,1,1,1,1],
                                [1,1,1,1,1,1,1,1,1,1]])


class Board:
    def __init__(self, staList = [], staType=stationTypeArray, staStart=stationStartArray, staAttr=stationAttractionsArray, staReg=stationRegionArray):
        # TODO: All arrays should be passed in as default values. 
        #   there will be an option to generate the board from the arrays or the list of Station objects
        # List of all Station objects fo this board
        self.station_list = staList.copy()
        
        
        # these three arrays describe the entire board
        self.stationType = staType.copy()
    
    
        self.stationStart = staStart.copy()
        
        self.stationAttractions = staAttr.copy()
        
        # basic station index for the station_type to text
        self.station_index = {1: "Circle", 2: "All", 3: "Triangle",
                              4: "Square", 5: "Pentagon"}
        
        
        # station_region will be global. I'll leave it in here
        # TODO: Add a region board (map)
        #   n by n array containing 1 to x, where x is the number of regions
        self.station_region = np.array([[10,1,1,2,2,2,2,3,3,11],
                                        [1,1,1,2,2,2,2,3,3,3],
                                        [1,1,1,2,2,2,2,3,3,3],
                                        [4,4,4,5,5,5,5,6,6,6],
                                        [4,4,4,5,5,5,5,6,6,6],
                                        [4,4,4,5,5,5,5,6,6,6],
                                        [4,4,4,5,5,5,5,6,6,6],
                                        [7,7,7,8,8,8,8,9,9,9],
                                        [7,7,7,8,8,8,8,9,9,9],
                                        [12,7,7,8,8,8,8,9,9,13]])
        
        # When generating station maps, I think river boundaries could also be generated
        #   Using map data.
        # TODO: Add a thames map
        #   n by n array with 0 on the north side of the thames, 1 on south
        self.stationRegion = staReg
        
    # def display_board(self):
        
    def get_board_coords(self):
        # TODO: Add a try/catch to make sure there are sufficient arrays
        
        # Loop through stationType
        # create a Station object for each non-zero
        #   check stationAttractions
        # Use Station.createConnections
        for yy in range(len(self.stationType)):
            for xx in range(len(self.stationType[yy])):
                if self.stationType[yy][xx] != 0:
                    new_station = stations.Station(xx,yy,
                                                   self.stationType[yy][xx],
                                                   self.stationAttractions[yy][xx]
                                                   )
                    self.station_list.append(new_station)
        return
    
    # TODO: take a list of Station objects, turn it into multiple arrays representing the board
    #   This function will essentially invert get_board_coords()
    def get_board_arrays(self, staList):
        pass
    
    def get_board_shapes(self, shape):
        if 1 > shape > 6:
            print("Error: pick a number between 1 and 6")
            print("1: Circle, 2: '?', 3: Triangle, 4: Square, 5: Pentagon, 6: Attraction")
            return [[0]]
        
        if shape == 6:
            return self.stationAttractions
        
        return [self.stationType == shape]
    
    def draw(self,screen,x0,y0,x1,y1):
        # print(self.stationType.shape)
        
        # Use the Station.draw(screen, x, y) function
        
        # draw the board in the area defined by (x0, y0) (x1, y1)
        #   Pad the edges by some % or number of pixels
        #   Map the station coordinates to the coordinate range (within padding)
        #   Draw in the dotted lines between adjacent stations (Station.inline)
        
        
        # Maybe refactor this into a new function:
        # 5 percent (on all 4 sides)
        # Right now, this is not a percent. will need to fix.
        padding = 5
        
        totalX = abs(x1-x0)
        totalY = abs(y1-y0)
        
        paddingPixX = round(totalX / padding)
        paddingPixY = round(totalY / padding)
        
        x0 = x0+paddingPixX
        y0 = y0+paddingPixY
        x1 = x1-paddingPixX
        y1 = y1-paddingPixY
        # new coordinates are the padded coordinates
        
        
        
        # create coordinates for each station using linspace
        board_shape = self.stationType.shape
        # these are maps for stations plotted coordinates
        #   xPlot = xCoords[Station.location[0]]
        xCoords = np.linspace(x0,x1,board_shape[0])
        yCoords = np.linspace(y0,y1,board_shape[1])
        
        
        for station in self.station_list:
            xPlot = xCoords[station.location[0]]
            yPlot = yCoords[station.location[1]]
            # print("Drawing station at", xPlot,yPlot)
            station.draw(screen, xPlot, yPlot)
        
        
        return
        
        
# print(stationStart.shape)