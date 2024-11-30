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
import card

import pygame

b = board.Board()
d = card.Deck()
print(b.stationType)
print(d.get_card())
print(d.get_card())
d.shuffle()
print(d.get_card())


pygame.init()
screen = pygame.display.set_mode((480, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()