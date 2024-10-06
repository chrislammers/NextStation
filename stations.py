# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:41:36 2024

@author: chris
"""


# Station classes


class Station:
    def __init__(self):
        # connections: list of len 0 to 8, other Stations
        self.line_list = []
        # type of station: integer (0: empty, 1: circ, 2: ?, 3: tri, 4: squ, 5: pent)
        self.station_type = 0
        # location on the map: list of [x,y]
        self.location = [0,0]
        # tourist, for later: boolean
        self.isAttraction = False
        # 
        