# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:07:55 2024

@author: chris
"""


# Next station: London

# preset map
# queued card system (11 total: 1 junction, 5 purple station cards, 5 blue ones)
# each line is a set 1 to n stations with 1 or more terminus stations
#   no overlapping lines (later)

# game loop: a station card is pulled, 1 station can be added to the active line
#   once all the purple station cards are pulled, the round for that line is over and the next line becomes active
#   once all lines have been drawn, the final scores are calculated

import board
b = board.Board()
print(b.stationType)