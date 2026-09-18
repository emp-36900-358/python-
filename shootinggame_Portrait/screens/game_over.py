
import pygame

from objects.button import Button

WIDTH = 600
HEIGHT = 800

class GameOverScene:

    def __init__(self, game_data):

        self.game_data = game_data
        
        self.restart_button = Button(
            300, 250, 200, 60,
            "Retry"
        )

        self.memberselect_button = Button(
            300, 450, 200, 60,
            "Select Member"
        )

        self.exsit_button = Button(
            300, 550, 200, 60,
            "Quit Game"
        )

    def update(self, events):

        for event in events:

            if self.restart_button.is_clicked(event):

                if self.game_data.player_count == 1:
                    return "play_single"

                elif self.game_data.player_count == 2:
                    return "play_multi"
                 
            elif self.memberselect_button.is_clicked(event):
                return "member_select"

            elif self.exsit_button.is_clicked(event):
                return "quit"

        return "game_over"

    def draw(self, screen):

        screen.fill((0, 0, 0))

        # タイトル用フォント
        title_font = pygame.font.Font(None, 70)

        # ボタン用フォント
        button_font = pygame.font.Font(None, 50)

        # 「Meta Force Shooting」
        title_text = title_font.render(
            "Game Over",
            True,
            (255, 255, 255)
        )

        # 画面中央に配置
        title_rect = title_text.get_rect(
            center=(WIDTH // 2, 150)
        )

        screen.blit(
            title_text,
            title_rect
        )

        # ボタン
        self.restart_button.draw(
            screen,
            button_font
        )

        # ボタン
        self.memberselect_button.draw(
            screen,
            button_font
        )

        self.exsit_button.draw(
            screen,
            button_font
        )