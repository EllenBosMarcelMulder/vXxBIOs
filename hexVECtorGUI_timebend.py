# hexVECtorGUI Core Concept (time-bending simulation)
# Visual + logic base for real GUI interaction

import pygame
import math
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

hex_radius = 30
hex_height = math.sqrt(3) * hex_radius

cols = 15
rows = 10

def hex_center(col, row):
    x = col * 1.5 * hex_radius
    y = row * hex_height + (hex_height / 2 if col % 2 else 0)
    return (int(x + 100), int(y + 50))

def draw_hexagon(surface, x, y, radius, color):
    points = []
    for i in range(6):
        angle = math.pi / 3 * i
        px = x + radius * math.cos(angle)
        py = y + radius * math.sin(angle)
        points.append((px, py))
    pygame.draw.polygon(surface, color, points, 0)
    pygame.draw.polygon(surface, (80, 80, 80), points, 1)

# Time-based pulse field
start_time = time.time()

while running:
    screen.fill((10, 10, 10))
    current_time = time.time() - start_time

    for row in range(rows):
        for col in range(cols):
            x, y = hex_center(col, row)
            pulse = (math.sin(current_time + col * 0.3 + row * 0.2) + 1) / 2
            color = (int(255 * (1 - pulse)), int(80 * pulse), int(255 * pulse))
            draw_hexagon(screen, x, y, hex_radius, color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
