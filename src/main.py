import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BACKGROUND_COLOR = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Super Bingo Game')

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Game logic goes here

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()