# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from padlib import *
import sys, os
import Settings
if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

Screen = (800,600)
icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("Battle for Planet Vector - Ian Mallett - v.6.0.0 - May 2008")
Surface = pygame.display.set_mode(Screen)

LEFTTURN,RIGHTTURN,FIRE,THRUST,PSDDENSITY,LIGHT,THRUSTOCCLUDE,TURNOCCLUDE,EXPLODEOCCLUDE,BULLETOCCLUDE,MUSICVOLUME,FXVOLUME = Settings.LoadSettings()

MenuHover  = pygame.mixer.Sound("Data/Sound/MenuHover.ogg")
MenuAction = pygame.mixer.Sound("Data/Sound/MenuAction.ogg")
Font  = pygame.font.Font("Data/Fonts/Font2.ttf",24)#30
Font2 = pygame.font.Font("Data/Fonts/Font2.ttf",12)#15
Font3 = pygame.font.Font("Data/Fonts/Font2.ttf",16)#20
#Main Menu
MainBegin       = Font.render("Begin",True,(255,255,255))
MainOptions     = Font.render("Options",True,(255,255,255))
MainStory       = Font.render("Story",True,(255,255,255))
MainQuit        = Font.render("Quit",True,(255,255,255))
MainBG          = pygame.image.load("Data/Menus/MainMenu.png").convert()
#Options Menu
OptionsKeyboard = Font3.render("Keyboard:",True,(255,255,255))
OptionsThrust   = Font2.render("Thrust Key:",True,(255,255,255))
OptionsLeft     = Font2.render("Turn Left Key:",True,(255,255,255))
OptionsRight    = Font2.render("Turn Right Key:",True,(255,255,255))
OptionsFire     = Font2.render("Fire Key:",True,(255,255,255))

OptionsEffects  = Font3.render("Effects:",True,(255,255,255))
OptionsPSD      = Font2.render("Particle System Density:",True,(255,255,255))
OptionsLightOn  = Font2.render("Enable Ship Lighting:",True,(255,255,255))
OptionsThOcc    = Font2.render("Thrust Occlude:",True,(255,255,255))
OptionsTuOcc    = Font2.render("Turn Occlude:",True,(255,255,255))
OptionsExOcc    = Font2.render("Explosions Occlude:",True,(255,255,255))
OptionsBuOcc    = Font2.render("Bullets Occlude:",True,(255,255,255))

OptionsSound    = Font3.render("Sound:",True,(255,255,255))
OptionsMusic    = Font2.render("Music Volume:",True,(255,255,255))
OptionsSFX      = Font2.render("Effects Volume:",True,(255,255,255))
OptionsBG     = pygame.image.load("Data/Menus/OptionsMenu.png").convert()
OptionsSlider = pygame.image.load("Data/Menus/Slider.png").convert_alpha()
#Story Menu
Story1          = Font2.render("For many aeons, the Rigel star system had harbored four planets within its brilliant blue glow.  The first,",True,(255,255,255))
Story2          = Font2.render("and hottest, was named Triagma, and was rich in minerals and caked in molten lead.  The second,",True,(255,255,255))
Story3          = Font2.render("Sigma, was entirely encased within an azure shell of water.  Its oceans held secrets and wealth be-",True,(255,255,255))
Story4          = Font2.render("-neath their cryptic waters.  The third, and only inhabited planet, Vector, was a small little world,",True,(255,255,255))
Story5          = Font2.render("with lakes and rivers, trees and plants, and you.  Here in this microcosm, you and your people have",True,(255,255,255))
Story6          = Font2.render("lived together, seeking peace and happiness; prosperity in harmony with others and Planet Vector--until now.",True,(255,255,255))

Story7          = Font2.render("Rigel has just exploded.  The shockwave deeply penetrated the Triagma and Sigma, destroying them, while",True,(255,255,255))
Story8          = Font2.render("severely shaking Vector--at this present time, no artificial structures have been observed standing.  Capitalizing",True,(255,255,255))
Story9          = Font2.render("on Vector's vulnerability, the inhabitants of Rigel's neighboring system have attacked the weakened planet.",True,(255,255,255))
Story10         = Font2.render("They have realized that the most effective way to conquer your world is to colonize it immediately.  With",True,(255,255,255))
Story11         = Font2.render("no base, Vector's forces will be left out in the open, as an airplane with nowhere to land.  In addition,",True,(255,255,255))
Story12         = Font2.render("the inhabitants of Vector will have nowhere to go.",True,(255,255,255))

Story13         = Font2.render("Recognizing Vector's peril, you boarded Vector's most powerful spaceship, before it was catured, and set",True,(255,255,255))
Story14         = Font2.render("out on a one person mission to destroy those who would take your home world from you.",True,(255,255,255))

Story15         = Font2.render("Their strategy will be most elementary.  They have already suceeded in installing turrets on Vector's",True,(255,255,255))
Story16         = Font2.render("surface.  For your own safety, these should be avoided, as it is inauspicious to the ship's integrity to be",True,(255,255,255))
Story17         = Font2.render("exposed to the invaders' fire.  With the object of landing as many units on the surface as possible,",True,(255,255,255))
Story18         = Font2.render("they will send transports, and everything from miniscule robotic drones to intergalactic crusiers to",True,(255,255,255))
Story19         = Font2.render("defend them.",True,(255,255,255))

Story20         = Font2.render("You are one ship, and the odds are stacked against you.  Your self-assigned mission is to demolish",True,(255,255,255))
Story21         = Font2.render("the invasion force to the best of your ability.  Your efforts may give Vector a chance to recover, or,",True,(255,255,255))
Story22         = Font2.render("at least, provide an obstacle to the opposition's sucess.  Destroy as much as you can.",True,(255,255,255))

Story23         = Font2.render("Keep your wits.",True,(255,255,255))
StoryBG         = pygame.image.load("Data/Menus/StoryMenu.png").convert()

Menu = "Main"

def Collide(surf,blitpos):
    if mpos[0] > blitpos[0]:
        if mpos[1] > blitpos[1]:
            size = surf.get_size()
            if mpos[0] < blitpos[0] + size[0]:
                if mpos[1] < blitpos[1] + size[1]:
                    if Hovering == False: MenuHover.play(0)
                    return True
    return False
pressing = False
def GetInput():
    global mpos, Hovering, Menu, pressing
    global LEFTTURN, RIGHTTURN, THRUST, FIRE
    global PSDDENSITY, THRUSTOCCLUDE, TURNOCCLUDE, EXPLODEOCCLUDE, LIGHT, BULLETOCCLUDE
    global MUSICVOLUME, FXVOLUME
    key = pygame.key.get_pressed()
    mpos = pygame.mouse.get_pos()
    mpress = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(); sys.exit()
        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            if Menu == "Story":
                Menu = "Main"; MenuAction.play(0)
        if event.type == KEYDOWN and Menu == "Options":
            if   Hovering == 1: MenuAction.play(0); LEFTTURN = event.key
            elif Hovering == 2: MenuAction.play(0); RIGHTTURN = event.key
            elif Hovering == 3: MenuAction.play(0); THRUST = event.key
            elif Hovering == 4: MenuAction.play(0); FIRE = event.key
    if Menu == "Main":
        if   Collide(MainBegin,  (170,250)): Hovering = 1
        elif Collide(MainOptions,(170,300)): Hovering = 2
        elif Collide(MainStory,  (170,350)): Hovering = 3
        elif Collide(MainQuit,   (170,400)): Hovering = 4
        else: Hovering = False
        if mpress[0]:
            if Hovering != False:
                MenuAction.play(0)
                if   Hovering == 1: return "Start Game"
                elif Hovering == 2:
                    Menu = "Options"
                    LEFTTURN,RIGHTTURN,FIRE,THRUST,PSDDENSITY,LIGHT,THRUSTOCCLUDE,TURNOCCLUDE,EXPLODEOCCLUDE,BULLETOCCLUDE,MUSICVOLUME,FXVOLUME = Settings.LoadSettings()
                elif Hovering == 3: Menu = "Story"
                elif Hovering == 4: pygame.quit(); sys.exit()
    elif Menu == "Options":
        try:
            if mpos[0] > mainrectpos[0] and mpos[0] < mainrectpos[0]+mainrectsize[0]:
                if mpos[1] > mainrectpos[1] and mpos[1] < mainrectpos[1]+mainrectsize[1]:
                    tmphover = Hovering
                    Hovering = False
                    if (mpos[1] > keyboardyrows[0] and mpos[1] < keyboardyrows[0]+15): Hovering = 1
                    if (mpos[1] > keyboardyrows[1] and mpos[1] < keyboardyrows[1]+15): Hovering = 2
                    if (mpos[1] > keyboardyrows[2] and mpos[1] < keyboardyrows[2]+15): Hovering = 3
                    if (mpos[1] > keyboardyrows[3] and mpos[1] < keyboardyrows[3]+15): Hovering = 4
                    if (mpos[0] >= MenuBarLeft and mpos[0] <= (MenuBarLeft+15)):
                        if mpos[1] > effectyrows[1] and mpos[1] < effectyrows[1]+15:
                            Hovering = 5
                            if mpress[0]:
                                if not pressing:
                                    pressing = True; LIGHT = not LIGHT; MenuAction.play(0)
                        if LIGHT:
                            if mpos[1] > effectyrows[5] and mpos[1] < effectyrows[5]+15:
                                Hovering = 6
                                if mpress[0]:
                                    if not pressing:
                                        pressing = True; BULLETOCCLUDE = not BULLETOCCLUDE; MenuAction.play(0)
                    if (mpos[0] > MenuBarLeft+6 and mpos[0] < MenuBarLeft+157-7):
                        if mpos[1] > effectyrows[0] and mpos[1] < effectyrows[0]+15:
                            Hovering = 7
                            if mpress[0]:
                                LeftAmt = mpos[0]-(MenuBarLeft+6)
                                tmpPSDDENSITY = rndint(LeftAmt/9.0)
                                if tmpPSDDENSITY != PSDDENSITY: PSDDENSITY = tmpPSDDENSITY; MenuAction.play(0)
                                while THRUSTOCCLUDE > PSDDENSITY: THRUSTOCCLUDE -= 1
                                while TURNOCCLUDE > PSDDENSITY: TURNOCCLUDE -= 1
                        if LIGHT:
                            if mpos[1] > effectyrows[2] and mpos[1] < effectyrows[2]+15:
                                Hovering = 8
                                if mpress[0]:
                                    LeftAmt = mpos[0]-(MenuBarLeft+6)
                                    tmpTHRUSTOCCLUDE = rndint(LeftAmt/(144.0/float(PSDDENSITY)))
                                    if tmpTHRUSTOCCLUDE != THRUSTOCCLUDE: THRUSTOCCLUDE = tmpTHRUSTOCCLUDE; MenuAction.play(0)
                            if mpos[1] > effectyrows[3] and mpos[1] < effectyrows[3]+15:
                                Hovering = 9
                                if mpress[0]:
                                    LeftAmt = mpos[0]-(MenuBarLeft+6)
                                    tmpTURNOCCLUDE = rndint(LeftAmt/(144.0/float(PSDDENSITY)))
                                    if tmpTURNOCCLUDE != TURNOCCLUDE: TURNOCCLUDE = tmpTURNOCCLUDE; MenuAction.play(0)
                            if mpos[1] > effectyrows[4] and mpos[1] < effectyrows[4]+15:
                                Hovering = 10
                                if mpress[0]:
                                    LeftAmt = mpos[0]-(MenuBarLeft+6)
                                    tmpEXPLODEOCCLUDE = rndint(LeftAmt/(144/4.0))
                                    if tmpEXPLODEOCCLUDE != EXPLODEOCCLUDE: EXPLODEOCCLUDE = tmpEXPLODEOCCLUDE; MenuAction.play(0)
                        if (mpos[1] > soundyrows[0] and mpos[1] < soundyrows[0]+15):
                            Hovering = 11
                            if mpress[0]:
                                LeftAmt = mpos[0]-(MenuBarLeft+6)
                                MUSICVOLUME = LeftAmt/144.0
                        if (mpos[1] > soundyrows[1] and mpos[1] < soundyrows[1]+15):
                            Hovering = 12
                            if mpress[0]:
                                LeftAmt = mpos[0]-(MenuBarLeft+6)
                                FXVOLUME = LeftAmt/144.0
                                MenuHover.set_volume(FXVOLUME)
                                MenuAction.set_volume(FXVOLUME)
                    if tmphover != Hovering and Hovering != False: MenuHover.play(0)
        except:pass
        if key[K_ESCAPE]:
            Menu = "Main"
            MenuAction.play(0)
            Settings.WriteSettings(LEFTTURN,RIGHTTURN,FIRE,THRUST,PSDDENSITY,LIGHT,THRUSTOCCLUDE,TURNOCCLUDE,EXPLODEOCCLUDE,BULLETOCCLUDE,MUSICVOLUME,FXVOLUME)
    if not mpress[0]:
        pressing = False
def rndint(num):
    return int(round(num))
Hovering = False
def DrawRect(Rect,lvl=1,roundedness=7):
    if lvl == 1:
        color1 = (32,32,32)
        color2 = (128,128,128)
    elif lvl == 2:
        color1 = (48,48,48)
        color2 = (128,128,128)
    if Rect != None:
        RoundedRect(Surface,color1,Rect,roundedness)
        RoundedRect(Surface,color2,Rect,roundedness,1)
def Draw():
    global Hovering, keyboardyrows,effectyrows,soundyrows,mainrectpos,mainrectsize,MenuBarLeft
    if Menu == "Main":
        Surface.blit(MainBG,(0,0))
        Rect = None
        if   Hovering == 1: Rect = (164,250,72,32)
        elif Hovering == 2: Rect = (164,300,98,32)
        elif Hovering == 3: Rect = (164,350,69,32)
        elif Hovering == 4: Rect = (164,400,61,32)
        DrawRect(Rect)
        Surface.blit(MainBegin,  (170,250))
        Surface.blit(MainOptions,(170,300))
        Surface.blit(MainStory,  (170,350))
        Surface.blit(MainQuit,   (170,400))
    if Menu == "Options":
        Surface.blit(OptionsBG,(0,0))
        mainrectsize = (350,300)
        subrectpadding = 10
        mainrectpos = (50,rndint((Screen[1]-mainrectsize[1])/2.0))
        DrawRect((mainrectpos[0],mainrectpos[1],mainrectsize[0],mainrectsize[1]))
        subrects = (5,7,3)
        rectspaceavailable = mainrectsize[1]-(subrectpadding*(len(subrects)+1))
        xcounter = 0
        textspacecounter = 0
        for rect in subrects:
            xcounter += (rect+1)
            textspacecounter += 20
            textspacecounter += ((rect-1)*15)
        x = float(rectspaceavailable-textspacecounter)/float(xcounter)
        rectsizes = []
        for rect in subrects:
            xsize = mainrectsize[0]-(2*subrectpadding)
            ysize = 20+((rect-1)*15)+((rect+1)*x)
            rectsizes.append((xsize,ysize))
        rectpositions = []
        rectcounter = 0
        currentyposition = mainrectpos[1]+10
        for rect in subrects:
            xpos = mainrectpos[0]+subrectpadding
            ypos = currentyposition
            rectpositions.append((xpos,ypos))
            currentyposition += rectsizes[rectcounter][1]
            currentyposition += 10
            rectcounter += 1
        rectnumber = 0
        for rect in subrects:
            xpos = rectpositions[rectnumber][0]
            ypos = rectpositions[rectnumber][1]
            xsize = rectsizes[rectnumber][0]
            ysize = rectsizes[rectnumber][1]
            DrawRect((rndint(xpos),rndint(ypos),rndint(xsize),rndint(ysize)),2)
            if   rectnumber == 0:
                keyboardyrows = [rndint(ypos+x+20+x)-2,
                                 rndint(ypos+x+20+x+15+x)-2,
                                 rndint(ypos+x+20+x+15+x+15+x)-2,
                                 rndint(ypos+x+20+x+15+x+15+x+15+x)-2]
                if Hovering != False and Hovering <= 4: DrawRect((rndint(xpos+8),keyboardyrows[Hovering-1],mainrectsize[0]-(4*subrectpadding),15))
                Surface.blit(OptionsKeyboard,(rndint(xpos+8),rndint(ypos+x)))
                LK = Font2.render(pygame.key.name(LEFTTURN),True,(255,255,255))
                RK = Font2.render(pygame.key.name(RIGHTTURN),True,(255,255,255))
                TK = Font2.render(pygame.key.name(THRUST),True,(255,255,255))
                FK = Font2.render(pygame.key.name(FIRE),True,(255,255,255))
                Surface.blit(OptionsLeft,  (rndint(xpos+16),keyboardyrows[0])); Surface.blit(LK,(rndint(xpos+128),keyboardyrows[0]))
                Surface.blit(OptionsRight, (rndint(xpos+16),keyboardyrows[1])); Surface.blit(RK,(rndint(xpos+128),keyboardyrows[1]))
                Surface.blit(OptionsThrust,(rndint(xpos+16),keyboardyrows[2])); Surface.blit(TK,(rndint(xpos+128),keyboardyrows[2]))
                Surface.blit(OptionsFire,  (rndint(xpos+16),keyboardyrows[3])); Surface.blit(FK,(rndint(xpos+128),keyboardyrows[3]))
            elif rectnumber == 1:
                Surface.blit(OptionsEffects,(rndint(xpos+8),rndint(ypos+x)))
                effectyrows = [rndint(ypos+x+20+x)-2,
                               rndint(ypos+x+20+x+15+x)-2,
                               rndint(ypos+x+20+x+15+x+15+x)-2,
                               rndint(ypos+x+20+x+15+x+15+x+15+x)-2,
                               rndint(ypos+x+20+x+15+x+15+x+15+x+15+x)-2,
                               rndint(ypos+x+20+x+15+x+15+x+15+x+15+x+15+x)-2]
                Surface.blit(OptionsPSD,    (rndint(xpos+16),effectyrows[0]))
                MenuBarLeft = rndint(xpos+xsize-subrectpadding-157)
                DrawRect((MenuBarLeft,effectyrows[0],157,15))
                for xtrans in xrange(0,144+9,9):
                    lefttrans = xtrans+6
                    pygame.draw.line(Surface,(64,64,64),(MenuBarLeft+lefttrans,effectyrows[0]+1),(MenuBarLeft+lefttrans,effectyrows[0]+13))
                Surface.blit(OptionsSlider,(MenuBarLeft+4+(9*PSDDENSITY),effectyrows[0]+1))
                
                Surface.blit(OptionsLightOn,(rndint(xpos+16),effectyrows[1]))
                DrawRect((MenuBarLeft,effectyrows[1],15,15),1,3)
                if LIGHT:
                    pygame.draw.line(Surface,(128,128,128),(MenuBarLeft+3,effectyrows[1]+3),(MenuBarLeft+11,effectyrows[1]+11))
                    pygame.draw.line(Surface,(128,128,128),(MenuBarLeft+3,effectyrows[1]+11),(MenuBarLeft+11,effectyrows[1]+3))
                
                Surface.blit(OptionsThOcc,  (rndint(xpos+24),effectyrows[2]))
                if PSDDENSITY != 0:
                    DrawRect((MenuBarLeft,effectyrows[2],157,15))
                    try:
                        step = 144.0/float(PSDDENSITY)
                        xtrans = 0
                        while xtrans <= 144:
                            lefttrans = xtrans+6
                            pygame.draw.line(Surface,(64,64,64),(MenuBarLeft+lefttrans,effectyrows[2]+1),(MenuBarLeft+lefttrans,effectyrows[2]+13))
                            xtrans += step
                        Surface.blit(OptionsSlider,(MenuBarLeft+4+(step*THRUSTOCCLUDE),effectyrows[2]+1))
                    except:pass
                
                Surface.blit(OptionsTuOcc,  (rndint(xpos+24),effectyrows[3]))
                if PSDDENSITY != 0:
                    DrawRect((MenuBarLeft,effectyrows[3],157,15))
                    try:
                        step = 144.0/float(PSDDENSITY)
                        xtrans = 0
                        while xtrans <= 144:
                            lefttrans = xtrans+6
                            pygame.draw.line(Surface,(64,64,64),(MenuBarLeft+lefttrans,effectyrows[3]+1),(MenuBarLeft+lefttrans,effectyrows[3]+13))
                            xtrans += step
                        Surface.blit(OptionsSlider,(MenuBarLeft+4+(step*TURNOCCLUDE),effectyrows[3]+1))
                    except:pass
                
                Surface.blit(OptionsExOcc,  (rndint(xpos+24),effectyrows[4]))
                DrawRect((MenuBarLeft,effectyrows[4],157,15))
                try:
                    step = 144.0/4.0
                    xtrans = 0
                    while xtrans <= 144:
                        lefttrans = xtrans+6
                        pygame.draw.line(Surface,(64,64,64),(MenuBarLeft+lefttrans,effectyrows[4]+1),(MenuBarLeft+lefttrans,effectyrows[4]+13))
                        xtrans += step
                    Surface.blit(OptionsSlider,(MenuBarLeft+4+(step*EXPLODEOCCLUDE),effectyrows[4]+1))
                except:pass
                
                Surface.blit(OptionsBuOcc,  (rndint(xpos+24),effectyrows[5]))
                DrawRect((MenuBarLeft,effectyrows[5],15,15),1,3)
                if BULLETOCCLUDE:
                    pygame.draw.line(Surface,(128,128,128),(MenuBarLeft+3,effectyrows[5]+3),(MenuBarLeft+11,effectyrows[5]+11))
                    pygame.draw.line(Surface,(128,128,128),(MenuBarLeft+3,effectyrows[5]+11),(MenuBarLeft+11,effectyrows[5]+3))
            elif rectnumber == 2:
                Surface.blit(OptionsSound,(rndint(xpos+8),rndint(ypos+x)))
                soundyrows = [rndint(ypos+x+20+x)-2,
                              rndint(ypos+x+20+x+15+x)-2]
                Surface.blit(OptionsMusic,(rndint(xpos+16),soundyrows[0]))
                DrawRect((MenuBarLeft,soundyrows[0],157,15))
                step = 3
                xtrans = 0
                while xtrans <= 144:
                    lefttrans = xtrans+6
                    pygame.draw.line(Surface,(64,64,64),(MenuBarLeft+lefttrans,soundyrows[0]+1),(MenuBarLeft+lefttrans,soundyrows[0]+13))
                    xtrans += step
                    Surface.blit(OptionsSlider,(rndint(MenuBarLeft+4+(144.0*MUSICVOLUME)),soundyrows[0]+1))
                Surface.blit(OptionsSFX,  (rndint(xpos+16),soundyrows[1]))
                
                DrawRect((MenuBarLeft,soundyrows[1],157,15))
                step = 3
                xtrans = 0
                while xtrans <= 144:
                    lefttrans = xtrans+6
                    pygame.draw.line(Surface,(64,64,64),(MenuBarLeft+lefttrans,soundyrows[1]+1),(MenuBarLeft+lefttrans,soundyrows[1]+13))
                    xtrans += step
                    Surface.blit(OptionsSlider,(rndint(MenuBarLeft+4+(144.0*FXVOLUME)),soundyrows[1]+1))
                Surface.blit(OptionsSFX,  (rndint(xpos+16),soundyrows[1]))
            rectnumber += 1
        if not LIGHT:
            blankedsurface = pygame.Surface((  rectsizes[1][0]-(2*subrectpadding),  (5*x)+(15*4)  ))
            blankedsurface.fill((48,48,48))
            blankedsurface.set_alpha(230)
            xpos = rectpositions[1][0]+subrectpadding
            ypos = rectpositions[1][1]+(4*x)+20+(2*15)-2
            Surface.blit(blankedsurface,(xpos,ypos))
    if Menu == "Story":
        Surface.blit(StoryBG,(0,0))
        
        Surface.blit(Story1,(140,25))
        Surface.blit(Story2,(147,40))
        Surface.blit(Story3,(155,55))
        Surface.blit(Story4,(161,70))
        Surface.blit(Story5,(169,85))
        Surface.blit(Story6,(177,100))
        
        Surface.blit(Story7,(189,130))
        Surface.blit(Story8,(196,145))
        Surface.blit(Story9,(203,160))
        Surface.blit(Story10,(210,175))
        Surface.blit(Story11,(215,190))
        Surface.blit(Story12,(220,205))

        Surface.blit(Story13,(230,235))
        Surface.blit(Story14,(234,250))

        Surface.blit(Story15,(241,280))
        Surface.blit(Story16,(245,295))
        Surface.blit(Story17,(248,310))
        Surface.blit(Story18,(250,325))
        Surface.blit(Story19,(253,340))

        Surface.blit(Story20,(255,370))
        Surface.blit(Story21,(258,385))
        Surface.blit(Story22,(260,400))

        Surface.blit(Story23,(262,460))
    pygame.display.flip()
def main():
    while True:
        ToDo = GetInput()
        if ToDo == "Start Game": break
        Draw()
    return LEFTTURN,RIGHTTURN,THRUST,FIRE,PSDDENSITY,LIGHT,THRUSTOCCLUDE,TURNOCCLUDE,EXPLODEOCCLUDE,BULLETOCCLUDE,MUSICVOLUME,FXVOLUME
