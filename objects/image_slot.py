import pygame


class ImageSlot:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen, image):
        # 枠の背景
        pygame.draw.rect(screen, (40, 40, 40), self.rect)

        # 枠線
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 3)

        if image is None:
            return

        # 元画像のサイズ
        image_rect = image.get_rect()

        # 枠内に収まる倍率を計算
        scale_x = self.rect.width / image_rect.width
        scale_y = self.rect.height / image_rect.height
        scale = min(scale_x, scale_y)

        # 新しいサイズ
        new_width = max(1, int(image_rect.width * scale))
        new_height = max(1, int(image_rect.height * scale))

        # 画像をリサイズ
        resized_image = pygame.transform.smoothscale(
            image,
            (new_width, new_height)
        )

        # 枠の中央に配置
        resized_rect = resized_image.get_rect(
            center=self.rect.center
        )

        screen.blit(resized_image, resized_rect)