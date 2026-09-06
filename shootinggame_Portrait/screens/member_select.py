import pygame

from objects.button import Button

WIDTH = 600
HEIGHT = 800

class MemberSelectScene:

    def __init__(self):
        self.button_1p = Button(
            300, 250, 200, 60,
            "1pplay"
        )

        self.button_2p = Button(
            300, 450, 200, 60,
            "2pplay"
        )

    def update(self, events):

        for event in events:

            if self.button_1p.is_clicked(event):
                return "ship_select_single"
            elif self.button_2p.is_clicked(event):
                return "ship_select_multi"

        return "member_select"

    def draw(self, screen):

        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 50)

        self.button_1p.draw(screen, font)
        self.button_2p.draw(screen, font)
