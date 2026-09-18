import pygame
from pathlib import Path

from objects.button import Button
from objects.image_slot import ImageSlot


WIDTH = 600
HEIGHT = 800

BASE_DIR = Path(__file__).resolve().parent.parent

SHIP_DIR = BASE_DIR / "images" / "ships" / "player"


class MultiSelectShipScene:

    def __init__(self, game_data):

        self.game_data = game_data

        # ====================================
        # 機体画像
        # ====================================

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

        # ====================================
        # 1P / 2Pの現在の選択
        # ====================================

        self.current_ship_1p = 0
        self.current_ship_2p = 0

        # ====================================
        # 画像表示枠
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
            10, 200,
            80, 60,
            "<"
        )

        self.button_select_after_1p = Button(
            220, 200,
            80, 60,
            ">"
        )

        self.ok_button_1p = Button(
            100, 480,
            200, 60,
            "OK"
        )

        # ====================================
        # 2Pボタン
        # ====================================

        self.button_select_before_2p = Button(
            305, 200,
            80, 60,
            "<"
        )

        self.button_select_after_2p = Button(
            520, 200,
            80, 60,
            ">"
        )

        self.ok_button_2p = Button(
            350, 480,
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

    def _update_ship(self, event, previous_button, next_button, attribute):
        change = 0
        if previous_button.is_clicked(event):
            change = -1
        elif next_button.is_clicked(event):
            change = 1

        if change:
            current_ship = getattr(self, attribute)
            setattr(
                self,
                attribute,
                (current_ship + change) % len(self.ships)
            )

    def _press_ok(self, event, button, attribute):
        if button.is_clicked(event):
            setattr(self, attribute, True)

    def update(self, events):

        for event in events:
            self._update_ship(
                event, self.button_select_before_1p,
                self.button_select_after_1p, "current_ship_1p"
            )
            self._update_ship(
                event, self.button_select_before_2p,
                self.button_select_after_2p, "current_ship_2p"
            )
            self._press_ok(event, self.ok_button_1p, "ok_pressed_1p")
            self._press_ok(event, self.ok_button_2p, "ok_pressed_2p")

        # --------------------------------
        # 両方OKなら次へ
        # --------------------------------

        if self.ok_pressed_1p and self.ok_pressed_2p:
            self.game_data.ship_1p = self.current_ship_1p
            self.game_data.ship_2p = self.current_ship_2p
            return "bullet_select_multi"

        return "ship_select_multi"

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
            "2P SHIP SELECT",
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 40)
        )

        screen.blit(title, title_rect)

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

        # --------------------------------
        # 1P
        # --------------------------------

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

        self.image_slot_1p.draw(
            screen,
            self.ships[self.current_ship_1p]
        )

        ship1_text = font.render(
            f"SHIP {self.current_ship_1p + 1} / {len(self.ships)}",
            True,
            (255, 255, 255)
        )

        ship1_rect = ship1_text.get_rect(
            center=(200, 370)
        )

        screen.blit(
            ship1_text,
            ship1_rect
        )

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

        # --------------------------------
        # 2P
        # --------------------------------

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

        self.image_slot_2p.draw(
            screen,
            self.ships[self.current_ship_2p]
        )

        ship2_text = font.render(
            f"SHIP {self.current_ship_2p + 1} / {len(self.ships)}",
            True,
            (255, 255, 255)
        )

        ship2_rect = ship2_text.get_rect(
            center=(450, 370)
        )

        screen.blit(
            ship2_text,
            ship2_rect
        )

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