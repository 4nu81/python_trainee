import os
import sys
import vlc
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.quit()

icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("Create - Ian Mallett - v.1.0.5 - 2014")

fullscreen = True
def setup_display():
    global surface, screen_size

    flags = RESIZABLE
    if fullscreen:
        flags |= FULLSCREEN
        screen_size = [1920,1080]
    else:
        screen_size = [1920//2,1080//2]
    surface = pygame.display.set_mode(screen_size,flags)

    surface_movie = pygame.Surface(screen_size,HWSURFACE)
    surface_movie.fill((0,0,255))
setup_display()

vlc_instance = vlc.Instance()
media_a = vlc_instance.media_new("data/a.mp4")
media_b = vlc_instance.media_new("data/b.mp4")

vlc_player = vlc_instance.media_player_new()

win_id = pygame.display.get_wm_info()["window"]
if sys.platform == "linux2": # for Linux using the X Server
    vlc_player.set_xwindow(win_id)
elif sys.platform == "win32": # for Windows
    vlc_player.set_hwnd(win_id)
elif sys.platform == "darwin": # for MacOS
    vlc_player.set_agl(win_id)

def start():
    vlc_player.play()
    while not vlc_player.is_playing(): pass
def get_events():
    global fullscreen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if   event.key == K_ESCAPE:
                return False
##            elif event.key == K_f:
##                fullscreen = not fullscreen
##                setup_display()
    return True
def main_loops():
    vlc_player.set_media(media_a)
    start()

    while vlc_player.is_playing(): #vlc_player.get_state()!=vlc.State.Ended
        if not get_events():
            return

    vlc_player.set_media(media_b)
    
    while True:
        start()

        while vlc_player.is_playing():
            if not get_events():
                return
            
        vlc_player.stop()
        start()
pygame.mouse.set_visible(False)
main_loops()
pygame.mouse.set_visible(True)
pygame.quit()
sys.exit()
