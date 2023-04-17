import pygame

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("My Pygame Window")

from Matrix import Matrix
from Wavy import Wave

screen.fill((255, 255, 255))

clock = pygame.time.Clock()

matrix = Matrix()
wave = Wave()

running = True
matrix.draw_whole_matrix()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw objects on the screen (e.g. shapes, images, text)
    wave.update()

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()