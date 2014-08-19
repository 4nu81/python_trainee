from padlib import *
def shadow(position,occluders):
    s = Shadow(100,position,occluders,(255,255,255),20)
    return s
def exhaustsystem():
    position = (0,0)
##    colors = [(255,0,0),(255,255,0),(0,255,0),(0,255,255),(0,0,255),(0,0,0)]
    colors = [(255,0,0),(255,128,0),(255,255,0),(128,0,0),(0,0,0)]
    speeds = [11.25,45]
    disperse = 8
    direction = 0
    density = 4
    framestolast = 50
    p = particle_system(position,colors,speeds,disperse,direction,density,framestolast)
    return p
def turnexhaustsystem():
    position = (0,0)
    colors = [(255,0,0),(255,128,0),(255,255,0),(128,0,0),(0,0,0)]
    speeds = [7.5,15]
    disperse = 45
    direction = 0
    density = 16
    framestolast = 10
    p = particle_system(position,colors,speeds,disperse,direction,density,framestolast)
    return p
def selfexplosion(pos):
    position = pos
    colors = [(255,0,0),(255,128,0),(255,255,0),(128,0,0),(0,0,0)]
    speeds = [3,45]
    disperse = 360
    direction = 0
    density = 32
    framestolast = 50
    p = particle_system(position,colors,speeds,disperse,direction,density,framestolast)
    return p
def enemyexplosion(pos):
    position = pos
    colors = [(255,0,0),(255,128,0),(255,255,0),(128,0,0),(0,0,0)]
    speeds = [1.5,22.5]
    disperse = 360
    direction = 0
    density = 16
    framestolast = 50
    p = particle_system(position,colors,speeds,disperse,direction,density,framestolast)
    return p
def bulletimpact(pos):
    position = pos
    colors = [(255,0,0),(255,128,0),(255,255,0),(128,0,0),(0,0,0)]
    speeds = [7.5,15]
    disperse = 360
    direction = 0
    density = 4
    framestolast = 50
    p = particle_system(position,colors,speeds,disperse,direction,density,framestolast)
    return p
