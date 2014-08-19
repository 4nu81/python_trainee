import pygame
from pygame.locals import *
import os, sys
import Settings
pygame.init()
def main():
    selections = Settings.main(1)
##    selections = [0, 5]
    if selections[0] is 1:  Fullscreen = 1
    else:  Fullscreen = 0
    if selections[1] is 1:  screen=[620, 480]
    elif selections[1] is 2:  screen=[640, 480]
    elif selections[1] is 3:  screen=[800, 600]
    elif selections[1] is 4:  screen=[800, 640]
    elif selections[1] is 5:  screen=[1024, 768]
    elif selections[1] is 6:  screen=[1152, 864]
    elif selections[1] is 7:  screen=[1280, 720]
    elif selections[1] is 8:  screen=[1280, 960]
    elif selections[1] is 9:  screen=[1280, 1024]
    elif selections[1] is 10:  screen=[1440, 900]
    if Fullscreen is 1:  surface = pygame.display.set_mode((screen[0], screen[1]), FULLSCREEN, 16)
    else:  surface = pygame.display.set_mode((screen[0], screen[1]), 16)
    return surface, screen
