#!/usr/bin/env python
"""app.py: 
A simple implementation of Conway's Game of Life using Pygame.
"""

__author__ = "@daibeal"
__email__ = "andres@daibeal.me"
__license__ = "MIT"
# Import libraries
import pygame
import numpy as np

# Define constants
WIDTH = 800 # Width of the window
HEIGHT = 800 # Height of the window
ROWS = 50 # Number of rows in the grid
COLS = 50 # Number of columns in the grid
CELL_SIZE = WIDTH // COLS # Size of a cell
FPS = 10 # Frames per second
BLACK = (0, 0, 0) # Color for dead cells and background
WHITE = (255, 255, 255) # Color for alive cells and text
RED = (255, 0, 0) # Color for buttons
GREEN = (0, 255, 0) # Color for buttons
BLUE = (0, 0, 255) # Color for buttons
FONT_SIZE = 32 # Size of the font
BUTTON_WIDTH = 150 # Width of the buttons
BUTTON_HEIGHT = 50 # Height of the buttons
BUTTON_MARGIN = 20 # Margin between buttons

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", FONT_SIZE)

# Create a random grid of cells
grid = np.random.randint(2, size=(ROWS, COLS))

# Define a function to draw the grid on the screen
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, WHITE, (i*CELL_SIZE+1, j*CELL_SIZE+1,
                                                 CELL_SIZE-1, CELL_SIZE-1))

# Define a function to update the grid according to the rules
def update_grid():
    global grid
    new_grid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
            # Count the number of living neighbors
            n = np.sum(grid[i-1:i+2,j-1:j+2]) - grid[i][j]

            # Apply the rules
            if grid[i][j] == 1 and (n < 2 or n > 3):
                new_grid[i][j] = 0 # Die
            elif grid[i][j] == 0 and n == 3:
                new_grid[i][j] = 1 # Resurrect

    grid = new_grid

# Define a function to draw a button on the screen
def draw_button(x, y, w, h, color, text):
    pygame.draw.rect(screen, color, (x, y, w, h))
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + w // 2 , y + h // 2)
    screen.blit(text_surface , text_rect)

# Define some variables for the game state and menu options
paused = True # Whether the game is paused or not
randomize = False # Whether to randomize the grid or not
clear = False # Whether to clear the grid or not

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Draw the grid
    draw_grid()

    # Update the grid if not paused
    if not paused:
        update_grid()

    # Draw the buttons
    draw_button(WIDTH - BUTTON_WIDTH - BUTTON_MARGIN,
                BUTTON_MARGIN,
                BUTTON_WIDTH,
                BUTTON_HEIGHT,
                RED if paused else GREEN,
                "PAUSE" if paused else "PLAY")

    draw_button(WIDTH - BUTTON_WIDTH - BUTTON_MARGIN,
                BUTTON_MARGIN * 2 + BUTTON_HEIGHT,
                BUTTON_WIDTH + BUTTON_MARGIN,
                BUTTON_HEIGHT,
                BLUE,
                "RANDOMIZE")

    draw_button(WIDTH - BUTTON_WIDTH - BUTTON_MARGIN,
                BUTTON_MARGIN * 3 + BUTTON_HEIGHT * 2,
                BUTTON_WIDTH,
                BUTTON_HEIGHT
                , BLUE,
                "CLEAR")
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x >= WIDTH - BUTTON_WIDTH - BUTTON_MARGIN and x <= WIDTH - BUTTON_MARGIN:
                if y >= BUTTON_MARGIN and y <= BUTTON_MARGIN + BUTTON_HEIGHT:
                    paused = not paused
                elif y >= BUTTON_MARGIN * 2 + BUTTON_HEIGHT and y <= BUTTON_MARGIN * 2 + BUTTON_HEIGHT * 2:
                    randomize = True
                elif y >= BUTTON_MARGIN * 3 + BUTTON_HEIGHT * 2 and y <= BUTTON_MARGIN * 3 + BUTTON_HEIGHT * 3:
                    clear = True

    # Randomize the grid if requested
    if randomize:
        grid = np.random.randint(2, size=(ROWS, COLS))

        randomize = False

    # Clear the grid if requested
    if clear:
        grid = np.zeros((ROWS, COLS))
        clear = False

    

    

    pygame.display.flip()

pygame.quit()


