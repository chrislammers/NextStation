# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:55:14 2025

@author: chris
"""


# Exporting the map as a PDF

# These maps are intended to be used in place of the NextStation map

# import importMapData
# TODO: add this to requirements.txt
# I might just create an image, then put it into a pdf to help with scaling issues

# Various modes: image/pdf modes
# TODO: Draw in static shapes/text (scoreboard, background, etc.)
#   Could pre-draw the static parts?
#   Use the imported map data in the Board object to draw the map in the 10x10 grid

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import board
import os

# Page and layout setup
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 50
GRID_SIZE = 10  # 10x10 grid
CELL_SIZE = 40  # Size of each grid square
GRID_WIDTH = GRID_SIZE * CELL_SIZE
GRID_HEIGHT = GRID_SIZE * CELL_SIZE

# Positioning
grid_x = (PAGE_WIDTH - GRID_WIDTH) / 2
grid_y = (PAGE_HEIGHT - GRID_HEIGHT) / 2

# Static area heights
STATIC_AREA_HEIGHT = 100

# Create PDF
c = canvas.Canvas("game_board.pdf", pagesize=A4)

# Draw static area (top and bottom)
def draw_static_areas():
    c.setFillColor(colors.lightgrey)
    # Top static area
    c.rect(MARGIN, PAGE_HEIGHT - STATIC_AREA_HEIGHT - MARGIN, PAGE_WIDTH - 2 * MARGIN, STATIC_AREA_HEIGHT, fill=1)
    # Bottom static area
    c.rect(MARGIN, MARGIN, PAGE_WIDTH - 2 * MARGIN, STATIC_AREA_HEIGHT, fill=1)

    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(MARGIN + 10, PAGE_HEIGHT - STATIC_AREA_HEIGHT - MARGIN + 10, "Game Info / Points (Top)")
    c.drawString(MARGIN + 10, MARGIN + STATIC_AREA_HEIGHT - 20, "Game Info / Points (Bottom)")

# Draw dynamic 10x10 grid
def draw_grid():
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    for row in range(GRID_SIZE + 1):
        y = grid_y + row * CELL_SIZE
        c.line(grid_x, y, grid_x + GRID_WIDTH, y)
    for col in range(GRID_SIZE + 1):
        x = grid_x + col * CELL_SIZE
        c.line(x, grid_y, x, grid_y + GRID_HEIGHT)

    # Optional: label rows/columns
    c.setFont("Helvetica", 8)
    for i in range(GRID_SIZE):
        c.drawString(grid_x - 15, grid_y + i * CELL_SIZE + 15, str(GRID_SIZE - i))
        c.drawString(grid_x + i * CELL_SIZE + 15, grid_y - 10, chr(65 + i))  # A, B, C...

# need to import the Station list from the board
b = board.Board()
b.get_board_coords()
stationList = b.station_list.copy()

def draw_icons():
    for station in stationList:
        row = station.location[0]
        col = station.location[1]
        icon_name = f"Blue_{b.station_index[station.station_type]}.png"
        icon_file = os.path.join("assets","Cards",icon_name)
        if os.path.exists(icon_file):
            # Convert grid row/col to PDF coordinates
            x = grid_x + col * CELL_SIZE
            y = grid_y + (GRID_SIZE - 1 - row) * CELL_SIZE
            c.drawImage(icon_file, x + 5, y + 5, width=30, height=30, mask='auto')
        else:
            print(f"Missing icon: {icon_file}")
        
        
        
# Build the board
draw_static_areas()
draw_grid()
draw_icons()

# Save
c.showPage()
c.save()
print("PDF generated: game_board.pdf")
