import pygame
import const
from background import draw_back_gradient
import exercises
from const import EX_WIDHTS
from exercises import Exercises
from textinput import TextInput
from button import Button
pygame.init()

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("School_Project")
clock = pygame.time.Clock()


def main():
    current_ex = 0
    textinput = TextInput(20, 500, 700, 40, 30, text_color=const.BLACK, bg_color=const.WHITE, border_color=const.GRAY, active_border_color=const.GREEN)
    exercises = Exercises(const.SCREEN_WIDTH//2-(const.EX_WIDHTS[current_ex]//2), 20)
    score = 0
    stati = []
    show_result = False

    def button_answer():
        nonlocal  score, current_ex, show_result
        answer  = textinput.get_text()
        if answer == exercises.exercise_answers[current_ex]:
            score += 1
            stati.append('Верно')
        else:
            stati.append('Не верно')
        current_ex += 1
        if current_ex >= len(exercises.exercise_answers):
            show_result = True
            current_ex -= 1

        textinput.clear()

    button = Button(350,600, 100, 50, 'Ответить!', 20, const.WHITE, const.BLACK, const.RED, button_answer)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            textinput.update(event)
            button.update(event)
        #обновление объектов
        exercises.update(current_ex)

        #отрисовка
        draw_back_gradient(screen, (135, 180, 200), (0, 191, 255))
        if show_result:
            result_text = f"Вы набрали {score} из {len(exercises.exercise_answers)}"
            result_surface = pygame.font.Font(None, 50).render(result_text, True, const.GREEN)
            screen.blit(result_surface, (const.SCREEN_WIDTH//2 - result_surface.get_width()//2, 100))
            for i in range(len(exercises.exercise_answers)):
                result_text = f"{i+1} ответ {stati[i]} "
                result_surface = pygame.font.Font(None, 50).render(result_text, True, const.GREEN)
                screen.blit(result_surface, (const.SCREEN_WIDTH // 2 - result_surface.get_width() // 2, 200+i*100))
        else:
            exercises.render(screen)
            textinput.render(screen)
            button.render(screen)

        pygame.display.flip()
        clock.tick(const.FPS)

    pygame.quit()
main()