import pygame

from objects.button import Button


WIDTH = 600
HEIGHT = 800


class MemberSelectScene:

    def __init__(self, game_data):

        self.game_data = game_data

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
                self.game_data.player_count = 1
                return "ship_select_single"

            elif self.button_2p.is_clicked(event):
                self.game_data.player_count = 2
                return "ship_select_multi"

        return "member_select"

    def draw(self, screen):

        screen.fill((0, 0, 0))

        # 説明文用フォント
        title_font = pygame.font.Font("C:/Windows/Fonts/meiryo.ttc", 25)

        # ボタン用フォント
        button_font = pygame.font.Font(None, 45)

        # 「プレイ人数を選択してください」
        text = title_font.render(
            "プレイ人数を選択してください",
            True,
            (255, 255, 255)
        )

        # 画面中央に配置
        text_rect = text.get_rect(
            center=(WIDTH // 2, 120)
        )

        screen.blit(
            text,
            text_rect
        )

        # ボタン
        self.button_1p.draw(
            screen,
            button_font
        )

        self.button_2p.draw(
            screen,
            button_font
        )