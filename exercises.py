import pygame
import const

class Exercises():
    def __init__(self, x, y, number):
        self.image = pygame.image.load(const.EXERCIZES[number])
        self.number_ex = 0
        self.topleft = [x, y]
        self.otvet = 0

    def update(self):
        pass