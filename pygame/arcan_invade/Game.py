import sys

import pygame as pg
pg.init()

import random
from sprites import Block, Player, Bullet, Ball
import params


class game():

    def reset(self, count, reset=False):
        self.level += 1.0
        self.add_ball()
        params.energy_reg += 0.005
        params.energy_max += 3
        for i in range(count):
            block = Block(self.level * 0.1)
            block.pos[0] = random.randrange(params.screen_width)
            if reset:
                block.pos[1] = random.randrange(-200, -100)
            else:
                block.pos[1] = random.randrange(params.screen_height - 100)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

    def add_ball(self):
        ball = Ball()
        self.all_sprites_list.add(ball)
        self.ball_list.add(ball)

    def __init__(self):
        # Init Display
        self.screen = pg.display.set_mode([params.screen_width, params.screen_height], params.screen_mode)
        # Init Font
        self.font = pg.font.SysFont('Calibri', 25, True, False)

        # Init Sprite Lists
        self.block_list = pg.sprite.Group()
        self.bullet_list = pg.sprite.Group()
        self.all_sprites_list = pg.sprite.Group()
        self.ball_list = pg.sprite.Group()

        # Add Blocks and ball
        self.level = 0
        self.energy = params.energy
        self.energy_max = params.energy_max
        self.energy_reg = params.energy_reg
        self.shoot_speed = params.shoot_speed
        self.reset(50)

        # Add Player
        self.player = Player()
        self.all_sprites_list.add(self.player)
        self.player.rect.y = params.screen_height - self.player.height - 5

    # **** Ball Collisions ****

    def check_ball_wall_collision(self):
        for ball in self.ball_list:
            x = ball.pos[0]
            y = ball.pos[1]
            r = ball.rad
            if x < 0 or x + 2*r > params.screen_width:
                ball.angle = -ball.angle
            if y < 0:
                ball.angle = 180 - ball.angle
            elif y + 2*r > params.screen_height:
                self.score -= 10
                self.all_sprites_list.remove(ball)
                self.ball_list.remove(ball)
                self.add_ball()

    def check_player_ball_collision(self):
        for ball in self.ball_list:
            if pg.sprite.collide_rect(self.player, ball):
                xb,yb = ball.pos
                xp = self.player.rect.x
                yp = self.player.rect.y
                ax = (xb - xp) / self.player.width * 180
                ball.angle = ax - 90

    def check_ball_block_collision(self):
        for ball in self.ball_list:
            block_hit_list = pg.sprite.spritecollide(ball, self.block_list, True)
            for block in block_hit_list:
                self.score += 1
                xb,yb = ball.pos
                xp = block.rect.x
                yp = block.rect.y
                angle = ball.angle
                if xp < xb and xb < xp + block.width:
                    ball.angle = 180 - angle
                else:
                    ball.angle = -angle

    # **** Bullet Collisions ****

    def check_bullet_block_collision(self):
        for bullet in self.bullet_list:
            blocks_hit_list = pg.sprite.spritecollide(bullet, self.block_list, True)
            for blocks in blocks_hit_list:
                self.score += 1
                self.bullet_list.remove(bullet)
                self.all_sprites_list.remove(bullet)
            # bullets shall disappear, when out of screen
            if bullet.rect.y < -10:
                self.bullet_list.remove(bullet)
                self.all_sprites_list.remove(bullet)

    # **** Player Collisions ****

    def check_player_block_collision(self):
        block_hit_list = pg.sprite.spritecollide(self.player, self.block_list, True)
        for block in block_hit_list:
            self.score -= 20

    def run(self):
        # init additional gameparams
        clock = pg.time.Clock()
        self.score = 0
        tick = 0
        # game loop
        while True:
            #Eventhandling
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    sys.exit(0)

            # Mousebutton handling
            left, middle, right = pg.mouse.get_pressed()
            if left:
                tick += 1
                if self.energy > 1 and not tick%self.shoot_speed:
                    self.energy -= 1
                    bullet = Bullet()
                    bullet.rect.x = self.player.rect.x + self.player.width / 2 - bullet.width / 2
                    bullet.rect.y = self.player.rect.y
                    self.all_sprites_list.add(bullet)
                    self.bullet_list.add(bullet)
            else:
                tick = 0

            if self.energy < self.energy_max:
                self.energy += self.energy_reg

            #Gamelogic

            self.screen.fill(pg.Color('white'))
            self.all_sprites_list.update()

            self.check_player_ball_collision()
            self.check_ball_block_collision()
            self.check_bullet_block_collision()
            self.check_player_block_collision()
            self.check_ball_wall_collision()

            # add additional blocks
            if len(self.block_list) < 10:
                self.reset(20, True)

            # write stats on screen
            text = self.font.render('Score : {score}'.format(score=str(self.score)), True, pg.Color('black'))
            self.screen.blit(text, [50, 50])
            text = self.font.render('Level : {level}'.format(level=str(int(self.level))), True, pg.Color('black'))
            self.screen.blit(text, [250, 50])
            text = self.font.render('Energy : {energy}'.format(energy=str(self.energy)), True, pg.Color('blue'))
            self.screen.blit(text, [450, 50])

            # print sprites
            self.all_sprites_list.draw(self.screen)

            # print screen
            pg.display.flip()
            clock.tick(60)
