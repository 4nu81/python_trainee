import pygame
from pygame.locals import *
from padlib import *
from Classes import *
from FX import *
from Maths import *
import Menu
from random import *
import sys, os
if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

def Init():
    global Screen,Surface,Clock,Font,sFire,sThrust,sMusic,FireChannel,ThrustChannel,BulletHitChannels,MusicChannel,BulletHitSounds,player,Planet
    global Stars1,Stars2,Stars3,Explosions,Bullets,Enemies,ExhaustL,ExhaustR,TurnerFL,TurnerFR,TurnerBL,TurnerBR,BulletImpacts
    Screen = (800,600)
    icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
    pygame.display.set_caption("Battle for Planet Vector - Ian Mallett - v.6.0.0 - May 2008")
    Surface = pygame.display.set_mode(Screen)

    Clock = pygame.time.Clock()
    Font = pygame.font.Font("Data/Fonts/Font.ttf",12)
    sFire = pygame.mixer.Sound("Data/Sound/Fire.ogg")
    sThrust = pygame.mixer.Sound("Data/Sound/Thrust.ogg")
    sMusic = pygame.mixer.Sound("Data/Sound/Music"+str(choice([1,2,3,4]))+".ogg")
    sMusic.set_volume(0.4*MUSICVOLUME)
    FireChannel = pygame.mixer.Channel(0);   FireChannel.set_volume(0.25*FXVOLUME)
    ThrustChannel = pygame.mixer.Channel(1); ThrustChannel.set_volume(1.0*FXVOLUME)
    FireChannel.play(sFire,-1)
    ThrustChannel.play(sThrust,-1)
    FireChannel.pause()
    BulletHitChannels = [pygame.mixer.Channel(2),pygame.mixer.Channel(3),pygame.mixer.Channel(4),pygame.mixer.Channel(5),pygame.mixer.Channel(6)]
    MusicChannel = pygame.mixer.Channel(7)
    MusicChannel.play(sMusic,-1)
    for ch in BulletHitChannels:
        ch.set_volume(0.1*FXVOLUME)
    BulletHitSounds = [pygame.mixer.Sound("Data/Sound/Rico1.ogg"),
                       pygame.mixer.Sound("Data/Sound/Rico2.ogg"),
                       pygame.mixer.Sound("Data/Sound/Rico3.ogg"),
                       pygame.mixer.Sound("Data/Sound/Rico4.ogg"),
                       pygame.mixer.Sound("Data/Sound/Rico5.ogg")]

    player = Ship()
    player.pos = [2900,4100]

    Planet = PlanetVector(800)

    Stars1 = []
    for y in xrange(8):
        Row = []
        for x in xrange(8):
            StarBox = []
            for s in xrange(100):
                pos = [randint(0,1000),randint(0,1000)]
                pos = [pos[0]+(x*1000.0),pos[1]+(y*1000.0)]
                StarBox.append(Star(pos))
            Row.append(StarBox)
        Stars1.append(Row)
    Stars2 = []
    for y in xrange(4):
        Row = []
        for x in xrange(4):
            StarBox = []
            for s in xrange(100):
                pos = [randint(0,2000),randint(0,2000)]
                pos = [pos[0]+(x*2000.0),pos[1]+(y*2000.0)]
                StarBox.append(Star(pos))
            Row.append(StarBox)
        Stars2.append(Row)
    Stars3 = []
    for y in xrange(2):
        Row = []
        for x in xrange(2):
            StarBox = []
            for s in xrange(100):
                pos = [randint(0,4000),randint(0,4000)]
                pos = [pos[0]+(x*4000.0),pos[1]+(y*4000.0)]
                StarBox.append(Star(pos))
            Row.append(StarBox)
        Stars3.append(Row)
    Explosions = []
    Bullets = []
    Enemies = []
##    for x in xrange(25):
##        type = choice(["Transport","Micro Fighter","Medium Cruiser","Medium Fighter","Mini Gunship","Heavy Cruiser"])
##        Enemies.append(Enemy([random()*8000.0,random()*8000.0],type))
    for x in xrange(10):
        Enemies.append(Enemy(EdgePlace(),"Transport"))
    for x in xrange(50):
        Enemies.append(Enemy(EdgePlace(200),"Heavy Cruiser"))
    for x in xrange(10):
        Enemies.append(Enemy([random()*8000.0,random()*8000.0],"Medium Fighter"))
        Enemies.append(Enemy([random()*8000.0,random()*8000.0],"Mini Gunship"))
        Enemies.append(Enemy([random()*8000.0,random()*8000.0],"Medium Cruiser"))
    for angle in xrange(0,360,45):
        for angle2 in xrange(0,20,4):
            a = angle + angle2 - 8
            pos = [4000+rndint(Planet.size*cos(radians(a))),
                   4000+rndint(Planet.size*sin(radians(a)))]
            Enemies.append(Enemy(pos,"Turret",a))

    ExhaustL = exhaustsystem()
    ExhaustR = exhaustsystem()
    TurnerFL = turnexhaustsystem()
    TurnerFR = turnexhaustsystem()
    TurnerBL = turnexhaustsystem()
    TurnerBR = turnexhaustsystem()
    BulletImpacts = []
def EdgePlace(buffer=0):
    xy = choice(["x0","x8000","y0","y8000"])
    if xy == "x0": x = 0+buffer; y = randint(buffer,8000-buffer)
    if xy == "y0": y = 0+buffer; x = randint(buffer,8000-buffer)
    if xy == "x8000": x = 8000-buffer; y = randint(buffer,8000-buffer)
    if xy == "y8000": y = 8000-buffer; x = randint(buffer,8000-buffer)
    pos = [x,y]
    return pos
def GetInput():
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(); sys.exit()
    ThrustPlaying = 0.0
    if key[LEFTTURN]:
        if player.angularspeed < 3.75: player.angularspeed += 0.3
        TurnerFL.change_density(PSDDENSITY)
        TurnerBR.change_density(PSDDENSITY)
        ThrustPlaying += 0.5
    else:
        TurnerFL.change_density(0)
        TurnerBR.change_density(0)
    if key[RIGHTTURN]:
        if player.angularspeed > -3.75: player.angularspeed -= 0.3
        TurnerFR.change_density(PSDDENSITY)
        TurnerBL.change_density(PSDDENSITY)
        ThrustPlaying += 0.5
    else:
        TurnerFR.change_density(0)
        TurnerBL.change_density(0)
    if key[THRUST]:
        player.speed[0] += player.thrust*cos(radians(player.angle))
        player.speed[1] += player.thrust*sin(radians(player.angle))
        ExhaustL.change_density(PSDDENSITY)
        ExhaustR.change_density(PSDDENSITY)
        ThrustPlaying += 0.75
    else:
        ExhaustL.change_density(0)
        ExhaustR.change_density(0)
    ThrustChannel.set_volume(ThrustPlaying*FXVOLUME)
    if key[FIRE]:
        if player.firing == 0:
            player.firing = 3
            rpl = RotateAround((6, 8),player.angle)
            rpr = RotateAround((6,-8),player.angle)
            Bullets.append(Bullet((player.pos[0]+rpl[0],player.pos[1]+rpl[1]),player.angle,player.speed,"Self"))
            Bullets.append(Bullet((player.pos[0]+rpr[0],player.pos[1]+rpr[1]),player.angle,player.speed,"Self"))
            FireChannel.unpause()
    else:
        FireChannel.pause()
    if key[K_ESCAPE]:
        return "Return to Menu"
def Update():
    if len(Enemies) < 120:
        type = choice(["Transport","Micro Fighter","Medium Cruiser","Medium Fighter","Mini Gunship","Heavy Cruiser"])
        Enemies.append(Enemy(EdgePlace(),type))
    if player.beinghit > 0:
        player.beinghit -= 1
        player.color = (255,0,0)
    else:
        player.color = (255,255,255)
    ExhaustL.update()
    ExhaustR.update()
    TurnerFL.update()
    TurnerFR.update()
    TurnerBL.update()
    TurnerBR.update()
    for ps in BulletImpacts:
        ps.update()
    for e in Explosions:
        e.update()
    for b in Bullets:
        b.time += 1
        if b.time == 67:
            Bullets.remove(b); continue
    if player.firing > 0:
        player.firing -= 1
    for e in Enemies:
        if e.beinghit > 0:
            e.beinghit -= 1
            e.color = (255,0,0)
        else:
            e.color = (255,255,255)
        if e.waitvar > 0:   e.waitvar -= 1
        if e.launchvar > 0: e.launchvar -= 1
        #Gun AI
        if e.guns != None:
            for gun in e.guns:
                if CollideWith(gun.pos,player.pos,200):
                    if gun.firing == 0:
                        Bullets.append(Bullet(gun.pos,gun.angle,(0,0),"Enemy"))
                        gun.firing = 33
                    else:
                        gun.firing -= 1
def Move():
    #Player
    player.move()
    #   Gravity
    G = 0.005
    Me = pi*(Planet.size**2)
    Mo = 1.0
    XDiff = player.pos[0]-Planet.pos[0]
    YDiff = player.pos[1]-Planet.pos[1]
    r = sqrt(  (XDiff**2)  +  (YDiff**2)  )
    Force = G*(Me*Mo)/(r**2)
    Acceleration = Force / Mo
    player.speed[0] -= Acceleration*(XDiff/r)
    player.speed[1] -= Acceleration*(YDiff/r)
    #Bullets
    for b in Bullets:
        b.move()
    #Particle Systems
    rpl = RotateAround((-5, 4),-player.angle)
    rpr = RotateAround((-5,-4),-player.angle)
    ExhaustL.change_position((rpl[0]+(Screen[0]/2),Screen[1]-((Screen[1]/2)-rpl[1])))
    ExhaustR.change_position((rpr[0]+(Screen[0]/2),Screen[1]-((Screen[1]/2)-rpr[1])))
    ExhaustL.change_direction(-player.angle+180)
    ExhaustR.change_direction(-player.angle+180)
    
    rpfl = RotateAround((0,-14),-player.angle)
    rpfr = RotateAround((0, 14),-player.angle)
    rpbl = RotateAround((-4,-14),-player.angle)
    rpbr = RotateAround((-4, 14),-player.angle)
    TurnerFL.change_position((rpfl[0]+(Screen[0]/2),Screen[1]-((Screen[1]/2)-rpfl[1])))
    TurnerFR.change_position((rpfr[0]+(Screen[0]/2),Screen[1]-((Screen[1]/2)-rpfr[1])))
    TurnerBL.change_position((rpbl[0]+(Screen[0]/2),Screen[1]-((Screen[1]/2)-rpbl[1])))
    TurnerBR.change_position((rpbr[0]+(Screen[0]/2),Screen[1]-((Screen[1]/2)-rpbr[1])))
    TurnerFL.change_direction(-player.angle)
    TurnerFR.change_direction(-player.angle)
    TurnerBL.change_direction(-player.angle+180)
    TurnerBR.change_direction(-player.angle+180)

    for bi in BulletImpacts:
        point = WorldPoint(bi.pos)
        bi.ps.change_position((point[0],Screen[1]-point[1]))
    #Enemies
    for e in Enemies:
        e.pos = [e.pos[0]+e.speed[0],e.pos[1]+e.speed[1]]
        if e.guns != None:
            if e.onscreen:
                if e.type == "Turret":
                    for gun in e.guns:
                        XDiff = gun.pos[0] - player.pos[0]
                        YDiff = gun.pos[1] - player.pos[1]
                        gun.angle = degrees(atan2(YDiff,XDiff))+180.0
                else:
                    for gun in e.guns:
                        gun.pos = [e.pos[0],e.pos[1]]
                        point = RotateAround((gun.relpos[0],gun.relpos[1]),e.angle)
                        gun.pos = [gun.pos[0]+point[0],gun.pos[1]+point[1]]
                        XDiff = gun.pos[0] - player.pos[0]
                        YDiff = gun.pos[1] - player.pos[1]
                        gun.angle = degrees(atan2(YDiff,XDiff))+180.0
        #AI
        if e.type == "Transport":
            if e.hascargo == True:
                XDiff = e.pos[0] - 4000
                YDiff = e.pos[1] - 4000
                e.angle = degrees(atan2(YDiff,XDiff))+180.0
                e.speed = [e.maxspeed*cos(radians(e.angle)),e.maxspeed*sin(radians(e.angle))]
            elif e.hascargo == "Turning":
                if e.waitvar == 0: e.hascargo = "Unloading"; e.waitvar = 100
                else: e.angle += 1
            elif e.hascargo == "Unloading":
                if e.waitvar == 0: e.hascargo = False
            elif e.hascargo == False:
                e.speed = [e.maxspeed*cos(radians(e.angle)),e.maxspeed*sin(radians(e.angle))]
        elif e.type == "Heavy Cruiser":
            if e.waitvar > 0: e.angle += 0.1
            if e.waitvar == 0: e.speed = [e.maxspeed*cos(radians(e.angle)),e.maxspeed*sin(radians(e.angle))]
            if e.launchvar == 0:
                if CollideWith(player.pos,e.pos,300):
                    e.launchvar = 150
                    pos1 = RotateAround((-20,0),e.angle)
                    pos2 = RotateAround((-40,0),e.angle)
                    pos3 = RotateAround((-60,0),e.angle)
                    Enemies.append(Enemy([e.pos[0]+pos1[0],e.pos[1]+pos1[1]],"Micro Fighter",e.angle+90))
                    Enemies.append(Enemy([e.pos[0]+pos1[0],e.pos[1]+pos1[1]],"Micro Fighter",e.angle-90))
                    Enemies.append(Enemy([e.pos[0]+pos2[0],e.pos[1]+pos2[1]],"Micro Fighter",e.angle+90))
                    Enemies.append(Enemy([e.pos[0]+pos2[0],e.pos[1]+pos2[1]],"Micro Fighter",e.angle-90))
                    Enemies.append(Enemy([e.pos[0]+pos3[0],e.pos[1]+pos3[1]],"Micro Fighter",e.angle+90))
                    Enemies.append(Enemy([e.pos[0]+pos3[0],e.pos[1]+pos3[1]],"Micro Fighter",e.angle-90))
        elif e.type == "Micro Fighter":
            XDiff = e.pos[0] - player.pos[0]
            YDiff = e.pos[1] - player.pos[1]
            angle = degrees(atan2(YDiff,XDiff))+180
            e.angle = AngleMoveTowards(angle,e.angle,3)
            e.speed[0] += e.thrust*cos(radians(e.angle))
            e.speed[1] += e.thrust*sin(radians(e.angle))
            if e.speed[0] >  2.0: e.speed[0] =  2.0
            if e.speed[1] >  2.0: e.speed[1] =  2.0
            if e.speed[0] < -2.0: e.speed[0] = -2.0
            if e.speed[1] < -2.0: e.speed[1] = -2.0
            if e.waitvar == 0:
                if CollideWith(player.pos,e.pos,200):
                    e.waitvar = 20
                    Bullets.append(Bullet(e.pos,e.angle,e.speed,"Enemy"))
        elif e.type == "Medium Fighter":
            XDiff = e.pos[0] - player.pos[0]
            YDiff = e.pos[1] - player.pos[1]
            angle = degrees(atan2(YDiff,XDiff))+180
            e.angle = AngleMoveTowards(angle,e.angle,2)
            e.speed[0] += e.thrust*cos(radians(e.angle))
            e.speed[1] += e.thrust*sin(radians(e.angle))
            if e.speed[0] >  1.0: e.speed[0] =  1.0
            if e.speed[1] >  1.0: e.speed[1] =  1.0
            if e.speed[0] < -1.0: e.speed[0] = -1.0
            if e.speed[1] < -1.0: e.speed[1] = -1.0
            if e.waitvar == 0:
                if CollideWith(player.pos,e.pos,200):
                    e.waitvar = 5
                    Bullets.append(Bullet(e.pos,e.angle,e.speed,"Enemy"))
        elif e.type == "Medium Cruiser":
            XDiff = e.pos[0] - player.pos[0]
            YDiff = e.pos[1] - player.pos[1]
            angle = degrees(atan2(YDiff,XDiff))+180
            e.angle = AngleMoveTowards(angle,e.angle,3)
            e.speed[0] += e.thrust*cos(radians(e.angle))
            e.speed[1] += e.thrust*sin(radians(e.angle))
            if e.speed[0] >  1.0: e.speed[0] =  1.0
            if e.speed[1] >  1.0: e.speed[1] =  1.0
            if e.speed[0] < -1.0: e.speed[0] = -1.0
            if e.speed[1] < -1.0: e.speed[1] = -1.0
            if e.waitvar == 0:
                if CollideWith(player.pos,e.pos,200):
                    e.waitvar = 10
                    Bullets.append(Bullet(e.pos,e.angle,e.speed,"Enemy"))
        elif e.type == "Mini Gunship":
            XDiff = e.pos[0] - player.pos[0]
            YDiff = e.pos[1] - player.pos[1]
            angle = degrees(atan2(YDiff,XDiff))+180
            e.angle = AngleMoveTowards(angle,e.angle,2)
            e.speed[0] += e.thrust*cos(radians(e.angle))
            e.speed[1] += e.thrust*sin(radians(e.angle))
            if e.speed[0] >  0.5: e.speed[0] =  0.5
            if e.speed[1] >  0.5: e.speed[1] =  0.5
            if e.speed[0] < -0.5: e.speed[0] = -0.5
            if e.speed[1] < -0.5: e.speed[1] = -0.5
            if e.waitvar == 0:
                if CollideWith(player.pos,e.pos,200):
                    e.waitvar = 5
                    pos1 = RotateAround((-5,20),e.angle)
                    pos2 = RotateAround((0,15),e.angle)
                    pos3 = RotateAround((0,-15),e.angle)
                    pos4 = RotateAround((-5,-20),e.angle)
                    Bullets.append(Bullet([e.pos[0]+pos1[0],e.pos[1]+pos1[1]],e.angle,e.speed,"Enemy"))
                    Bullets.append(Bullet([e.pos[0]+pos2[0],e.pos[1]+pos2[1]],e.angle,e.speed,"Enemy"))
                    Bullets.append(Bullet([e.pos[0]+pos3[0],e.pos[1]+pos3[1]],e.angle,e.speed,"Enemy"))
                    Bullets.append(Bullet([e.pos[0]+pos4[0],e.pos[1]+pos4[1]],e.angle,e.speed,"Enemy"))
def CollideWith(p1,p2,radius):
    d2 = radius**2
    if ((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2) <= d2:
        return True
    return False
def CollisionDetect():
    if player.health <= 0:
        player.deadtime += 1
        if player.deadtime == 50:
            return "Return to Menu"
    if player.pos[0] <  400: player.pos[0] =  400; player.speed[0] = 0
    if player.pos[0] > 7599: player.pos[0] = 7599; player.speed[0] = 0
    if player.pos[1] <  400: player.pos[1] =  400; player.speed[1] = 0
    if player.pos[1] > 7599: player.pos[1] = 7599; player.speed[1] = 0
    if CollideWith(player.pos,Planet.pos,Planet.size+25):
        hit = False
        for p in player.points:
            p2 = RotateAround(p,player.angle)
            p2 = [p2[0]+player.pos[0],p2[1]+player.pos[1]]
            if CollideWith(p2,Planet.pos,Planet.size+1):
                player.speed = [0.0,0.0]
                player.health = 0
                if len(Explosions) == 0:
                    Explosions.append(Explosion( (Screen[0]/2,Screen[1]-(Screen[1]/2)) ))
                break
    for e in Explosions:
        if e.kill:
            Explosions.remove(e); continue
    for b in Bullets:
        if CollideWith(b.pos,Planet.pos,Planet.size+1):
            BulletImpacts.append(BulletImpact(b.pos))
            SoundNumber = choice([1,2,3,4,5])
            BulletHitChannels[SoundNumber-1].play(BulletHitSounds[SoundNumber-1])
            Bullets.remove(b)
    for e in Enemies:
        if e.stamina <= 0:
            point = WorldPoint(e.pos)
            Explosions.append(EnemyExplosion( (point[0],Screen[1]-point[1]) ))
            for x in xrange(e.boundradius):
                Bullets.append(Bullet(e.pos,randint(0,360),e.speed,"Shrapnel",random()*3.0))
            Enemies.remove(e); continue
    for e in Enemies:
        if e.onscreen:
            for b in Bullets:
                if b.owner != "Enemy":
                    if CollideWith(b.pos,e.pos,e.boundradius):
                        if EnemyHit(b.pos,e):
                            e.beinghit = 4
                            e.stamina -= 1
                            BulletImpacts.append(BulletImpact(b.pos))
                            SoundNumber = choice([1,2,3,4,5])
                            BulletHitChannels[SoundNumber-1].play(BulletHitSounds[SoundNumber-1])
                            try:Bullets.remove(b);continue
                            except:pass
    if player.health > 0:
        for b in Bullets:
            if b.owner != "Self":
                if SelfHit(b.pos,player):
                    player.health -= 1
                    player.beinghit = 4
                    BulletImpacts.append(BulletImpact(b.pos))
                    SoundNumber = choice([1,2,3,4,5])
                    BulletHitChannels[SoundNumber-1].play(BulletHitSounds[SoundNumber-1])
                    try:Bullets.remove(b);continue
                    except:pass
    for e in Enemies:
        if e.type == "Transport":
            if e.hascargo == True:
                if CollideWith(e.pos,Planet.pos,Planet.size+75):
                    e.hascargo = "Turning"
                    e.speed = [0,0]
                    e.waitvar = 90
        if e.type == "Heavy Cruiser":
            if e.waitvar == 0:
                if CollideWith(e.pos,Planet.pos,Planet.size+100):
                    e.waitvar = 1800
                    e.speed = [0,0]
    for e in Enemies:
        if e.pos[0] > 8000: Enemies.remove(e); continue
        if e.pos[0] <    0: Enemies.remove(e); continue
        if e.pos[1] > 8000: Enemies.remove(e); continue
        if e.pos[1] <    0: Enemies.remove(e); continue
        if e.type != "Turret":
            if CollideWith(e.pos,Planet.pos,Planet.size+e.boundradius): Enemies.remove(e); continue
def OnScreen(point,buffer=0):
    worldpoint = WorldPoint(point)
    if worldpoint[0] > 0-buffer:
        if worldpoint[1] > 0-buffer:
            if worldpoint[0] < Screen[0]+buffer:
                if worldpoint[1] < Screen[1]+buffer:
                    return True
    return False
def WorldPoint(point):
    DiffPoint = [CameraPosition[0]-point[0],CameraPosition[1]-point[1]]
    RelPoint  = [(Screen[0]/2)-DiffPoint[0],(Screen[1]/2)-DiffPoint[1]]
    FlipPoint = [RelPoint[0],RelPoint[1]]
    RndPoint  = [rndint(FlipPoint[0]),rndint(FlipPoint[1])]
    return RndPoint
CameraPosition = [0,0]
def IndexGet(num,denom,len):
    counter = 0
    list = []
    for x in xrange(len):
        counter += 1
        if counter <= num:
            list.append(x)
        if counter == denom:
            counter = 0
    return list
def Draw():
    global CameraPosition
    CameraPosition = [player.pos[0],player.pos[1]]
    #Clear
    Surface.fill((0,0,0))
    #Stars
    #   Stars1
    BottomLeft = (  CameraPosition[0]-(Screen[0]/2.0),  CameraPosition[1]-(Screen[1]/2.0)  )
    TopRight   = (  CameraPosition[0]+(Screen[0]/2.0),  CameraPosition[1]+(Screen[1]/2.0)  )
    BottomLeftList = [ rndint(BottomLeft[0])/1000, rndint(BottomLeft[1])/1000 ]
    TopRightList   = [ rndint(TopRight[0])/1000,   rndint(TopRight[1])/1000   ]
    y = BottomLeftList[1]
    while y <= TopRightList[1]:
        x = BottomLeftList[0]
        while x <= TopRightList[0]:
            StarBox = Stars1[y][x]
            for s in StarBox:
                point = WorldPoint(s.pos)
                point = (point[0],Screen[1]-point[1])
                Surface.set_at( point, (150,150,150) )
            x += 1
        y += 1
    #   Stars2
    for row in Stars2:
        for StarBox in row:
            for s in StarBox:
                point = WorldPoint(s.pos)
                point = (point[0]/2,(Screen[1]-point[1])/2)
                Surface.set_at( point, (100,100,100) )
    #   Stars3
    for row in Stars3:
        for StarBox in row:
            for s in StarBox:
                point = WorldPoint(s.pos)
                point = (point[0]/4,(Screen[1]-point[1])/4)
                Surface.set_at( point, (50,50,50) )
    #Player
    if player.health > 0:
        RotatedPoints = []
        for point in player.points:
            rp = RotateAround(point,-player.angle)
            RotatedPoints.append(WorldPoint([rp[0]+player.pos[0],rp[1]+player.pos[1]]))
        pygame.draw.aalines(Surface, player.color, True, RotatedPoints)
    #Enemies
    for e in Enemies:
        if OnScreen(e.pos,100):
            e.onscreen = True
            RotatedPoints = []
            for point in e.points:
                rp = RotateAround(point,-e.angle)
                Point = WorldPoint(e.pos)
                RotatedPoints.append((Point[0]+rp[0],Screen[1]-Point[1]+rp[1]))
            pygame.draw.aalines(Surface, e.color, True, RotatedPoints)
            if e.guns != None:
                for gun in e.guns:
                    RotatedPoints = []
                    for point in gun.points:
                        rp = RotateAround(point,-gun.angle)
                        Point = WorldPoint(gun.pos)
                        RotatedPoints.append((Point[0]+rp[0],Screen[1]-Point[1]+rp[1]))
                    pygame.draw.aalines(Surface, e.color, True, RotatedPoints)
        else:
            e.onscreen = False
    #Bullets
    for b in Bullets:
        Point = WorldPoint(b.pos)
        Surface.set_at((Point[0],Screen[1]-Point[1]),(255,255,255))
    #Particle Systems
    #   Exhaust
    ExhaustL.draw(Surface)
    ExhaustR.draw(Surface)
    TurnerFL.draw(Surface)
    TurnerFR.draw(Surface)
    TurnerBL.draw(Surface)
    TurnerBR.draw(Surface)
    #   Explosions
    for e in Explosions:
        e.draw(Surface)
    #   Impacts
    for ps in BulletImpacts:
        ps.draw(Surface)
    #Shadow
    if LIGHT:
        Occluders = []
        if BULLETOCCLUDE:
            for b in Bullets:
                point = WorldPoint(b.pos)
                Occluders.append(pygame.Rect((point[0],Screen[1]-point[1]),(1,1)))
        if THRUSTOCCLUDE > 0:
            for ps in [ExhaustL.particles,ExhaustR.particles]:
                particlelist = IndexGet(THRUSTOCCLUDE,PSDDENSITY,len(ps))
                for index in particlelist:
                    p = ps[index]
                    pos = (p[0][0],p[0][1]); Occluders.append(pygame.Rect(pos,(1,1)))
        if TURNOCCLUDE > 0:
            for ps in [TurnerFL.particles,TurnerFR.particles,TurnerBL.particles,TurnerBR.particles]:
                particlelist = IndexGet(TURNOCCLUDE,PSDDENSITY,len(ps))
                for index in particlelist:
                    p = ps[index]
                    pos = (p[0][0],p[0][1]); Occluders.append(pygame.Rect(pos,(1,1)))
        if EXPLODEOCCLUDE > 0:
            for e in Explosions:
                particlelist = IndexGet(EXPLODEOCCLUDE,PSDDENSITY,len(e.ps.particles))
                for index in particlelist:
                    p = e.ps.particles[index]
                    pos = (p[0][0],p[0][1]); Occluders.append(pygame.Rect(pos,(1,1)))
            for bi in BulletImpacts:
                particlelist = IndexGet(EXPLODEOCCLUDE,PSDDENSITY,len(bi.ps.particles))
                for index in particlelist:
                    p = bi.ps.particles[index]
                    pos = (p[0][0],p[0][1]); Occluders.append(pygame.Rect(pos,(1,1)))
        s1 = shadow((Screen[0]/2,Screen[1]/2),Occluders)
        s1.draw(Surface)
    #Planet Vector
    Point = WorldPoint(Planet.pos)
    pygame.draw.circle(Surface,(0,0,0),(Point[0],Screen[1]-Point[1]),Planet.size)
    pygame.draw.circle(Surface,(0,255,0),(Point[0],Screen[1]-Point[1]),Planet.size,1)
    #HUD
    Display = pygame.Surface((150,150))
    Display.set_alpha(128)
    SelfPos = (  rndint((player.pos[0]/8000.0)*150.0),  rndint(150-((player.pos[1]/8000.0))*150.0)  )
    Display.set_at(SelfPos,(255,255,255))
    pygame.draw.circle(Display,(0,255,0),(75,75),rndint((Planet.size*150.0)/8000.0),1)
    for e in Enemies:
        Point = (  rndint((e.pos[0]/8000.0)*150.0),  rndint(150-((e.pos[1]/8000.0))*150.0)  )
        Display.set_at(Point,(255,0,255))
    Surface.blit(Display,(15,15))
    RoundedRect(Surface,(255,255,255),(15,15,150,150),7,1)
    #   Health Meter
    if player.health > 0:
        width = rndint(200.0*(player.health/100.0))
        color = (  rndint(((100-player.health)/100.0)*255.0),  rndint((player.health/100.0)*255.0),  0  )
        BarSurface = pygame.Surface((200,20))
        BarSurface.set_alpha(128)
        BarSurface.set_colorkey((0,0,0))
        RoundedRect(BarSurface,color,(-200+width,0,200,20),7)
        RoundedRect(BarSurface,(255,255,255),(0,1,200,18),7,1)
        RoundedRect(BarSurface,(255,255,255),(1,1,198,18),7,1)
        RoundedRect(BarSurface,(0,0,0),(-3,-3,206,26),7,4)
        Surface.blit(BarSurface,(Screen[0]-(200+15+2),15))

    RoundedRect(Surface,(255,255,255),(Screen[0]-(200+15+2),15,200,20),7,1)
    EHI = Font.render("Estimated Hull Integrity",True,(255,255,255))
    Surface.blit(EHI,(Screen[0]-(100+15)-(EHI.get_width()/2),16))
    #   RADAR
    radarsurface = pygame.Surface((100,100))
    radarsurface.set_colorkey((0,0,0))
    radarsurface.set_alpha(128)
    pygame.draw.circle(radarsurface,(128,128,128),(50,50),50)
    center = (Screen[0]-15-100,15+20+15+50)
    for e in Enemies:
        if e.onscreen:
            XDiff = e.pos[0] - player.pos[0]
            YDiff = e.pos[1] - player.pos[1]
            angle = atan2(YDiff,XDiff)
            if e.type == "Transport": color = (255,128,0)
            elif e.type == "Turret": color = (0,255,0)
            else: color = (255,0,0)
            pygame.draw.aaline(radarsurface,color,(50,50),(50+rndint(50.0*cos(angle)),50-rndint(50.0*sin(angle))))
    Surface.blit(radarsurface,(Screen[0]-15-100-50,15+20+15))
    pygame.draw.circle(Surface,(255,255,255),center,50,1)
    pygame.draw.circle(Surface,(255,255,255),center,2,1)
    #FPS
    fps = Font.render(str(rndint(Clock.get_fps()))+" Frames/Second",True,(255,255,255))
    Surface.blit(fps,(10,Screen[1]-(fps.get_height()+10)))
    #Flip
    pygame.display.flip()
def main():
    global LEFTTURN,RIGHTTURN,THRUST,FIRE,PSDDENSITY,LIGHT,THRUSTOCCLUDE,TURNOCCLUDE,EXPLODEOCCLUDE,BULLETOCCLUDE,MUSICVOLUME,FXVOLUME
    while True:
        LEFTTURN,RIGHTTURN,THRUST,FIRE,PSDDENSITY,LIGHT,THRUSTOCCLUDE,TURNOCCLUDE,EXPLODEOCCLUDE,BULLETOCCLUDE,MUSICVOLUME,FXVOLUME = Menu.main()
        Init()
        while True:
            ToDo = GetInput()
            if ToDo == "Return to Menu":break
            Update()
            Move()
            ToDo = CollisionDetect()
            if ToDo == "Return to Menu":break
            Draw()
            Clock.tick(40)
        MusicChannel.stop()
if __name__ == '__main__': main()
