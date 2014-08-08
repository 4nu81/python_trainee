import sys
import pygame as pg
import random
from sprites import Block, Player, Bullet, Ball

pg.init()

class game():

    infoObject = pg.display.Info()

    screen_width = infoObject.current_w
    screen_height= infoObject.current_h

    def reset(self, count, reset=False):
        for i in range(count):
            block = Block(self)
            block.pos[0] = random.randrange(game.screen_width)
            if reset:
                block.pos[1] = random.randrange(-200, -100)
            else:
                block.pos[1] = random.randrange(game.screen_height - 100)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

    def add_ball(self):
        self.ball = Ball(self)
        self.all_sprites_list.add(self.ball)

    def __init__(self):
        self.screen = pg.display.set_mode([game.screen_width, game.screen_height], pg.FULLSCREEN)

        self.block_list = pg.sprite.Group()
        self.bullet_list = pg.sprite.Group()
        self.all_sprites_list = pg.sprite.Group()

        self.reset(50)

        self.player = Player(self)
        self.all_sprites_list.add(self.player)
        self.player.rect.y = game.screen_height - self.player.height - 5

        self.add_ball()

        self.font = pg.font.SysFont('Calibri', 25, True, False)

    def check_ball_wall_collision(self):
        x = self.ball.pos[0]
        y = self.ball.pos[1]
        r = self.ball.rad
        if x < 0 or x + 2*r > game.screen_width:
            self.ball.angle = -self.ball.angle
        if y < 0:
            self.ball.angle = 180 - self.ball.angle
        elif y + 2*r > game.screen_height:
            self.score -= 10
            self.all_sprites_list.remove(self.ball)
            self.add_ball()

        while self.ball.angle > 360:
            self.ball.angle -= 360
        while self.ball.angle < 0:
            self.ball.angle += 360

    def check_player_ball_collision(self):
        if pg.sprite.collide_rect(self.player, self.ball):
            xb,yb = self.ball.pos
            xp = self.player.rect.x
            yp = self.player.rect.y

            ax = (xb - xp) / self.player.width * 180
            self.ball.angle = ax - 90

    def check_ball_block_collision(self):

        block_hit_list = pg.sprite.spritecollide(self.ball, self.block_list, True)
        for block in block_hit_list:
            self.score += 1
            xb,yb = self.ball.pos
            xp = block.rect.x
            yp = block.rect.y
            angle = self.ball.angle
            if xp < xb and xb < xp + block.width:
                self.ball.angle = 180 - angle
            else:
                self.ball.angle = -angle

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

    def check_player_block_collision(self):
        block_hit_list = pg.sprite.spritecollide(self.player, self.block_list, True)
        for block in block_hit_list:
            self.score -= 20

    def run(self):
        clock = pg.time.Clock()
        self.score = 0

        while True:

            #Eventhandling
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    bullet = Bullet(self)
                    bullet.rect.x = self.player.rect.x + self.player.width / 2 - bullet.width / 2
                    bullet.rect.y = self.player.rect.y
                    self.all_sprites_list.add(bullet)
                    self.bullet_list.add(bullet)
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    sys.exit(0)

            #Gamelogic

            self.screen.fill(pg.Color('white'))
            self.all_sprites_list.update()

            self.check_player_ball_collision()
            self.check_ball_block_collision()
            self.check_bullet_block_collision()
            self.check_player_block_collision()
            self.check_ball_wall_collision()

            if len(self.block_list) < 10:
                self.reset(20, True)

            text = self.font.render('Score : {score}'.format(score=str(self.score)), True, pg.Color('black'))
            self.screen.blit(text, [50, 50])

            self.all_sprites_list.draw(self.screen)
            pg.display.flip()
            clock.tick(60)

def main():
    g = game()
    g.run()

main()
