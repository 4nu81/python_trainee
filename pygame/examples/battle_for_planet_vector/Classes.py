from math import *
from FX import *
import random
class Ship:
    def __init__(self):
        self.pos = [0,0]
        self.thrust = 0.12
        self.speed = [0.0,0.0]
        self.angle = 0
        self.angularspeed = 0
        self.points = [[10,0],[-2,5],[3,7],[-13,25],[-6,8],[-10,6],[-10,3],[-4,0],[-10,-3],[-10,-6],[-6,-8],[-13,-25],[3,-7],[-2,-5]]
        for p in self.points:
            p[0] += 4
        self.firing = 0
        self.health = 100
        self.beinghit = 0
        self.color = (255,255,255)
        self.deadtime = 0
    def move(self):
        self.angle += self.angularspeed
        if self.angularspeed < 0.0:
            self.angularspeed += 0.1125
        if self.angularspeed > 0.0:
            self.angularspeed -= 0.1125
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
class Enemy:
    def __init__(self,pos,type,angle=0):
        self.pos = pos
        self.angle = angle
        self.type = type
        self.onscreen = False
        self.beinghit = 0
        self.guns = None
        self.speed = [0.0,0.0]
        self.waitvar = 0
        self.launchvar = 0
        if self.type == "Transport":
            self.points = [(-55,15),(-50,15),(-50,3),(50,3),(50,15),(65,0),(50,-15),(50,-3),(-50,-3),(-50,-15),(-55,-15)]
            self.stamina = 10
            point = [57.5,0]
            self.guns = [EnemyGun(point)]
            self.hascargo = True
            self.boundradius = 55
            self.maxspeed = 1.5
        elif self.type == "Micro Fighter":
            self.points = [(10,0),(-10,5),(-10,-5)]
            self.stamina = 4
            self.boundradius = 10
            self.thrust = 0.12
        elif self.type == "Medium Cruiser":
            self.points = [(-25,10),(0,15),(-2,40),(4,20),(8,20),(10,13),(25,10),(33,7),(35,0),(33,-7),(25,-10),(10,-13),(8,-20),(4,-20),(-2,-40),(0,-15),(-25,-10)]
            self.stamina = 20
            self.guns = [EnemyGun((5,17)),EnemyGun((5,-17)),
                         EnemyGun((14,8)),EnemyGun((14,-8))]
            self.boundradius = 33
            self.thrust = 0.12
        elif self.type == "Medium Fighter":
            self.points = [(10,0),(1,5),(-2,15),(-10,20),(-3,5),(-3,-5),(-10,-20),(-2,-15),(1,-5)]
            self.stamina = 10
            self.boundradius = 20
            self.thrust = 0.12
        elif self.type == "Mini Gunship":
            self.points = [(-10,2),(-6,2),(-8,20),(-2,2),(-3,15),(2,2),(15,0),(2,-2),(-3,-15),(-2,-2),(-8,-20),(-6,-2),(-10,-2)]
            self.stamina = 5
            self.boundradius = 20
            self.thrust = 0.12
        elif self.type == "Turret":
            self.points = [(0,10),(10,8),(10,5),(5,5),(5,-5),(10,-5),(10,-8),(0,-10)]
            self.stamina = 25
            point = [self.pos[0],self.pos[1]]
            point[0] += 10.0*(cos(radians(self.angle)))
            point[1] += 10.0*(sin(radians(self.angle)))
            self.guns = [EnemyGun(point)]
            self.boundradius = 10
        elif self.type == "Heavy Cruiser":
            self.angle = random.randint(0,360)
            self.points = [(-100,-7),(-80,-2),(-77,-13),(-20,-13),(-20,-10),(35,-20),(40,-13),(50,-13),(50,-10),(95,-5),(100,0),
                           (95,5),(50,10),(50,13),(40,13),(35,20),(-20,10),(-20,13),(-77,13),(-80,2),(-100,7)]
            self.stamina = 50
            self.guns = [EnemyGun((32,14)),EnemyGun((32,-14)),
                         EnemyGun((22,12)),EnemyGun((22,-12)),
                         EnemyGun((12,10)),EnemyGun((12,-10)),
                         EnemyGun((2,8)),EnemyGun((2,-8)),
                         EnemyGun((-8,6)),EnemyGun((-8,-6))]
            self.boundradius = 100
            self.maxspeed = 0.5
        self.color = (255,255,255)
class EnemyGun:
    def __init__(self,pos):
        self.pos = pos
        self.relpos = pos
        self.angle = 0
        self.firing = 0
        self.points = []
        step = 36
        for angle in xrange(0,360+step,step):
            point = [5.0*cos(radians(angle)),5.0*sin(radians(angle))]
            self.points.append(point)
        self.points.append((10,0))
class Bullet:
    def __init__(self,pos,angle,selfspeed,owner,speed=9):
        self.pos = [pos[0],pos[1]]
        self.speed = [speed*cos(radians(angle))+selfspeed[0],
                      speed*sin(radians(angle))+selfspeed[1]]
        self.time = 0
        self.owner = owner
    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
class PlanetVector:
    def __init__(self,size):
        self.pos = [4000,4000]
        self.size = size
class Explosion:
    def __init__(self,pos):
        self.pos = pos
        self.kill = False
        self.ps = selfexplosion(self.pos)
        self.time = 0
    def update(self):
        self.ps.update()
        NewDensity = self.ps.density-1
        if NewDensity < 0:
            self.time += 1
            if self.time == 50:
                self.kill = True
        else:
            self.ps.change_density(NewDensity)
    def draw(self,Surface):
        self.ps.draw(Surface)
class EnemyExplosion:
    def __init__(self,pos):
        self.pos = pos
        self.kill = False
        self.ps = enemyexplosion(self.pos)
        self.time = 0
    def update(self):
        self.ps.update()
        NewDensity = self.ps.density-2
        if NewDensity < 0:
            self.time += 1
            if self.time == 50:
                self.kill = True
        else:
            self.ps.change_density(NewDensity)
    def draw(self,Surface):
        self.ps.draw(Surface)
class BulletImpact:
    def __init__(self,pos):
        self.pos = pos
        self.kill = False
        self.ps = bulletimpact(self.pos)
        self.time = 0
    def update(self):
        self.ps.update()
        NewDensity = self.ps.density-1
        if NewDensity < 0:
            self.time += 1
            if self.time == 50:
                self.kill = True
        else:
            self.ps.change_density(NewDensity)
    def draw(self,Surface):
        self.ps.draw(Surface)
class Star:
    def __init__(self,pos):
        self.pos = pos
