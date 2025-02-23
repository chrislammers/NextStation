# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:41:02 2024

@author: chris
"""

import random
import pygame

# import time

class Card:
    def __init__(self, color, shape):
        self.shape = shape
        self.color = color
        self.image = pygame.image.load(f"assets/Cards/{self.color}_{self.shape}.png")
        
    def __str__(self):
        return f"{self.color} {self.shape}"
    
    def draw(self,screen,x,y):
        lh = screen.get_size()
        # print(lh)
        img = pygame.transform.scale(self.image, (lh[0]-x,lh[1]-y))
        
        screen.blit(img, (x,y))
        
    
    
class Deck:
    def __init__(self):
        colors = ["Blue", "Pink"]
        shapes = ["Circle", "All", "Triangle", "Square", "Pentagon"]
        self.deck = [Card(color, shape) for color in colors for shape in shapes]
        self.deck.append(Card("Blue","Junction"))
        
        # This is my custom top card to make the deck look nice (basically a filler)
        self.top_card = Card("Top", "Card")
        self.deck.insert(0,self.top_card)
        
        self.pinks = 0
    
    def pull_card(self):
        card = self.deck.pop(0)
        self.deck.append(card)
        print("Pulling", card)
        if card.color == "Pink":
            self.pinks += 1
            print("There are", 5-self.pinks, "pink cards left")
        
        # pseudocode for the real game loop:
        # if pinks == 5:
        #   run: shuffle()
        #   set: pinks = 0
        if self.pinks >= 5:
            self.shuffle()
            self.pinks = 0
        
        
        return card
    
    def shuffle(self):
        print("Shuffling and resetting deck")
        self.deck.remove(self.top_card)
        random.shuffle(self.deck)
        self.deck.insert(0,self.top_card)
    
        