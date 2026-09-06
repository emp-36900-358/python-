from asyncio import events

import pygame

from objects.button import Button

WIDTH = 600
HEIGHT = 800

class SingleSelectShipScene:

    def __init__(self):
        self.button_select_after = Button(
            550, 150, 70, 60,
            ">"
        )

        self.button_select_before = Button(
            55, 150, 70, 60,
            "<"
        )

        self.ok_button = Button(
            300, 400, 200, 60,
            "ok"
        )

    def update(self, events):

        for event in events:

            for button, delta in (
                (self.button_select_before, -1),
                (self.button_select_after, 1),
            ):
                if button.is_clicked(event):
                    self.current_ship = (self.current_ship + delta) % len(self.ships)

            if self.ok_button.is_clicked(event):
                return "bullet_select_single"
        
        return "ship_select_single"

    def draw(self, screen):

        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 50)

        self.button_select_after.draw(screen, font)
        self.button_select_before.draw(screen, font)
        self.ok_button.draw(screen, font)

