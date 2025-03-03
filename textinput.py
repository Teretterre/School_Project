import pygame

class TextInput:
    def __init__(self, x, y, w, h, font_size, text_color, bg_color, border_color, active_border_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.inactive_border_color = border_color
        self.active_border_color = active_border_color
        self.bg_color = bg_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)
        self.text = ''
        self.active = False

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.colliderect(event.pos):
                self.active = True
                self.border_color = self.active_border_color
            else:
                self.active = False
                self.border_color = self.inactive_border_color
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def render(self, screen):
        # Отрисовывает поле ввода
        pygame.draw.rect(screen, self.bg_color, self.rect)  # Фон
        pygame.draw.rect(screen, self.border_color, self.rect, 2)  # Граница
        text_surface = self.font.render(self.text, True, self.text_color)  # Текст
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + (self.rect.height - text_surface.get_height()) // 2))  # Отрисовка

    def get_text(self):
        # Возвращает введенный текст
        return self.text

    def clear(self):
        # Отчищает поле
        self.text = ''