# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:41:36 2024

@author: chris
"""


# Station classes

import pygame
import numpy as np


directionVectors = np.array([[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]])
boardXMin = 0
boardXMax = 9
boardYMin = 0
boardYMax = 9

def isInLine(p1, p2):
    # TODO: add diagonal connections
    # TODO: remove all but the closest connection in each direction

    #   Depth first Search
    # Check if p1 is in line with p2.
    
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return True
    
    return False


class Station:
    def __init__(self, x, y, st_type, isAttr, isStart=0):
              
        # inline_list: list of stations: len 8: DFS from Station x,y in in each 8 directions
        #   N is first [0], clockwise to NW last [7]
        #   If nothing is found in a direction, that slot will be null (or 0)
        #   At the end, the closest station in each direction will be in the corresponding slot
        
        # List of possible connection stations:
        #   This may need to be a list of indicies in the Boards Station List
        self.inline_list = np.zeros(8)
        # type of station: integer (0: empty, 1: circ, 2: ?, 3: tri, 4: squ, 5: pent)
        self.station_type = st_type
        # location on the map: list of [x,y]
        self.location = [x,y]
        # tourist, for later: boolean
        self.isAttraction = isAttr
        # Is this a start point?: Boolean (there can only be 1 start point per station type)
        # If no value is supplied or the board is generating from a list (eg. Real Lat/lon data),
        #   these will need to be generated automatically
        self.isStart = isStart
        # # basic station index for the station_type to text
        self.station_index = {1: "Circle", 2: "All", 3: "Triangle",
                              4: "Square", 5: "Pentagon"}
        
        
        # Testing this feature in main Station object:
        self.next = []
        self.image = pygame.image.load(f"assets/Cards/Blue_{self.station_index[self.station_type]}.png")
        
        
    
    
    
    # Used from my Transit sim. 
    #   This may not be the best to use here.
    def connectTwoWay(self, station):
        self.inline_list.append(station)
        station.inline_list.append(self)
    
    # This function will be used by Board once stationList and arrays are generated
    def createConnections(self, stationList, typeArray):
        # stationList is a list of existing stations.
        # My original idea for the algorithm:
        # for each station, add it to connections if the connection is on the 8 ordinal and cardinal directions
        #   For now, Just N, E, S, W
        
        # New Algorithm: DFS from Station location [x,y] in in each 8 directions
        #   South (0,1) is first, then rotate CCW to SW (-1,1) last in the array
        #   If nothing is found in a direction, that slot will be null (or 0)
        #   At the end, the closest station in each direction will be in the corresponding slot
        
        #TODO: Typecheck stationList and typeArray
        for ii in range(len(directionVectors)):
            status = True
            currentDir = directionVectors[ii]
            currentLoc = self.location.copy()
            
            while status:
                currentLoc += currentDir
                # out of bounds check:
                if currentLoc[0] < boardXMin or currentLoc[1] < boardYMin or currentLoc[0] > boardXMax or currentLoc[1] > boardYMax:
                    self.inline_list[ii] = 0
                    status = False
                    
                else: 
                    # Compare the currentLoc to the typeArray
                    # The next line is flagged as invalid syntax, I disagree
                    if not typeArray[currentLoc[1]][currentLoc[0]]:
                        # Do nothing if currentLoc is not on a station
                        pass
                    else:
                        # If currentLoc is on a station, find that station and create a connection
                        for jj in range(len(stationList)):
                            if (stationList[jj].location == currentLoc).all():
                                # TODO: Connect Stations,
                                # Not sure if I should do two-way to cut time in half and add a check at the start of this func
                                self.inline_list[ii] = jj
                                status = False
                                pass
                    
                
                    
                
        
        # Old Code: Not compatible
        # for station in stationList:
        #     # probably should have type safety
        #     # print("Testing "+self.name+" and "+station.name)
        #     if isInLine(self.location, station.location):
        #         print("Connecting " +str(self.location)+" to "+str(station.location))
        #         self.connectTwoWay(station)
    
    def draw(self, screen, x, y):
        lh = screen.get_size()
        mult_screen = 0.04
        img = pygame.transform.scale(self.image, (lh[0]*mult_screen, lh[1]*mult_screen))
        # print("Station at",x,y," Size:", (lh[0]*mult_screen, lh[1]*mult_screen))
        screen.blit(img, (x,y))
        # return
    
    def __str__(self):
        return f"{self.station_index[self.station_type]} station at {self.location}"
    
# Actual station connectivity:
# Not fully sure how this is going to work. It may be a doubly linked list
# A linear set of stations would be trivial to implement in an array or a linked list
# Branches will not be as straightforward with either method
# Linked lists could get very messy here. The "next" object could be an array, though.
# Internally debating on whether or not to make a new object for the line, 
#   or just use the station object that I already have.

# class StationLine:
#     def __init__(self):

#         pass
        