import pygame


class PlayArea:

    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self.right = left + width
        self.bottom = top + height

    def contains(self, x, y, width=0, height=0):
        """オブジェクトがプレイ範囲内にいるか"""

        return (
            x + width > self.left
            and
            x < self.right
            and
            y + height > self.top
            and
            y < self.bottom
        )

    def is_outside(self, x, y, width=0, height=0):
        """オブジェクトが完全に範囲外に出たか"""

        return not self.contains(
            x,
            y,
            width,
            height
        )