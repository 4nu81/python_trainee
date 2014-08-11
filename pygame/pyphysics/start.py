#! /usr/bin/python

import pygame
import PyParticles

pygame.display.set_caption('Modulize')
(width, height) = (400,400)
screen = pygame.display.set_mode((width, height))


env = PyParticles.Environment((width, height))
env.addParticles(5)
running = True
selected_particle = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                selected_particle = env.findParticle(pygame.mouse.get_pos())
            elif right:
                env.addParticles()
            elif middle:
                p = env.findParticle(pygame.mouse.get_pos())
                if p:
                    env.particles.remove(p)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        selected_particle.mouseMove(pygame.mouse.get_pos())

    screen.fill(env.color)

    env.update()

    for p in env.particles:
        #pygame.draw.circle(screen, p.color, (int(p.x), int(p.y)), p.size, p.thickness)
        pygame.draw.ellipse(screen, p.color, (int(p.x) - p.size, int(p.y) - p.size, 2 * p.size, 2 * p.size))
    pygame.display.flip()
