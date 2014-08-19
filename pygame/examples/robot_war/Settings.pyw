def main(drawicon):
    import pygame, sys, os
    from pygame.locals import *
    pygame.init()

    if sys.platform == 'win32':
        os.environ['SDL_VIDEO_CENTERED'] = '1'
    surface = pygame.display.set_mode((275,86), 16)
    
    Fullscreen = pygame.image.load("Settings Data/Fullscreen.png").convert()
    ScreenDim = pygame.image.load("Settings Data/ScreenDim.png").convert()
    SelectBox = pygame.image.load("Settings Data/SelectBox.png").convert()
    SelectDone = pygame.image.load("Settings Data/SelectDone.png").convert()
    SelectDot = pygame.image.load("Settings Data/SelectDot.png").convert()
    CheckBox = pygame.image.load("Settings Data/CheckBox.png").convert()
    CheckDot = pygame.image.load("Settings Data/CheckDot.png").convert()
    icon = pygame.image.load("Settings Data/icon.png").convert()

    pygame.display.set_caption('Options')
    if drawicon == 1:
        pygame.display.set_icon(icon)

    selections = [None, 1]
    while 1:
        keystate = pygame.key.get_pressed()
        mpress = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keystate[K_ESCAPE]:
                pygame.quit()
                sys.exit()
        if keystate[K_RETURN] and selections[0] != None:
            break

        surface.blit(Fullscreen, (0,0))
        if (mpos[0] > 22 and mpos[0] < 35 and mpos[1] > 52 and mpos[1] < 65):
            if mpress[0]:
                if selections[0] == None:
                    surface = pygame.display.set_mode((275,128), 16)
                selections[0] = 1
            else:
                surface.blit(SelectBox, (22,52))
        elif (mpos[0] > 164 and mpos[0] < 177 and mpos[1] > 52 and mpos[1] < 65):
            if mpress[0]:
                if selections[0] == None:
                    surface = pygame.display.set_mode((275,128), 16)
                selections[0] = 2
            else:
                surface.blit(SelectBox, (164,52))
        elif (mpos[0] > 98 and mpos[0] < 176 and mpos[1] > 86 and mpos[1] < 107):
            surface.blit(SelectDone, (98,86))
            if mpress[0]:
                break
            
        if selections[0] == 1:  surface.blit(CheckBox, (22,52))
        elif selections[0] == 2:  surface.blit(CheckBox, (164,52))
        pygame.display.flip()
        
    surface = pygame.display.set_mode((195,291), 16)
    while 1:
        keystate = pygame.key.get_pressed()
        mpress = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keystate[K_ESCAPE]:
                pygame.quit()
                sys.exit()

        surface.blit(ScreenDim, (0,0))
        if (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 47 and mpos[1] < 60):
            surface.blit(SelectDot, (44,47))
            if mpress[0]:
                selections[1] = 1
        elif (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 66 and mpos[1] < 78):
            surface.blit(SelectDot, (44,66))
            if mpress[0]:
                selections[1] = 2
        elif (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 84 and mpos[1] < 97):
            surface.blit(SelectDot, (44,84))
            if mpress[0]:
                selections[1] = 3
        elif (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 103 and mpos[1] < 116):
            surface.blit(SelectDot, (44,103))
            if mpress[0]:
                selections[1] = 4
        elif (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 122 and mpos[1] < 135):
            surface.blit(SelectDot, (44,122))
            if mpress[0]:
                selections[1] = 5
        elif (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 141 and mpos[1] < 154):
            surface.blit(SelectDot, (44,141))
            if mpress[0]:
                selections[1] = 6
        elif (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 160 and mpos[1] < 173):
            surface.blit(SelectDot, (44,160))
            if mpress[0]:
                selections[1] = 7
        elif (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 179 and mpos[1] < 192):
            surface.blit(SelectDot, (44,179))
            if mpress[0]:
                selections[1] = 8
        elif (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 198 and mpos[1] < 211):
            surface.blit(SelectDot, (44,198))
            if mpress[0]:
                selections[1] = 9
        elif (mpos[0] > 44 and mpos[0] < 57 and mpos[1] > 217 and mpos[1] < 230):
            surface.blit(SelectDot, (44,217))
            if mpress[0]:
                selections[1] = 10
        elif (mpos[0] > 58 and mpos[0] < 136 and mpos[1] > 250 and mpos[1] < 271):
            surface.blit(SelectDone, (58,250))
            if mpress[0]:
                break

        if selections[1] == 1:  surface.blit(CheckDot, (44,47))
        elif selections[1] == 2:  surface.blit(CheckDot, (44,66))
        elif selections[1] == 3:  surface.blit(CheckDot, (44,84))
        elif selections[1] == 4:  surface.blit(CheckDot, (44,103))
        elif selections[1] == 5:  surface.blit(CheckDot, (44,122))
        elif selections[1] == 6:  surface.blit(CheckDot, (44,141))
        elif selections[1] == 7:  surface.blit(CheckDot, (44,160))
        elif selections[1] == 8:  surface.blit(CheckDot, (44,179))
        elif selections[1] == 9:  surface.blit(CheckDot, (44,198))
        elif selections[1] == 10:  surface.blit(CheckDot, (44,217))
            
        pygame.display.flip()
            
    return (selections[0], selections[1])
