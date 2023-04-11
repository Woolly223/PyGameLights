import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (in pixels)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("My Pygame Window")

# Import Matrix class
from Matrix import Matrix

# Fill the screen with a color (e.g. white)
screen.fill((255, 255, 255))

# Screen Update Speed (FPS)
clock = pygame.time.Clock()

# Initialize Matrix
matrix = Matrix()

# Start the main loop
running = True
while running:
    # Handle events (e.g. quit button pressed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw objects on the screen (e.g. shapes, images, text)
    matrix.draw_whole_matrix()

    # Update the display
    pygame.display.update()
    
    #Setting FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()