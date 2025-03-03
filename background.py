import pygame
import random
import const


def draw_back_gradient(screen, start_color, end_color):
    widht, height = screen.get_size()
    for y in range(height):
        r = start_color[0] + (end_color[0] - start_color[0]) * y // height
        g = start_color[1] + (end_color[1] - start_color[1]) * y // height
        b = start_color[2] + (end_color[2] - start_color[2]) * y // height
        pygame.draw.line(screen, (r, g, b), (0, y), (widht, y))
