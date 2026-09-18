import pygame

from objects.player import Player
from objects.bullet import PlayerBullet
from objects.playarea import PlayArea
from objects.enemy import Enemy
from objects.life_gauge import LifeGauge


WIDTH = 600
HEIGHT = 800

CENTER_X = 300


class MultiPlayScene:

    def __init__(self, game_data, player_count=2, play_area=None):

        self.game_data = game_data
        self.player_count = player_count
        self.play_area = play_area

        # ==================================
        # 1Pの範囲
        # ==================================

        self.play_area_1p = PlayArea(
            0,
            0,
            300,
            800
        )

        # ==================================
        # 2Pの範囲
        # ==================================

        self.play_area_2p = PlayArea(
            300,
            0,
            300,
            800
        )

        # ==================================
        # P1
        # ==================================

        self.player_1p = Player(
            150,
            700,
            self.game_data.ship_1p,
            1,
            self.play_area_1p
        )

        # ==================================
        # P2
        # ==================================

        self.player_2p = Player(
            450,
            700,
            self.game_data.ship_2p,
            2,
            self.play_area_2p
        )

        self.player_1p_dead = False
        self.player_2p_dead = False

        # ==================================
        # 弾
        # ==================================

        self.player_bullets_1p = []
        self.player_bullets_2p = []

        # ==================================
        # 射撃クールダウン
        # ==================================

        self.shot_cooldown_1p = 0
        self.shot_cooldown_2p = 0

        # ==================================
        # ステージ開始
        # ==================================

        self.start_stage()

    # ======================================
    # P1 移動範囲制限
    # ======================================

    def limit_player_1p_position(self):

        player_width = self.player_1p.image.get_width()
        player_height = self.player_1p.image.get_height()

        min_x = self.play_area_1p.left
        max_x = self.play_area_1p.right - player_width

        min_y = self.play_area_1p.top
        max_y = self.play_area_1p.bottom - player_height

        self.player_1p.x = max(
            min_x,
            min(max_x, self.player_1p.x)
        )

        self.player_1p.y = max(
            min_y,
            min(max_y, self.player_1p.y)
        )

        # 当たり判定を合わせる
        self.player_1p.hitbox.set_position(
            self.player_1p.x + 10,
            self.player_1p.y + 10
        )

    # ======================================
    # P2 移動範囲制限
    # ======================================

    def limit_player_2p_position(self):

        player_width = self.player_2p.image.get_width()
        player_height = self.player_2p.image.get_height()

        min_x = self.play_area_2p.left
        max_x = self.play_area_2p.right - player_width

        min_y = self.play_area_2p.top
        max_y = self.play_area_2p.bottom - player_height

        self.player_2p.x = max(
            min_x,
            min(max_x, self.player_2p.x)
        )

        self.player_2p.y = max(
            min_y,
            min(max_y, self.player_2p.y)
        )

        # 当たり判定を合わせる
        self.player_2p.hitbox.set_position(
            self.player_2p.x + 10,
            self.player_2p.y + 10
        )

    # ======================================
    # ステージ開始
    # ======================================

    def start_stage(self):

        self.player_bullets_1p.clear()
        self.player_bullets_2p.clear()

        # ==================================
        # ステージごとの敵数
        # ==================================

        if self.game_data.stage == 1:

            self.enemy_count = 10

        elif self.game_data.stage == 2:

            self.enemy_count = 15

        elif self.game_data.stage == 3:

            self.enemy_count = 20

        else:

            self.enemy_count = 10

        # ==================================
        # 敵リスト
        # ==================================

        self.enemies = []

        # ==================================
        # 敵生成
        # ==================================

        for i in range(self.enemy_count):

            x = 30 + (i % 10) * 60
            y = 100 + (i // 10) * 70

            # ------------------------------
            # 敵タイプ
            # ------------------------------

            if self.game_data.stage == 1:

                enemy_type = 1

            elif self.game_data.stage == 2:

                enemy_type = 2

            else:
                    
                enemy_type = 3

            # ------------------------------
            # 敵生成
            # ------------------------------

            enemy = Enemy(
                x,
                y,
                enemy_type
            )

            self.enemies.append(enemy)

    # ======================================
    # ステージクリア
    # ======================================

    def stage_clear(self):

        if self.game_data.stage < 3:

            self.game_data.stage += 1

            self.start_stage()

            return False

        else:

            return True

    # ======================================
    # 更新
    # ======================================

    def _update_players(self):
        self.player_1p.update()
        self.player_2p.update()
        self.limit_player_1p_position()
        self.limit_player_2p_position()

    def _update_shot(self, player, bullets, cooldown_name, bullet_type):
        cooldown = getattr(self, cooldown_name)
        if cooldown > 0:
            cooldown -= 1
        if player.is_shooting() and cooldown <= 0:
            bullets.append(PlayerBullet(
                player.x + player.image.get_width() // 2,
                player.y - 30,
                bullet_type
            ))
            cooldown = 10
        setattr(self, cooldown_name, cooldown)

    def _update_bullets(self, bullets):
        for bullet in bullets:
            bullet.update()
        return [bullet for bullet in bullets if not bullet.is_outside()]

    def _remove_collisions(self):
        for player, dead in ((self.player_1p, "player_1p_dead"),
                             (self.player_2p, "player_2p_dead")):
            if not getattr(self, dead):
                hit = next((enemy for enemy in self.enemies
                            if player.hitbox.collide_rect(enemy.hitbox)), None)
                if hit is not None:
                    setattr(self, dead, True)
                    self.enemies.remove(hit)
        bullets = self.player_bullets_1p + self.player_bullets_2p
        remaining = []
        for enemy in self.enemies:
            hit = next((bullet for bullet in bullets
                        if bullet.hitbox.collide_rect(enemy.hitbox)), None)
            if hit is None:
                remaining.append(enemy)
            else:
                bullets.remove(hit)
        self.enemies = remaining

    def update(self, events):
        self._update_players()
        self._update_shot(self.player_1p, self.player_bullets_1p,
                          "shot_cooldown_1p", self.game_data.bullet_1p)
        self._update_shot(self.player_2p, self.player_bullets_2p,
                          "shot_cooldown_2p", self.game_data.bullet_2p)
        self.player_bullets_1p = self._update_bullets(self.player_bullets_1p)
        self.player_bullets_2p = self._update_bullets(self.player_bullets_2p)
        for enemy in self.enemies:
            enemy.update()
        self._remove_collisions()

        if self.player_1p_dead and self.player_2p_dead:
            return "game_over"


        # ==================================
        # 敵全滅
        # ==================================

        if len(self.enemies) == 0:

            clear = self.stage_clear()

            if clear:

                return "game_clear"

        return "play_multi"

    # ======================================
    # 描画
    # ======================================

    def draw(self, screen):

        screen.fill((0, 0, 0))

        # ==================================
        # 中央線
        # ==================================

        pygame.draw.line(
            screen,
            (255, 255, 255),
            (CENTER_X, 0),
            (CENTER_X, HEIGHT),
            2
        )

        # ==================================
        # ステージ表示
        # ==================================

        font = pygame.font.SysFont(None, 30)

        stage_text = font.render(
            f"STAGE {self.game_data.stage}",
            True,
            (255, 255, 255)
        )

        screen.blit(
            stage_text,
            (10, 10)
        )

        # ==================================
        # プレイヤー
        # ==================================

        if not self.player_1p_dead:
            self.player_1p.draw(screen)

        if not self.player_2p_dead:
            self.player_2p.draw(screen)

        # ==================================
        # P1 弾
        # ==================================

        for bullet in self.player_bullets_1p:

            bullet.draw(screen)

        # ==================================
        # P2 弾
        # ==================================

        for bullet in self.player_bullets_2p:

            bullet.draw(screen)

        # ==================================
        # 敵
        # ==================================

        for enemy in self.enemies:

            enemy.draw(screen)
