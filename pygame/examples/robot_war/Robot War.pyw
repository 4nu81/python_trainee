import pygame
from pygame.locals import *
import sys, os
import math
if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
import surface
pygame.init()

surface, screen = surface.main()
pygame.display.set_caption("Robot War")

font = pygame.font.SysFont("Times New Roman",12)

Robot1 = pygame.image.load("Data/Robot1_1.png").convert()
Robot2 = pygame.image.load("Data/Robot2_1.png").convert()
Smoke = pygame.image.load("Data/Smoke.png").convert_alpha()
Smoke.set_alpha(0)

player1pos = [50.0, 50.0]
player2pos = [screen[0]-50, screen[1]-50]
player1score = 0
player2score = 0
player1rot = 0.0
player2rot = 0.0
player1bullets = []
player2bullets = []
player1smoke = []
player2smoke = []

frames = 0
fps = 0

class bullet:
    def __init__(self, x, y, rot):
        self.x = x
        self.y = y
        self.speedx = -2*math.sin(math.radians(rot))
        self.speedy = -2*math.cos(math.radians(rot))
        self.rot = rot
class smoke_particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 1

def get_input():
    global player1pos, player2pos
    global player1rot, player2rot
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT: pygame.quit();sys.exit()
    if keystate[K_ESCAPE]: pygame.quit();sys.exit()
    if keystate[K_UP]: player1pos[1] -= math.cos(math.radians(player1rot)); player1pos[0] -= math.sin(math.radians(player1rot))
    if keystate[K_DOWN]: player1pos[1] += math.cos(math.radians(player1rot)); player1pos[0] += math.sin(math.radians(player1rot))
    if keystate[K_LEFT]: player1rot += 1
    if keystate[K_RIGHT]: player1rot -= 1
    if keystate[K_w]: player2pos[1] -= math.cos(math.radians(player2rot)); player2pos[0] -= math.sin(math.radians(player2rot))
    if keystate[K_s]: player2pos[1] += math.cos(math.radians(player2rot)); player2pos[0] += math.sin(math.radians(player2rot))
    if keystate[K_a]: player2rot += 1
    if keystate[K_d]: player2rot -= 1
    if keystate[K_RCTRL] and frames%15 == 0: player1bullets.append(bullet(player1pos[0],player1pos[1],player1rot))
    if keystate[K_LCTRL] and frames%15 == 0: player2bullets.append(bullet(player2pos[0],player2pos[1],player2rot))
    
def draw():
    surface.fill((255,255,255))

    draw = pygame.transform.rotate(Robot1, player1rot)
    height = draw.get_height()/2.0
    draw.set_colorkey((0,128,0))
    surface.blit(draw, (player1pos[0]-(height), player1pos[1]-(height)))

    draw = pygame.transform.rotate(Robot2, player2rot)
    height = draw.get_height()/2.0
    draw.set_colorkey((0,128,0))
    surface.blit(draw, (player2pos[0]-(height), player2pos[1]-(height)))

    for bullet in player1bullets:
        pygame.draw.line(surface, (255,255,0),(  bullet.x+(2.5*math.cos(math.radians(-bullet.rot+90))), bullet.y+(2.5*math.sin(math.radians(-bullet.rot+90)))  ),(  bullet.x+(2.5*math.cos(math.radians(-bullet.rot-90))), bullet.y+(2.5*math.sin(math.radians(-bullet.rot-90)))  ),1)
        pygame.draw.line(surface, (202,124,0),(  bullet.x+(2.2*math.cos(math.radians(-bullet.rot+89))), bullet.y+(2.2*math.sin(math.radians(-bullet.rot+89)))  ),(  bullet.x+(2.2*math.cos(math.radians(-bullet.rot-91))), bullet.y+(2.2*math.sin(math.radians(-bullet.rot-91)))  ),1)
        pygame.draw.line(surface, (202,124,0),(  bullet.x+(2.2*math.cos(math.radians(-bullet.rot+91))), bullet.y+(2.2*math.sin(math.radians(-bullet.rot+91)))  ),(  bullet.x+(2.2*math.cos(math.radians(-bullet.rot-89))), bullet.y+(2.2*math.sin(math.radians(-bullet.rot-89)))  ),1)
    for bullet in player2bullets:
##        pygame.draw.rect(surface,(255,255,0),(bullet.x,bullet.y,5,5),0)
        pygame.draw.line(surface, (255,255,0),(  bullet.x+(2.5*math.cos(math.radians(-bullet.rot+90))), bullet.y+(2.5*math.sin(math.radians(-bullet.rot+90)))  ),(  bullet.x+(2.5*math.cos(math.radians(-bullet.rot-90))), bullet.y+(2.5*math.sin(math.radians(-bullet.rot-90)))  ),1)
        pygame.draw.line(surface, (202,124,0),(  bullet.x+(2.2*math.cos(math.radians(-bullet.rot+89))), bullet.y+(2.2*math.sin(math.radians(-bullet.rot+89)))  ),(  bullet.x+(2.2*math.cos(math.radians(-bullet.rot-91))), bullet.y+(2.2*math.sin(math.radians(-bullet.rot-91)))  ),1)
        pygame.draw.line(surface, (202,124,0),(  bullet.x+(2.2*math.cos(math.radians(-bullet.rot+91))), bullet.y+(2.2*math.sin(math.radians(-bullet.rot+91)))  ),(  bullet.x+(2.2*math.cos(math.radians(-bullet.rot-89))), bullet.y+(2.2*math.sin(math.radians(-bullet.rot-89)))  ),1)
    for smokeparticle in player1smoke:
        DrawSmoke = pygame.transform.scale(Smoke, (smokeparticle.size, smokeparticle.size))
        height = DrawSmoke.get_height()/2.0
        surface.blit(DrawSmoke, (smokeparticle.x-height+5,smokeparticle.y-height+5))
        if smokeparticle.size == 90:
            player1smoke.remove(smokeparticle)
    for smokeparticle in player2smoke:
        DrawSmoke = pygame.transform.scale(Smoke, (smokeparticle.size, smokeparticle.size))
        height = DrawSmoke.get_height()/2.0
        surface.blit(DrawSmoke, (smokeparticle.x-height+5,smokeparticle.y-height+5))
        if smokeparticle.size == 90:
            player2smoke.remove(smokeparticle)

    info1 = font.render("Player 1 score = "+str(player1score), True, (0,0,0))
    surface.blit(info1, (5,0))
    info2 = font.render("Player 2 score = "+str(player2score), True, (0,0,0))
    surface.blit(info2, (screen[0]-110,0))
    drawfps = font.render("fps = "+str(int(fps)), True, (0,0,0))
    surface.blit(drawfps, (5,12))

    pygame.display.flip()

def move_bullets():
    for bullet in player1bullets:
        bullet.x += bullet.speedx
        bullet.y += bullet.speedy
    for bullet in player2bullets:
        bullet.x += bullet.speedx
        bullet.y += bullet.speedy

def update_smoke():
    global player1smoke, player2smoke, frames
    if frames % 25 == 0: #every 25th frame...
        if frames >= 25*7:
            player1smoke = player1smoke[1:]
            player2smoke = player2smoke[1:]
        player1smoke.append( smoke_particle(player1pos[0]-5, player1pos[1]-5) )
        player2smoke.append( smoke_particle(player2pos[0]-5, player2pos[1]-5) )
    if frames % 2 == 0: #every 3rd frame...
        for particle in player1smoke:
            particle.size += 1
        for particle in player2smoke:
            particle.size += 1

def collision_detect():
    global player1score, player2score
    global player1pos, player2pos
    for bullet in player1bullets:
        if abs(bullet.x - player2pos[0]) <= 20 and abs(bullet.y - player2pos[1]) <= 20: player1bullets.remove(bullet);player1score += 1
        elif bullet.x < 0 or bullet.x > screen[0] or bullet.y < 0 or bullet.y > screen[1]: player1bullets.remove(bullet)
    for bullet in player2bullets:
        if abs(bullet.x - player1pos[0]) <= 20 and abs(bullet.y - player1pos[1]) <= 20: player2bullets.remove(bullet);player2score += 1
        elif bullet.x < 0 or bullet.x > screen[0] or bullet.y < 0 or bullet.y > screen[1]: player2bullets.remove(bullet)

    if player1pos[0] < 0: player1pos[0] = 0
    if player1pos[1] < 0: player1pos[1] = 0
    if player1pos[0] > screen[0]: player1pos[0] = screen[0]
    if player1pos[1] > screen[1]: player1pos[1] = screen[1]

    if player2pos[0] < 0: player2pos[0] = 0
    if player2pos[1] < 0: player2pos[1] = 0
    if player2pos[0] > screen[0]: player2pos[0] = screen[0]
    if player2pos[1] > screen[1]: player2pos[1] = screen[1]

def main():
    global fps, frames
    Clock = pygame.time.Clock()
    while True:
        get_input()
        move_bullets()
        update_smoke()
        collision_detect()
        draw()

        fps = Clock.get_fps()
        Clock.tick()

        frames += 1

if __name__ == "__main__": main()
