#! /usr/bin/python

import pygame
import PyParticles
import math

pygame.display.set_caption('Billard')
(width, height) = (800,800)
screen = pygame.display.set_mode((width, height))

class Hitter:
    def __init__(self, ball):
        self.ball = ball

    def release(self, (x, y)):
        dx = self.ball.x - x
        dy = self.ball.y - y
        speed = math.hypot(dx, dy) * 0.1
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        self.ball.angle = angle
        self.ball.speed = speed

env = PyParticles.Environment((width, height))
env.addParticles(5)
env.addFunctions([
    'move',
    #'accelerate',
    'collide',
    'bounce',
    'drag',
])
env.gravity = (math.pi, 0.001)
running = True
hitter = None
selected_particle = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                (x,y) = pygame.mouse.get_pos()
                selected_particle = env.findParticle((x,y))
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

    screen.fill(env.color)

    if hitter:
        pygame.draw.line(screen, (255,0,0), (hitter.ball.x, hitter.ball.y), (pygame.mouse.get_pos()), 2)
        #selected_particle.mouseMove(pygame.mouse.get_pos())

    env.update()

    for p in env.particles:
        #pygame.draw.circle(screen, p.color, (int(p.x), int(p.y)), p.size, p.thickness)
        pygame.draw.ellipse(screen, p.color, (int(p.x) - p.size, int(p.y) - p.size, 2 * p.size, 2 * p.size))
    pygame.display.flip()
