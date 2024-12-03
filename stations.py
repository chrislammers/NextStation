# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:41:36 2024

@author: chris
"""


# Station classes

def isInLine(p1, p2):
    # Check if p1 is in line with p2.
    
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return True
    
    return False



class Station:
    def __init__(self, x, y, st_type, isAttr):
        # connections: list of len 0 to 8, other Stations
        self.inline_list = []
        # type of station: integer (0: empty, 1: circ, 2: ?, 3: tri, 4: squ, 5: pent)
        self.station_type = st_type
        # location on the map: list of [x,y]
        self.location = [x,y]
        # tourist, for later: boolean
        self.isAttraction = isAttr
        # # basic station index for the station_type to text
        self.station_index = {1: "Circle", 2: "All", 3: "Triangle",
                              4: "Square", 5: "Pentagon"}
        
    
    
    
    # Used from my Transit sim. Just use this as a suggestion
    def connectTwoWay(self, station):
        self.inline_list.append(station)
        station.inline_list.append(self)
    
    def createConnections(self, stationList):
        # stationList is a list of existing stations.
        # for each station, add it to connections if the connection is on the 8 ordinal and cardinal directions
        # For now, Just N, E, S, W
        for station in stationList:
            # probably should have type safety
            # print("Testing "+self.name+" and "+station.name)
            if isInLine(self.location, station.location):
                print("Connecting " +str(self.location)+" to "+str(station.location))
                self.connectTwoWay(station)
    
    def draw(self, screen, x, y):
        
        return
    
    def __str__(self):
        return f"{self.station_index[self.station_type]} station at {self.location}"
        