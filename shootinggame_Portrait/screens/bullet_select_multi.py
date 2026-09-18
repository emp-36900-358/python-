import pygame
from pathlib import Path

from objects.button import Button
from objects.image_slot import ImageSlot


WIDTH = 600
HEIGHT = 800

BASE_DIR = Path(__file__).resolve().parent.parent

BULLET_DIR = BASE_DIR / "images" / "bullets" / "player"


class MultiSelectBulletScene:

    def __init__(self, game_data):

        self.game_data = game_data

        # ====================================
        # 弾画像
        # ====================================
        #
        # ↓実際のファイル名に変更してください
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

        # ====================================
        # 選択状態
        # ====================================

        self.current_bullet_1p = 0
        self.current_bullet_2p = 0

        # ====================================
        # 画像枠
        # ====================================

        self.image_slot_1p = ImageSlot(
            90, 150,
            128, 128
        )

        self.image_slot_2p = ImageSlot(
            390, 150,
            128, 128
        )

        # ====================================
        # 1Pボタン
        # ====================================

        self.button_select_before_1p = Button(
            15, 200,
            70, 60,
            "<"
        )

        self.button_select_after_1p = Button(
            220, 200,
            70, 60,
            ">"
        )

        self.ok_button_1p = Button(
            65, 480,
            200, 60,
            "OK"
        )

        # ====================================
        # 2Pボタン
        # ====================================

        self.button_select_before_2p = Button(
            310, 200,
            70, 60,
            "<"
        )

        self.button_select_after_2p = Button(
            520, 200,
            70, 60,
            ">"
        )

        self.ok_button_2p = Button(
            385, 480,
            200, 60,
            "OK"
        )

        # ====================================
        # OK状態
        # ====================================

        self.ok_pressed_1p = False
        self.ok_pressed_2p = False

    # ====================================
    # 更新
    # ====================================

    def _change_bullet(self, button, event, attribute, step):
        if button.is_clicked(event):
            current = getattr(self, attribute) + step
            setattr(self, attribute, current % len(self.bullets))

    def _confirm_bullet(self, button, event, current_attribute,
                        data_attribute, pressed_attribute):
        if button.is_clicked(event):
            setattr(self.game_data, data_attribute,
                    getattr(self, current_attribute))
            setattr(self, pressed_attribute, True)

    def update(self, events):

        for event in events:
            self._change_bullet(
                self.button_select_before_1p, event, "current_bullet_1p", -1
            )
            self._change_bullet(
                self.button_select_after_1p, event, "current_bullet_1p", 1
            )
            self._change_bullet(
                self.button_select_before_2p, event, "current_bullet_2p", -1
            )
            self._change_bullet(
                self.button_select_after_2p, event, "current_bullet_2p", 1
            )
            self._confirm_bullet(
                self.ok_button_1p, event, "current_bullet_1p", "bullet_1p",
                "ok_pressed_1p"
            )
            self._confirm_bullet(
                self.ok_button_2p, event, "current_bullet_2p", "bullet_2p",
                "ok_pressed_2p"
            )

        # 両方OK
        if self.ok_pressed_1p and self.ok_pressed_2p:
            return "play_multi"

        return "bullet_select_multi"

    # ====================================
    # 描画
    # ====================================

    def draw(self, screen):

        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 36)
        title_font = pygame.font.Font(None, 50)

        # --------------------------------
        # タイトル
        # --------------------------------

        title = title_font.render(
            "2P BULLET SELECT",
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

        # --------------------------------
        # 中央線
        # --------------------------------

        pygame.draw.line(
            screen,
            (100, 100, 100),
            (300, 80),
            (300, 600),
            2
        )

        # ====================================
        # 1P
        # ====================================

        player1_text = font.render(
            "PLAYER 1",
            True,
            (255, 255, 255)
        )

        player1_rect = player1_text.get_rect(
            center=(150, 90)
        )

        screen.blit(
            player1_text,
            player1_rect
        )

        # 弾画像
        self.image_slot_1p.draw(
            screen,
            self.bullets[self.current_bullet_1p]
        )

        # 番号
        bullet1_text = font.render(
            f"BULLET {self.current_bullet_1p + 1} / {len(self.bullets)}",
            True,
            (255, 255, 255)
        )

        bullet1_rect = bullet1_text.get_rect(
            center=(150, 370)
        )

        screen.blit(
            bullet1_text,
            bullet1_rect
        )

        # ボタン
        self.button_select_before_1p.draw(
            screen,
            font
        )

        self.button_select_after_1p.draw(
            screen,
            font
        )

        self.ok_button_1p.draw(
            screen,
            font
        )

        # ====================================
        # 2P
        # ====================================

        player2_text = font.render(
            "PLAYER 2",
            True,
            (255, 255, 255)
        )

        player2_rect = player2_text.get_rect(
            center=(450, 90)
        )

        screen.blit(
            player2_text,
            player2_rect
        )

        # 弾画像
        self.image_slot_2p.draw(
            screen,
            self.bullets[self.current_bullet_2p]
        )

        # 番号
        bullet2_text = font.render(
            f"BULLET {self.current_bullet_2p + 1} / {len(self.bullets)}",
            True,
            (255, 255, 255)
        )

        bullet2_rect = bullet2_text.get_rect(
            center=(450, 370)
        )

        screen.blit(
            bullet2_text,
            bullet2_rect
        )

        # ボタン
        self.button_select_before_2p.draw(
            screen,
            font
        )

        self.button_select_after_2p.draw(
            screen,
            font
        )

        self.ok_button_2p.draw(
            screen,
            font
        )