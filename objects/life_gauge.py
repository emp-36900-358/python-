import pygame
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

LIFE_DIR = (
    BASE_DIR
    / "images"
    / "lifegauge"
)


class LifeGauge:

    def __init__(
        self,
        ship_number,
        life=4,
        x=20,
        y=50
    ):

        self.ship_number = ship_number

        self.max_life = life
        self.life = life

        self.x = x
        self.y = y

        # ====================================
        # 自機の色ごとの残機画像
        # ====================================

        life_files = [
            "red_ship_life.png",
            "blue_ship_life.png",
            "green_ship_life.png",
            "yellow_ship_life.png",
            "lightblue_ship_life.png",
            "purple_ship_life.png"
        ]

        half_life_files = [
            "red_ship_life_half.png",
            "blue_ship_life_half.png",
            "green_ship_life_half.png",
            "yellow_ship_life_half.png",
            "lightblue_ship_life_half.png",
            "purple_ship_life_half.png"
        ]

        # ====================================
        # 通常残機画像
        # ====================================

        self.life_image = pygame.image.load(
            str(LIFE_DIR / life_files[ship_number])
        ).convert_alpha()

                # 自機画像を縮小
        max_width = 20
        max_height = 20

        image_width = self.life_image.get_width()
        image_height = self.life_image.get_height()

        scale = min(
            max_width / image_width,
            max_height / image_height
        )

        new_width = max(1, int(image_width * scale))
        new_height = max(1, int(image_height * scale))

        self.life_image = pygame.transform.smoothscale(
            self.life_image,
            (new_width, new_height)
        )



        # ====================================
        # 半分残機画像
        # ====================================

        self.half_life_image = pygame.image.load(
            str(LIFE_DIR / half_life_files[ship_number])
        ).convert_alpha()

                # 自機画像を縮小
        max_width = 20
        max_height = 20

        image_width = self.half_life_imag.get_width()
        image_height = self.half_life_imag.get_height()

        scale = min(
            max_width / image_width,
            max_height / image_height
        )

        new_width = max(1, int(image_width * scale))
        new_height = max(1, int(image_height * scale))

        self.half_life_imag = pygame.transform.smoothscale(
            self.half_life_imag,
            (new_width, new_height)
        )


    # ========================================
    # 残機を減らす
    # ========================================

    def damage(self, amount=1):

        self.life -= amount

        if self.life < 0:
            self.life = 0

    # ========================================
    # 残機を回復
    # ========================================

    def heal(self, amount=1):

        self.life += amount

        if self.life > self.max_life:
            self.life = self.max_life

    # ========================================
    # 残機があるか
    # ========================================

    def is_empty(self):

        return self.life <= 0

    # ========================================
    # 描画
    # ========================================

    def draw(self, screen):

        # 整数部分
        full_life = int(self.life)

        # 0.5部分
        has_half = (
            self.life - full_life >= 0.5
        )

        current_x = self.x

        # ====================================
        # 通常残機
        # ====================================

        for _ in range(full_life):

            screen.blit(
                self.life_image,
                (
                    current_x,
                    self.y
                )
            )

            current_x += self.life_image.get_width()

        # ====================================
        # 半分残機
        # ====================================

        if has_half:

            screen.blit(
                self.half_life_image,
                (
                    current_x,
                    self.y
                )
            )