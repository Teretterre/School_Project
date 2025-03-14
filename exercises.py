import pygame
import const

class Exercises():
    def __init__(self, x, y):
        self.number_ex = 0
        self.exercise_imgs = [
            pygame.transform.scale(pygame.image.load("img/exercise_1.png"), [const.EX_WIDHTS[0], const.EX_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/exercise_2.png"), [const.EX_WIDHTS[1], const.EX_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/exercise_3.png"), [const.EX_WIDHTS[2], const.EX_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/exercise_4.png"), [const.EX_WIDHTS[3], const.EX_HEIGHT]),
            pygame.transform.scale(pygame.image.load("img/exercise_5.png"), [const.EX_WIDHTS[4], const.EX_HEIGHT])
        ]
        self.exercise_answers = ['-9', '1', '6', '3', '-36']
        self.image = self.exercise_imgs[self.number_ex]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]



    def update(self, num):
        if num != self.number_ex:
            self.number_ex = num
            self.image = self.exercise_imgs[num]


    def render(self, screen):
        screen.blit(self.image, self.rect.topleft)