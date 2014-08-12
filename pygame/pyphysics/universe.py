#! /usr/bin/python

import pygame
import random
import PyParticles
import math

pygame.display.set_caption('Universe')
(width, height) = (1000,800)
screen = pygame.display.set_mode((width, height))

def calculateRadius(mass):
    return 0.4 * mass ** (0.5)

class Creator:
    def __init__(self, universe, (x, y)):
        self.universe = universe
        self.x = x
        self.y = y
        self.mass = random.randint(1,4)
        self.size = calculateRadius(self.mass)

    def release(self, (x, y)):
        dx = self.x - x
        dy = self.y - y
        speed = math.hypot(dx, dy) * 0.1
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        self.universe.addParticles(
            x=self.x,
            y=self.y,
            mass=self.mass,
            size=size,
            color=(255,255,255),
            speed=speed,
            angle=angle
        )

class UniverseScreen:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        (self.dx, self.dy) = (0,0)
        (self.mx, self.my) = (0,0)
        self.magnification = 1.0
        self.paused = False

    def scroll(self, dx=0, dy=0):
        self.dx += dx * width / (self.magnification * 10)
        self.dy += dy * height / (self.magnification * 10)

    def zoom(self, zoom):
        self.magnification *= zoom
        self.mx = (1-self.magnification) * self.width / 2
        self.my = (1-self.magnification) * self.height / 2

    def reset(self):
        (self.dx, self.dy) = (0,0)
        (self.mx, self.my) = (0,0)
        self.magnification = 1.0

    def set_paused(self):
         self.paused = (True, False)[self.paused]
### Main Program

universe = PyParticles.Environment((width, height))
universe.color = (0,0,0)

key_to_function = {
    pygame.K_LEFT:      (lambda x: x.scroll(dx=1)),
    pygame.K_RIGHT:     (lambda x: x.scroll(dx=-1)),
    pygame.K_UP:        (lambda x: x.scroll(dy=1)),
    pygame.K_DOWN:      (lambda x: x.scroll(dy=-1)),
    pygame.K_KP_PLUS:   (lambda x: x.zoom(2)),
    pygame.K_KP_MINUS:  (lambda x: x.zoom(0.5)),
    pygame.K_r:         (lambda x: x.reset()),
    pygame.K_SPACE:     (lambda x: x.set_paused())
}

universe.addFunctions([
    'move',
    'attract',
    'combine',
    #'outofbounds',
    #'accelerate',
    #'collide',
    #'bounce',
    #'drag',
])

universe_screen = UniverseScreen(width, height)

def create_particle():
    particle_mass = random.randint(1,4)
    particle_size = calculateRadius(particle_mass)
    speed = 0
    universe.addParticles(mass=particle_mass, size=particle_size,color=(255,255,255),speed=speed)

for p in range(100):
    create_particle()

running = True
creator = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                (x,y) = pygame.mouse.get_pos()
                x = int((x - universe_screen.mx) / universe_screen.magnification - universe_screen.dx)
                y = int((y - universe_screen.my) / universe_screen.magnification - universe_screen.dy)
                creator = Creator(universe, (x,y))
            if right:
                for p in range(10):
                    create_particle()
        elif event.type == pygame.MOUSEBUTTONUP:
            if creator:
                (x,y) = pygame.mouse.get_pos()
                x = int((x - universe_screen.mx) / universe_screen.magnification - universe_screen.dx)
                y = int((y - universe_screen.my) / universe_screen.magnification - universe_screen.dy)
                creator.release((x,y))
                creator = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key in key_to_function:
                key_to_function[event.key](universe_screen)

    if not universe_screen.paused:
        universe.update()
    screen.fill(universe.color)

    particles_to_remove = []

    if creator:
        (x,y) = pygame.mouse.get_pos()
        (cx,cy) = (creator.x, creator.y)
        cx = int(universe_screen.mx + (universe_screen.dx + cx) * universe_screen.magnification)
        cy = int(universe_screen.my + (universe_screen.dy + cy) * universe_screen.magnification)
        pygame.draw.line(screen, (255,0,0), (cx, cy), (x,y), 2)

    for p in universe.particles:
        if 'collide_with' in p.__dict__:
            particles_to_remove.append(p.collide_with)
            p.size = calculateRadius(p.mass)
        if 'toremove' in p.__dict__:
            particles_to_remove.append(p)

        x = int(universe_screen.mx + (universe_screen.dx + p.x) * universe_screen.magnification)
        y = int(universe_screen.my + (universe_screen.dy + p.y) * universe_screen.magnification)
        size = int(p.size * universe_screen.magnification)

        if size < 2:
            pygame.draw.rect(screen, p.color, (x, y, 2, 2,))
        else:
            pygame.draw.ellipse(screen, (205,255,255), (x - size, y - size, 2 * size, 2 * size))
    for p in particles_to_remove:
        if p in universe.particles:
            universe.particles.remove(p)
    pygame.display.flip()

