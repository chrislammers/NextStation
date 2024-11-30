# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:41:02 2024

@author: chris
"""

import random
# import time

class Card:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
    def __str__(self):
        return f"{self.color} {self.shape}"
    
    
class Deck:
    def __init__(self):
        colors = ["Blue", "Pink"]
        shapes = ["Circle", "All", "Triangle", "Square", "Pentagon"]
        self.deck = [Card(shape, color) for color in colors for shape in shapes]
        self.deck.append(Card("Junction", "Blue"))
        self.pinks = 0
    
    def get_card(self):
        card = self.deck.pop(0)
        self.deck.append(card)
        return card
    
    def shuffle(self):
        random.shuffle(self.deck)
        