import pygame
from pathlib import Path

from objects.button import Button
from objects.image_slot import ImageSlot


WIDTH = 600
HEIGHT = 800

BASE_DIR = Path(__file__).resolve().parent.parent

BULLET_DIR = BASE_DIR / "images" / "bullets" / "player"


class SingleSelectBulletScene:

    def __init__(self, game_data):

        self.game_data = game_data

        # ====================================
        # 弾画像
        # ====================================
        #
        # ↓ここは実際のファイル名に変更してください
        #

        self.bullets = [
            pygame.image.load(
                str(BULLET_DIR / "red_bullet.png")
            ).convert_alpha(),

            pygame.image.load(
                str(BULLET_DIR / "blue_bullet.png")
            ).convert_alpha(),

            pygame.image.load(
                str(BULLET_DIR / "green_bullet.png")
            ).convert_alpha(),

            pygame.image.load(
                str(BULLET_DIR / "yellow_bullet.png")
            ).convert_alpha(),

            pygame.image.load(
                str(BULLET_DIR / "lightblue_bullet.png")
            ).convert_alpha(),

            pygame.image.load(
                str(BULLET_DIR / "purple_bullet.png")
            ).convert_alpha(),
        ]

        self.current_bullet = 0

        # ====================================
        # 画像枠
        # ====================================

        self.image_slot = ImageSlot(
            300, 150,
            128, 128
        )

        # ====================================
        # ボタン
        # ====================================

        self.button_select_before = Button(
            100, 200,
            100, 60,
            "<"
        )

        self.button_select_after = Button(
            520, 200,
            100, 60,
            ">"
        )

        self.ok_button = Button(
            300, 480,
            200, 60,
            "OK"
        )

    # ====================================
    # 更新
    # ====================================

    def update(self, events):

        for event in events:

            # 左
            if self.button_select_before.is_clicked(event):

                self.current_bullet -= 1

                if self.current_bullet < 0:
                    self.current_bullet = len(self.bullets) - 1

            # 右
            if self.button_select_after.is_clicked(event):

                self.current_bullet += 1

                if self.current_bullet >= len(self.bullets):
                    self.current_bullet = 0

            # OK
            if self.ok_button.is_clicked(event):
                self.game_data.bullet = self.current_bullet
                return "play_single"

        return "bullet_select_single"

    # ====================================
    # 描画
    # ====================================

    def draw(self, screen):

        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 40)
        title_font = pygame.font.Font(None, 50)

        # タイトル
        title = title_font.render(
            "1P BULLET SELECT",
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(300, 40)
        )

        screen.blit(
            title,
            title_rect
        )

        # 弾画像
        current_image = self.bullets[self.current_bullet]

        self.image_slot.draw(
            screen,
            current_image
        )

        # 番号
        text = font.render(
            f"BULLET {self.current_bullet + 1} / {len(self.bullets)}",
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=(300, 430)
        )

        screen.blit(
            text,
            text_rect
        )

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