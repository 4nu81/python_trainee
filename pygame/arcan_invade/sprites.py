import pygame as pg
import random
import math

class Block(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([40, 20])
        self.image.fill(pg.Color('black'))

        self.rect = self.image.get_rect()
        self.game = game
        self.width = 40
        self.height = 20
        self.pos = [50,50]

    def reset_pos(self):
        self.rect.y = random.randrange(-100, -10)
        self.rect.x = random.randrange(self.game.screen_width)

    def update(self):
        self.pos[1] += 0.1
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])
        if self.rect.y > self.game.screen_height:
            self.reset_pos()

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.width = 100
        self.height = 20
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([self.width, self.height])
        #self.image = pg.image.load("player.png").convert()
        #self.image.set_colorkey(pg.Color('white'))
        self.image.fill(pg.Color('red'))

        self.rect = self.image.get_rect()
        self.game = game

    def update(self):
        pos = pg.mouse.get_pos()
        self.rect.x = pos[0] - self.width / 2

class Bullet(pg.sprite.Sprite):
    def __init__(self, game):
        self.width = 4
        self.height = 10
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([self.width,self.height])
        self.image.fill(pg.Color('red'))
        self.rect = self.image.get_rect()
        self.game = game

    def update(self):
        self.rect.y -= 3

class Ball(pg.sprite.Sprite):
    def __init__(self, game):
        
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([10,10])
        self.image = pg.image.load('ball.png').convert()
        self.image.set_colorkey(pg.Color('black'))

        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = 50
        self.rect.y = 50
        self.angle = 180
        self.speed = 2
        self.rad = 5
        self.pos = [50.0,50.0]

    def update(self):
        self.pos[0] += math.sin(self.angle * math.pi / 180.0) * self.speed
        self.pos[1] -= math.cos(self.angle * math.pi / 180.0) * self.speed
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])
