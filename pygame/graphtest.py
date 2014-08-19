import sys
import pygame as pg
import random
import math

LEFT = 1
RIGHT = 3
colors = ['red','white','blue','orange','pink','green','aquamarine','azure','gold','orangered','purple','yellow']

random.seed()
pg.init() 

width = 500
height = 500

class ball:
    def __init__(self, name, pos, color, radius, angle, speed):
        self.name = name
        self.pos = pos
        self.color = color
        self.radius = radius
        self.angle = angle
        self.speed = speed

    def move(self):
        x,y = self.pos
        x += math.sin(self.angle * math.pi / 180) * self.speed
        y -= math.cos(self.angle * math.pi / 180) * self.speed
        self.pos = (x,y)

class pool:
    def __init__(self):
        self.grav = 0.01
        self.balls = []
        self.window = pg.display.set_mode((width, height), pg.DOUBLEBUF)
        for n in range(1):
            self.create_rand_ball(n)

    def sim(self):
        for ball in self.balls:
            ball.move()

    def check_kollision(self):
        for i in range(0,len(self.balls) - 1):
            for j in range(i, len(self.balls)):
                ball1 = self.balls[i]
                x1,y1 = ball1.pos
                ball2 = self.balls[j]
                x2,y2 = ball2.pos
                d = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
                if d < (ball1.radius + ball2.radius):
                    if x2 - x1 == 0:
                        x2 = 0.1
                    angl = math.atan((y2 - y1) / (x2 - x1)) + 90
                    ball1.angle = angl - ball1.angle
                    ball2.angle = angl - ball2.angle
        for ball in self.balls:
            if (ball.pos[0] - ball.radius) < 0 or (ball.pos[0] + ball.radius) > width:
                ball.angle = -ball.angle
            if (ball.pos[1] - ball.radius) < 0 or (ball.pos[1] + ball.radius) > height:
                ball.angle = 180 - ball.angle

            while ball.angle > 360:
                ball.angle -= 360
            while ball.angle < 0:
                ball.angle += 360

    def run(self):
        while True:
            self.sim()
            self.check_kollision()
            self.draw_balls()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.create_rand_ball('mb', pos=event.pos)
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == RIGHT:
                    self.remove(event.pos)
                elif event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    sys.exit(0)

    def remove(self, pos):
        for ball in self.balls:
            x,y = pos
            xb, yb = ball.pos
            r = ball.radius
            if x > xb - r and x < xb + r and y > yb - r and y < yb + r:
                self.clear_ball(ball)
                self.balls.remove(ball)

    def draw_balls(self):
        self.window.fill((0,0,0))
        for ball in self.balls:
            x = int(ball.pos[0])
            y = int(ball.pos[1])
            pg.draw.circle(self.window, ball.color, (x, y), ball.radius)
        pg.display.flip()

    def create_rand_ball(self, name, pos=None):
        rad = random.randint(15, 20)
        if not pos:
            pos = (random.randint(rad, width - rad),random.randint(rad, height - rad))
        scol = colors[random.randint(0,len(colors)-1)]
        col = pg.Color(scol)
        speed = random.random()
        direction = random.uniform(0,360)
        b = ball(name, pos, col, rad, direction, speed)
        self.balls.append(b)

if __name__ == '__main__':
    p = pool()
    p.run()
