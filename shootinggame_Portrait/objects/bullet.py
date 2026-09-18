import pygame
from pathlib import Path
from objects.hitbox import RectHitbox


BASE_DIR = Path(__file__).resolve().parent.parent
BULLET_DIR = BASE_DIR / "images" / "bullets" / "player"


class PlayerBullet:

    def __init__(self, x, y, bullet_number):
        self.x = x
        self.y = y
        self.bullet_number = bullet_number

        bullet_files = [
            "red_bullet.png",
            "blue_bullet.png",
            "green_bullet.png",
            "yellow_bullet.png",
            "lightblue_bullet.png",
            "purple_bullet.png"
        ]

        self.image = pygame.image.load(
            str(BULLET_DIR / bullet_files[bullet_number])
        ).convert_alpha()

        # 弾を小さくする
        max_width = 30
        max_height = 30

        width, height = self.image.get_size()

        scale = min(
            max_width / width,
            max_height / height
        )

        new_width = int(width * scale)
        new_height = int(height * scale)

        self.image = pygame.transform.smoothscale(
            self.image,
            (new_width, new_height)
        )

        self.rect = self.image.get_rect(
            center=(self.x, self.y)
        )

        self.speed = 10

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

        # 上に飛ぶ
        self.y -= self.speed

        self.rect.center = (self.x, self.y)

        self.hitbox.set_position(
            self.rect.x,
            self.rect.y
        )

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_outside(self):
        return self.rect.bottom < 0
    
class EnemyBullet:

    def __init__(self, x, y, bullet_number):

        self.x = x
        self.y = y

        self.bullet_number = bullet_number

        self.hitbox = RectHitbox(
            self.x,
            self.y,
            20,
            20
        )

    def update(self):

        self.y += 10

        self.hitbox.set_position(
            self.x,
            self.y
        )
        