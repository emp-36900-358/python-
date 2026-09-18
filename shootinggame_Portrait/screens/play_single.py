import pygame

from objects.player import Player
from objects.bullet import PlayerBullet
from objects.playarea import PlayArea
from objects.enemy import Enemy
from objects.life_gauge import LifeGauge


WIDTH = 600
HEIGHT = 800


class SinglePlayScene:

    def __init__(self, game_data, player_count=1, play_area=None):

        self.game_data = game_data
        self.player_count = player_count
        self.play_area = play_area

        # ====================================
        # 1P用プレイエリア
        # ====================================

        self.play_area = PlayArea(
            0,
            0,
            600,
            800
        )

        # ====================================
        # プレイヤー
        # ====================================

        self.player = Player(
            300,
            700,
            self.game_data.ship,
            1,
            self.play_area
        )

        self.player_dead = False

        self.life_gauge = LifeGauge(
            self.game_data.ship,
            life=4,
            x=20,
            y=50
        )  

      # ====================================
        # 弾
        # ====================================

        self.player_bullets = []

        self.shot_cooldown = 0

        # ====================================
        # ステージ
        # ====================================

        self.start_stage()

    # ========================================
    # プレイヤー移動範囲制限
    # ========================================

    def limit_player_position(self):

        # 自機画像の大きさ
        player_width = self.player.image.get_width()
        player_height = self.player.image.get_height()

        # 左
        min_x = self.play_area.left

        # 右
        max_x = self.play_area.right - player_width

        # 上
        min_y = self.play_area.top

        # 下
        max_y = self.play_area.bottom - player_height

        # 範囲内に収める
        self.player.x = max(
            min_x,
            min(max_x, self.player.x)
        )

        self.player.y = max(
            min_y,
            min(max_y, self.player.y)
        )


    # ========================================
    # ステージ開始
    # ========================================

    def start_stage(self):

        stage = self.game_data.stage

        print("STAGE", stage, "START")

        # ====================================
        # ステージごとの敵数
        # ====================================

        if stage == 1:

            self.enemy_count = 10

        elif stage == 2:

            self.enemy_count = 15

        elif stage == 3:

            self.enemy_count = 20

        else:

            self.enemy_count = 10

        # ====================================
        # 敵リスト
        # ====================================

        self.enemies = []

        # ====================================
        # 敵生成
        # ====================================

        for i in range(self.enemy_count):

            x = 50 + (i % 5) * 120
            y = 100 + (i // 5) * 80

            # ステージごとに敵タイプを変更5
            if stage == 1:

                enemy_type = 1

            elif stage == 2:
                    
                    enemy_type = 2

            else:

                enemy_type = 3


            enemy = Enemy(
                x,
                y,
                enemy_type
            )

            self.enemies.append(enemy)

    # ========================================
    # 更新
    # ========================================

    def update_player(self):

        self.player.update()
        self.limit_player_position()

    def update_shooting(self):

        if self.shot_cooldown > 0:
            self.shot_cooldown -= 1

        if not self.player_dead and self.player.is_shooting() and self.shot_cooldown <= 0:
            bullet = PlayerBullet(
                self.player.x + self.player.image.get_width() // 2,
                self.player.y - 30,
                self.game_data.bullet
            )
            self.player_bullets.append(bullet)
            self.shot_cooldown = 10

    def update_bullets(self):

        for bullet in self.player_bullets:
            bullet.update()

        self.player_bullets = [
            bullet for bullet in self.player_bullets
            if not bullet.is_outside()
        ]

    def update_enemies(self):

        for enemy in self.enemies:
            enemy.update()

    def handle_player_enemy_collision(self):

       if not self.player_dead:

        hit_enemy = None

        for enemy in self.enemies:

            if self.player.hitbox.collide_rect(enemy.hitbox):
                hit_enemy = enemy
                break

        if hit_enemy is not None:

            self.player_dead = True

            # 残機を1減らす
            self.life_gauge.damage(1)

            # 衝突した敵を削除
            self.enemies.remove(hit_enemy)

    def handle_bullet_enemy_collisions(self):

        remaining_enemies = []

        for enemy in self.enemies:
            hit = False
            for bullet in self.player_bullets:
                if bullet.hitbox.collide_rect(enemy.hitbox):
                    hit = True
                    if bullet in self.player_bullets:
                        self.player_bullets.remove(bullet)
                    break

            if not hit:
                remaining_enemies.append(enemy)

        self.enemies = remaining_enemies

    def handle_stage_progress(self):

        if self.enemies:
            return "play_single"

        if self.game_data.stage < 3:
            self.game_data.stage += 1
            self.start_stage()
            return "play_single"

        return "game_clear"

    def update(self, events):

        self.update_player()
        self.update_shooting()
        self.update_bullets()
        self.update_enemies()
        self.handle_player_enemy_collision()
        self.handle_bullet_enemy_collisions()
        if self.player_dead:
            
            return "game_over"

        return self.handle_stage_progress()

    # ========================================
    # 描画
    # ========================================

    def draw(self, screen):

        screen.fill((0, 0, 0))

        # ====================================
        # ステージ表示
        # ====================================

        font = pygame.font.SysFont(None, 36)

        stage_text = font.render(
            f"STAGE {self.game_data.stage}",
            True,
            (255, 255, 255)
        )

        screen.blit(
            stage_text,
            (20, 20)
        )

        # ====================================
        # プレイヤー
        # ====================================

        if not self.player_dead:
            self.player.draw(screen)

        # ====================================
        # プレイヤー弾
        # ====================================

        for bullet in self.player_bullets:

            bullet.draw(screen)

        # ====================================
        # 敵
        # ====================================

        for enemy in self.enemies:

            enemy.draw(screen)

        self.life_gauge.draw(screen)
        

