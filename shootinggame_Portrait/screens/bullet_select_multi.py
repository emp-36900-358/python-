import pygame

from objects.button import Button

WIDTH = 600
HEIGHT = 800

class MultiSelectbulletScene:

    def __init__(self):
        self.button_select_after1p = Button(
            25, 150, 70, 60,
            "<"
        )

        self.button_select_before1p = Button(
            250, 150, 70, 60,
            ">"
        )

        self.button_select_after2p = Button(
            550, 150, 70, 60,
            ">"
        )

        self.button_select_before2p = Button(
            300, 150, 70, 60,
            "<"
        )

        self.ok_button_1p = Button(
            100, 400, 200, 60,
            "ok"
        )

        self.ok_button_2p = Button(
            400, 400, 200, 60,
            "ok"
        )

    def update(self, events):

        ok_pressed_1p = False
        ok_pressed_2p = False

        for event in events:
            for button, delta in (
                (self.button_select_before1p, -1),
                (self.button_select_after1p, 1),
                (self.button_select_before2p, -1),
                (self.button_select_after2p, 1),
            ):
                if button.is_clicked(event):
                    self.current_bullet = (self.current_bullet + delta) % len(self.ships)

            if self.ok_button_1p.is_clicked(event):
                ok_pressed_1p = True

            if self.ok_button_2p.is_clicked(event):
                ok_pressed_2p = True

        if ok_pressed_1p and ok_pressed_2p:
            return "bullet_select_multi"

        return "play_multi"

    def draw(self, screen):

        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 50)

        self.button_select_after1p.draw(screen, font)
        self.button_select_before1p.draw(screen, font)
        self.ok_button_1p.draw(screen, font)
        self.button_select_after2p.draw(screen, font)
        self.button_select_before2p.draw(screen, font)
        self.ok_button_2p.draw(screen, font)
