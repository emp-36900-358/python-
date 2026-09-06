
import pygame

from objects.button import Button

WIDTH = 600
HEIGHT = 800

class TitleScene:

    def __init__(self):
        self.start_button = Button(
            300, 250, 200, 60,
            "START"
        )

        self.exsit_button = Button(
            300, 450, 200, 60,
            "Quit Game"
        )

    def update(self, events):

        for event in events:

            if self.start_button.is_clicked(event):
                return "member_select"
            elif self.exsit_button.is_clicked(event):
                pygame.quit()

        return "title"

    def draw(self, screen):

        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 50)

        self.start_button.draw(screen, font)
        self.exsit_button.draw(screen, font)
