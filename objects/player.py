import pygame

from pathlib import Path
from objects.hitbox import RectHitbox

BASE_DIR = Path(__file__).resolve().parent.parent
SHIP_DIR = BASE_DIR / "images" / "ships" / "player"


class Player:

    def __init__(self, x, y, ship_number, player_number, play_area):

        self.x = x
        self.y = y

        self.ship_number = ship_number
        self.player_number = player_number
        self.play_area = play_area  

        # 移動速度
        self.speed = 5

        # --------------------------------
        # 自機画像
        # --------------------------------

        ship_files = [
            "red_ship.png",
            "blue_ship.png",
            "green_ship.png",
            "yellow_ship.png",
            "lightblue_ship.png",
            "purple_ship.png"
        ]

        self.image = pygame.image.load(
            str(SHIP_DIR / ship_files[ship_number])
        ).convert_alpha()

        # 自機画像を縮小
        max_width = 60
        max_height = 60

        image_width = self.image.get_width()
        image_height = self.image.get_height()

        scale = min(
            max_width / image_width,
            max_height / image_height
        )

        new_width = max(1, int(image_width * scale))
        new_height = max(1, int(image_height * scale))

        self.image = pygame.transform.smoothscale(
            self.image,
            (new_width, new_height)
        )

        # --------------------------------
        # 当たり判定
        # --------------------------------

        hitbox_scale = 0.9

        hitbox_width = int(self.image.get_width() * hitbox_scale)
        hitbox_height = int(self.image.get_height() * hitbox_scale)

        self.hitbox = RectHitbox(
                0,
                0,
                hitbox_width,
                hitbox_height
        )

        self.hitbox.set_position(
            self.x + 10,
            self.y + 10
        )

    # --------------------------------
    # 更新
    # --------------------------------

    def update(self):

        keys = pygame.key.get_pressed()

        if self.player_number == 1:
            movement_keys = (
                (pygame.K_w, 0, -1),
                (pygame.K_s, 0, 1),
                (pygame.K_a, -1, 0),
                (pygame.K_d, 1, 0),
            )
        elif self.player_number == 2:
            movement_keys = (
                (pygame.K_UP, 0, -1),
                (pygame.K_DOWN, 0, 1),
                (pygame.K_LEFT, -1, 0),
                (pygame.K_RIGHT, 1, 0),
            )
        else:
            movement_keys = ()

        for key, x_direction, y_direction in movement_keys:
            if keys[key]:
                self.x += self.speed * x_direction
                self.y += self.speed * y_direction

        # --------------------------------
        # 当たり判定を移動
        # --------------------------------

        self.hitbox.set_position(
            self.x + 10,
            self.y + 10
        )

    # --------------------------------
    # 描画
    # --------------------------------

    def draw(self, screen):

        screen.blit(
            self.image,
            (self.x, self.y)
        )

    # --------------------------------
    # 射撃キー
    # --------------------------------

    def is_shooting(self):

        keys = pygame.key.get_pressed()

        # 1P → Space
        if self.player_number == 1:
            return keys[pygame.K_SPACE]

        # 2P → Enter
        elif self.player_number == 2:
            return keys[pygame.K_RETURN]

        return False