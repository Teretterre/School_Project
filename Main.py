import pygame
import const
from background import draw_back_gradient
import exercises
from exercises import Exercises
from textinput import TextInput
pygame.init()

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("School_Project")
clock = pygame.time.Clock()


def main():
    NUM = 0
    exercise = Exercises(20, 20, NUM)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_back_gradient(screen, (135, 180, 200), (0, 191, 255))
        screen.blit(exercise.image, exercise.topleft)



        pygame.display.flip()
        clock.tick(const.FPS)

    pygame.quit()
main()