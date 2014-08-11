import pygame as pg

infoObject = pg.display.Info()

screen_width = infoObject.current_w
screen_height= infoObject.current_h

screen_width = 800
screen_height= 600
screen_mode  = 0 #pg.FULLSCREEN

energy = 15
energy_reg = 0.02
energy_max = 20
shoot_speed = 4
