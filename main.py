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
    textinput = TextInput(130, 400, 700, 40, 30, text_color=const.BLACK, bg_color=const.WHITE, border_color=const.GRAY, active_border_color=const.GREEN)
    exercises = Exercises(const.SCREEN_WIDTH//2, 70)
    score = 0
    stati = []
    show_result = False
    show_menu = True

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

    button = Button(350,500, 300, 150, 'Ответить!', 50, (29, 33, 29), (74, 217, 88), const.GREEN, button_answer)

    def button_start_answer():
        nonlocal show_menu
        show_menu = False

    button_start = Button(340,400, 300, 150, 'Начать!', 40, const.WHITE, (51, 78, 212), const.GREEN, button_start_answer)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            textinput.update(event)
            if show_menu:
                button_start.update(event)
            else:
                button.update(event)
        #обновление объектов
        exercises.update(current_ex)

        #отрисовка
        draw_back_gradient(screen, (135, 180, 200), (0, 191, 255))
        if show_result:
            if score == 5:
                result_text = f"Молодец! Всё правильно. Вы набрали {score} из {len(exercises.exercise_answers)}"
            elif score == 4:
                result_text = f"Неплохо, почти всё верно. Вы набрали {score} из {len(exercises.exercise_answers)}"
            elif score == 3:
                result_text = f"Больше половины есть, старайся. Вы набрали {score} из {len(exercises.exercise_answers)}"
            elif score == 2:
                result_text = f"Что-то знаешь, но есть куда расти. Вы набрали {score} из {len(exercises.exercise_answers)}"
            elif score == 1:
                result_text = f"Повтори материал и попробуй ещё раз. Вы набрали {score} из {len(exercises.exercise_answers)}"
            else:
                result_text = f"Подучи все темы и возвращайся. Вы набрали {score} из {len(exercises.exercise_answers)}"
            result_surface = pygame.font.Font(None, 50).render(result_text, True, const.GREEN)
            screen.blit(result_surface, (const.SCREEN_WIDTH//2 - result_surface.get_width()//2, 100))
            for i in range(len(exercises.exercise_answers)):
                result_text = f"{i+1} ответ {stati[i]} "
                if stati[i] == 'Верно':
                    result_surface = pygame.font.Font(None, 50).render(result_text, True, const.GREEN)
                else:
                    result_surface = pygame.font.Font(None, 50).render(result_text, True, (255, 28, 28))
                screen.blit(result_surface, (const.SCREEN_WIDTH // 2 - result_surface.get_width() // 2, 200+i*100))
        elif show_menu:
            title_text = 'Тренажёр по математике'
            title_surface = pygame.font.Font(None, 50).render(title_text, True, (51, 78, 212))
            screen.blit(title_surface, (const.SCREEN_WIDTH//2 - title_surface.get_width()//2, 100))
            button_start.render(screen)
        else:
            exercises.render(screen)
            textinput.render(screen)
            button.render(screen)

        pygame.display.flip()
        clock.tick(const.FPS)

    pygame.quit()
main()