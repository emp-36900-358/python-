import pygame
from pathlib import Path

from objects.button import Button
from objects.image_slot import ImageSlot


WIDTH = 600
HEIGHT = 800

# プロジェクトのルートフォルダ
BASE_DIR = Path(__file__).resolve().parent.parent

# 機体画像フォルダ
SHIP_DIR = BASE_DIR / "images" / "ships" / "player"


class SingleSelectShipScene:

    def __init__(self, game_data):

        self.game_data = game_data

        # --------------------------------
        # 機体画像
        # --------------------------------

        self.ships = [
            pygame.image.load(
                str(SHIP_DIR / "red_ship.png")
            ).convert_alpha(),

            pygame.image.load(
                str(SHIP_DIR / "blue_ship.png")
            ).convert_alpha(),

            pygame.image.load(
                str(SHIP_DIR / "green_ship.png")
            ).convert_alpha(),

            pygame.image.load(
                str(SHIP_DIR / "yellow_ship.png")
            ).convert_alpha(),

            pygame.image.load(
                str(SHIP_DIR / "lightblue_ship.png")
            ).convert_alpha(),

            pygame.image.load(
                str(SHIP_DIR / "purple_ship.png")
            ).convert_alpha(),
        ]

        # 現在選択している機体
        self.current_ship = 0

        # --------------------------------
        # 画像表示枠
        # --------------------------------

        self.image_slot = ImageSlot(
            250, 150,
            200, 200
        )

        # --------------------------------
        # ボタン
        # --------------------------------

        self.button_select_before = Button(
            100, 220,
            70, 60,
            "<"
        )

        self.button_select_after = Button(
            450, 220,
            70, 60,
            ">"
        )

        self.ok_button = Button(
            300, 580,
            200, 60,
            "OK"
        )

    # ====================================
    # 更新
    # ====================================

    def update(self, events):

        for event in events:

            # 左ボタン
            if self.button_select_before.is_clicked(event):

                self.current_ship -= 1

                if self.current_ship < 0:
                    self.current_ship = len(self.ships) - 1

            # 右ボタン
            if self.button_select_after.is_clicked(event):

                self.current_ship += 1

                if self.current_ship >= len(self.ships):
                    self.current_ship = 0

            # OK
            if self.ok_button.is_clicked(event):
                self.game_data.ship = self.current_ship
                return "bullet_select_single"

        return "ship_select_single"

    # ====================================
    # 描画
    # ====================================

    def draw(self, screen):

        screen.fill((0, 0, 0))

        # フォント
        font = pygame.font.Font(None, 40)
        title_font = pygame.font.Font(None, 50)

        # タイトル
        title = title_font.render(
            "1P SHIP SELECT",
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 40)
        )

        screen.blit(title, title_rect)

        # 現在の機体画像
        current_image = self.ships[self.current_ship]

        self.image_slot.draw(
            screen,
            current_image
        )

        # 機体番号
        text = font.render(
            f"SHIP {self.current_ship + 1} / {len(self.ships)}",
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=(WIDTH // 2, 430)
        )

        screen.blit(text, text_rect)

        # ボタン
        self.button_select_before.draw(
            screen,
            font
        )

        self.button_select_after.draw(
            screen,
            font
        )

        self.ok_button.draw(
            screen,
            font
        )