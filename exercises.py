import pygame
import const

class Exercises():
    def __init__(self, x, y):
        self.number_ex = 0
        self.exercise_imgs = [
            pygame.transform.scale(pygame.image.load("img/exercise_1.png"), [const.EX_WIDHT, const.EX_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/exercise_1.png"), [const.EX_WIDHT, const.EX_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/exercise_1.png"), [const.EX_WIDHT, const.EX_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/exercise_1.png"), [const.EX_WIDHT, const.EX_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/exercise_1.png"), [const.EX_WIDHT, const.EX_HEIGHT])
        ]
        self.exercise_answers = [156, 156, 156, 156, 156]
        self.image = self.exercise_imgs[self.number_ex]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]



    def update(self, num):
        if num != self.number_ex:
            self.number_ex = num
            self.image = self.exercise_imgs[num]


    def render(self, screen):
        screen.blit(self.image, self.rect.topleft)