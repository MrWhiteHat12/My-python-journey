import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Pygame Example")

# Set up clock for frame rate
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Circle properties
x, y = WIDTH // 2, HEIGHT // 2
radius = 30
speed = 50

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key input handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_r]:
        x = WIDTH // 2
        y = HEIGHT // 2

    # Fill the screen
    screen.fill(WHITE)

    # Draw the circle
    pygame.draw.circle(screen, RED, (x, y), radius)

    # Update the display
    pygame.display.flip()

    if keys[pygame.K_ESCAPE]:
        running = False

# Quit Pygame

pygame.quit()
sys.exit()
