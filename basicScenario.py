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
# b.stationType
d.pull_card()
d.pull_card()
d.shuffle()
current_card = d.pull_card()


pygame.init()
SCREEN_H = 720
SCREEN_W = 720
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            # print("keyup")
            if event.key == pygame.K_d:
                # print("Drawing card:")
                current_card = d.pull_card()
            if event.key == pygame.K_a:
                d.shuffle()
                current_card = d.pull_card()
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE
    
    current_card.draw(screen,2*SCREEN_W/3,2*SCREEN_H/3)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()