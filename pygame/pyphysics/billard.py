#! /usr/bin/python

import pygame
import PyParticles
import math

pygame.display.set_caption('Billard')
(width, height) = (800,800)
screen = pygame.display.set_mode((width, height))

pygame.init()

font = pygame.font.SysFont('Calibri', 20, True, False)

colors = [
    ('',  pygame.Color('white'),        pygame.Color('white')),
    ('3', pygame.Color('red'),          pygame.Color('white')),
    ('2', pygame.Color('blue'),         pygame.Color('white')),
    ('1', pygame.Color('yellow'),       pygame.Color('black')),
    ('4', pygame.Color('darkorchid'),   pygame.Color('white')),
    ('5', pygame.Color('orange'),       pygame.Color('black')),
    ('6', pygame.Color('green4'),       pygame.Color('white')),
    ('7', pygame.Color('brown'),        pygame.Color('white')),
    ('8', pygame.Color('black'),        pygame.Color('white')),
]

class Hitter:
    def __init__(self, ball):
        self.ball = ball

    def release(self, (x, y)):
        dx = self.ball.x - x
        dy = self.ball.y - y
        speed = math.hypot(dx, dy) * 0.02
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        self.ball.angle = angle
        self.ball.speed = speed

# Main Programm

env = PyParticles.Environment((width, height),bounds=((100,100),(width-100,height-100)))
env.color = (0,100,0)

for i in range(len(colors)):
    name, color, textcolor = colors[i]
    env.addParticles(color=color,size=10,speed=0,mass=1000,name=name,textcolor=textcolor)

env.addFunctions([
    'move',
    'collide',
    'bounce',
    'drag',
])
env.gravity = (math.pi, 0)

running = True
hitter = None
selected_particle = None

while running:
    # Eventhandler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                (x,y) = pygame.mouse.get_pos()
                selected_particle = env.findParticle((x,y))
                if selected_particle:
                    hitter = Hitter(selected_particle)
            elif right:
                env.addParticles()
            elif middle:
                p = env.findParticle(pygame.mouse.get_pos())
                if p:
                    env.particles.remove(p)
        elif event.type == pygame.MOUSEBUTTONUP:
            if hitter:
                hitter.release(pygame.mouse.get_pos())
                hitter = None
            selected_particle = None

    # Tisch zeichnen
    screen.fill((0,0,0))
    pygame.draw.rect(screen, env.color, ((100,100),(width - 200, height - 200)),)

    # Stosslinie zeichnen
    if hitter:
        pygame.draw.line(screen, (255,0,0), (hitter.ball.x, hitter.ball.y), (pygame.mouse.get_pos()), 2)

    # Ballbewegung berechnen
    env.update()

    # Baelle zeichnen
    for p in env.particles:
        pygame.draw.circle(screen, (0,0,0), (int(p.x), int(p.y)), p.size + 1, 1)
        pygame.draw.ellipse(screen, p.color, (int(p.x) - p.size, int(p.y) - p.size, 2 * p.size, 2 * p.size))
        text = font.render('{name}'.format(name=p.name), True, p.textcolor)
        screen.blit(text, [p.x - 4, p.y - 7])
    # Auf display darstellen
    pygame.display.flip()

# end
