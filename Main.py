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
    textinput = TextInput(20, 500, 700, 40, 30, text_color=const.BLACK, bg_color=const.WHITE, border_color=const.GRAY, active_border_color=const.GREEN)
    exercises = Exercises(20, 20)
    current_ex = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            textinput.update(event)
        #обновление объектов
        exercises.update(current_ex)


        #отрисовка
        draw_back_gradient(screen, (135, 180, 200), (0, 191, 255))
        exercises.render(screen)
        textinput.render(screen)


        pygame.display.flip()
        clock.tick(const.FPS)

    pygame.quit()
main()