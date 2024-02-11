import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Pygame Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Character
character_width = 50
character_height = 50
character_x = (screen_width - character_width) // 2
character_y = screen_height - character_height - 10
character_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed

    # Draw everything
    screen.fill(white)
    pygame.draw.rect(screen, black, (character_x, character_y, character_width, character_height))

    pygame.display.flip()

pygame.quit()
sys.exit()