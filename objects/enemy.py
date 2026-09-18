
import pygame
from pathlib import Path

from objects.hitbox import RectHitbox

BASE_DIR = Path(__file__).resolve().parent.parent
ENEMY_DIR = BASE_DIR / "images" / "ships" / "enemy"


class Enemy:
    def __init__(self, x, y, enemy_type):
        self.x = x
        self.y = y
        self.enemy_type = enemy_type

        enemy_files = [
            "enemy1.png",
            "enemy2.png",
            "enemy3.png"
        ]

        self.image = pygame.image.load(
            str(ENEMY_DIR / enemy_files[enemy_type - 1])
        ).convert_alpha()

        # とりあえず大きすぎないようにする
        max_width = 60
        max_height = 60

        width, height = self.image.get_size()

        scale = min(
            max_width / width,
            max_height / height
        )

        new_width = max(1, int(width * scale))
        new_height = max(1, int(height * scale))

        self.image = pygame.transform.smoothscale(
            self.image,
            (new_width, new_height)
        )

        self.rect = self.image.get_rect(
            center=(self.x, self.y)
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

        self.hitbox.set_center(
            self.rect.centerx,
            self.rect.centery
        ) 

    def update(self):
        # 今は動かさない
        self.rect.center = (self.x, self.y)

        self.hitbox.set_center(
            self.rect.centerx,
            self.rect.centery
        )   

    def draw(self, screen):
        screen.blit(self.image, self.rect)

