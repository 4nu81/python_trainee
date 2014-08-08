import sys
import pygame as pg
import random

pg.init()

screen_width = 800
screen_height= 600

class Block(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([40, 20])
        self.image.fill(pg.Color('black'))

        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-100, -10)
        self.rect.x = random.randrange(screen_width)

    def update(self):
        self.rect.y += 1
        if self.rect.y > screen_height:
            self.reset_pos()

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([20, 20])
        self.image.fill(pg.Color('red'))

        self.rect = self.image.get_rect()

    def update(self):
        pos = pg.mouse.get_pos()
        self.rect.x = pos[0]

class Bullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([4,10])
        self.image.fill(pg.Color('black'))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3

class game():

    def reset(self, count, reset=False):
        for i in range(count):
            block = Block()
            block.rect.x = random.randrange(screen_width)
            if reset:
                block.rect.y = random.randrange(-200, -100)
            else:
                block.rect.y = random.randrange(screen_height - 100)
            
            self.block_list.add(block)
            self.all_sprites_list.add(block)


    def __init__(self):
        self.screen = pg.display.set_mode([screen_width, screen_height])

        self.block_list = pg.sprite.Group()
        self.bullet_list = pg.sprite.Group()
        self.all_sprites_list = pg.sprite.Group()

        self.reset(50)

        self.player = Player()
        self.all_sprites_list.add(self.player)
        self.player.rect.y = screen_height - 50

        self.font = pg.font.SysFont('Calibri', 25, True, False)


    def run(self):
        clock = pg.time.Clock()
        score = 0

        while True:

            #Eventhandling
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    bullet = Bullet()
                    bullet.rect.x = self.player.rect.x + 8
                    bullet.rect.y = self.player.rect.y
                    self.all_sprites_list.add(bullet)
                    self.bullet_list.add(bullet)

            #Gamelogic

            self.screen.fill(pg.Color('white'))
            self.all_sprites_list.update()

            # Treffer mit den Bullets
            for bullet in self.bullet_list:            
                blocks_hit_list = pg.sprite.spritecollide(bullet, self.block_list, True)
                for blocks in blocks_hit_list:
                    score += 1
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

                if len(self.block_list) < 10:
                    self.reset(20, True)

            # Punktabzug bei Kollision mit Block
            block_hit_list = pg.sprite.spritecollide(self.player, self.block_list, True)
            for block in block_hit_list:
                score -= 20

            text = self.font.render('Score : {score}'.format(score=str(score)), True, pg.Color('black'))
            self.screen.blit(text, [50,550])

            self.all_sprites_list.draw(self.screen)
            pg.display.flip()
            clock.tick(60)

def main():
    g = game()
    g.run()

main()
