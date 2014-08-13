#! /usr/bin/python

import pygame
import random
import math

(width, height) = (600, 400)

gravity = (180, 0.1)
drag = 0.999
elasticity = 0.75

random.seed()

background_color = (255, 255, 255)

class Game():

    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Physics')
        self.sprite_list = pygame.sprite.Group()

        for i in range(50):
            self.create_particle()

    def collision(self):
        for i in range(len(self.sprite_list) - 1):
            for j in range(i, len(self.sprite_list)):
                p1 = self.sprite_list.sprites()[i]
                p2 = self.sprite_list.sprites()[j]
                collide(p1,p2)

    def create_particle(self):
        #rad = random.randint(20,40)
        rad = 20
        x = random.randint(rad, width - rad)
        y = random.randint(rad, height - rad)
        angle = random.randint(0,360)
        speed = random.uniform(0,3)
        particle = Particle(x, y, rad, angle, speed)
        self.sprite_list.add(particle)

    def run(self):
        clock = pygame.time.Clock()
        self.selected_particle = None
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_RETURN:
                        self.create_particle()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    self.selected_particle = findParticle(self.sprite_list, mouseX, mouseY)
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_particle:
                        x,y = pygame.mouse.get_pos()
                        dx = x - self.selected_particle.x
                        dy = self.selected_particle.y - y
                        self.selected_particle.angle = (0.5 * math.pi - math.atan2(dy, dx)) * 180 / math.pi
                        self.selected_particle.speed = math.hypot(dx, dy) * 0.2
                    self.selected_particle = None

            if self.selected_particle:
                x,y = pygame.mouse.get_pos()
                self.selected_particle.x = x
                self.selected_particle.y = y

            for particle in self.sprite_list:
                particle.bounce()
            self.sprite_list.update()
            self.collision()
            self.screen.fill(background_color)
            self.sprite_list.draw(self.screen)
            pygame.display.flip()
            clock.tick(60)

if __name__ == '__main__':
    g = Game()
    g.run()
