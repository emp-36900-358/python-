import pygame
import math


class RectHitbox:
    """
    四角形の当たり判定
    """

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

    def set_position(self, x, y):
        """
        左上の位置を変更
        """
        self.rect.topleft = (x, y)

    def set_center(self, x, y):
        """
        中心位置を変更
        """
        self.rect.center = (x, y)

    def collide_rect(self, other):
        """
        四角形同士の当たり判定
        """
        return self.rect.colliderect(other.rect)


class CircleHitbox:
    """
    円形の当たり判定
    """

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def set_position(self, x, y):
        """
        円の中心位置を変更
        """
        self.x = x
        self.y = y

    def collide_circle(self, other):
        """
        円形同士の当たり判定
        """

        distance = math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
        )

        return distance <= (
            self.radius
            + other.radius
        )

    def collide_rect(self, other):
        """
        円形と四角形の当たり判定
        """

        return other.collide_circle(self)

