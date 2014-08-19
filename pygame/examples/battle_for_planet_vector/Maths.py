from math import *
def rndint(num):
    return int(round(num))
def RotateAround(point,angle):
    x = cos(radians(angle))*point[0] - sin(radians(angle))*point[1]
    y = sin(radians(angle))*point[0] + cos(radians(angle))*point[1]
    return [x,y]
def AngleMoveTowards(angle1,angle2,turnspeed):
    angle1 = angle1%360
    tmpeangle = angle2
    tmpeangle -= angle1
    tmpeangle = tmpeangle%360
    if tmpeangle < 180:
        angle2 -= turnspeed
    else:
        angle2 += turnspeed
    return angle2
def EnemyHit(point,enemy):
    Hit=False
    if enemy.type == "Micro Fighter":
        if PolyCollide( point, ((10,0),(-10,5),(-10,-5)), enemy.pos, -enemy.angle ): Hit = True
    elif enemy.type == "Transport":
        if   PolyCollide( point, ((65,0),(50,15),(50,-15)), enemy.pos, -enemy.angle ):               Hit = True
        elif PolyCollide( point, ((50,3),(-50,3),(-50,-3),(50,-3)), enemy.pos, -enemy.angle ):       Hit = True
        elif PolyCollide( point, ((-55,-15),(-50,-15),(-50,15),(-55,15)), enemy.pos, -enemy.angle ): Hit = True
    elif enemy.type == "Medium Cruiser":
        if   PolyCollide( point, ((-2,40),(4,20),(8,20)), enemy.pos, -enemy.angle ):                                   Hit = True
        elif PolyCollide( point, ((8,-20),(4,-20),(-2,-40)), enemy.pos, -enemy.angle ):                                Hit = True
        elif PolyCollide( point, ((-25,-10),(0,-15),(0,15),(-25,10)), enemy.pos, -enemy.angle ):                       Hit = True
        elif PolyCollide( point, ((10,-13),(25,-10),(33,-7),(35,0),(33,7),(25,10),(10,13)), enemy.pos, -enemy.angle ): Hit = True
    elif enemy.type == "Medium Fighter":
        if   PolyCollide( point, ((10,0),(-3,5),(-3,-5)), enemy.pos, -enemy.angle ):             Hit = True
        elif PolyCollide( point, ((-3,-5),(-10,-20),(-2,-15),(1,-5)), enemy.pos, -enemy.angle ): Hit = True
        elif PolyCollide( point, ((1,5),(-2,15),(-10,20),(-3,5)), enemy.pos, -enemy.angle ):     Hit = True
    elif enemy.type == "Mini Gunship":
        if   PolyCollide( point, ((-3,-15),(2,-2),(2,2),(-3,15)), enemy.pos, -enemy.angle ):                  Hit = True
        elif PolyCollide( point, ((-10,-2),(2,-2),(15,0),(2,2),(-10,2)), enemy.pos, -enemy.angle ):           Hit = True
        elif PolyCollide( point, ((-6,-2),(-8,-20),(-2,-2),(-2,2),(-8,20),(-6,2)), enemy.pos, -enemy.angle ): Hit = True
    elif enemy.type == "Turret":
        if PolyCollide( point, ((0,-10),(10,-8),(10,8),(0,10)), enemy.pos, enemy.angle ): Hit = True
    elif enemy.type == "Heavy Cruiser":
        if   PolyCollide( point, ((-77,-13),(-20,-13),(-20,13),(-77,13)), enemy.pos, enemy.angle ):                Hit = True
        elif PolyCollide( point, ((-100,-7),(-80,-2),(-80,2),(-100,7)), enemy.pos, enemy.angle ):                  Hit = True
        elif PolyCollide( point, ((40,-13),(50,-13),(50,13),(40,13)), enemy.pos, enemy.angle ):                    Hit = True
        elif PolyCollide( point, ((50,-10),(95,-5),(100,0),(95,5),(50,10)), enemy.pos, enemy.angle ):              Hit = True
        elif PolyCollide( point, ((-20,-10),(35,-20),(40,-13),(40,13),(35,20),(-20,10)), enemy.pos, enemy.angle ): Hit = True
    return Hit
def SelfHit(point,player):
    Hit=False
    if   PolyCollide( point, ((14,0),(-6,6),(-6,-6)), player.pos, -player.angle ):   Hit = True #Central Triangle
    elif PolyCollide( point, ((7,-7),(-9,-25),(-2,-8)), player.pos, -player.angle ): Hit = True #Left Wing
    elif PolyCollide( point, ((7,7),(-9,25),(-2,8)), player.pos, -player.angle ):    Hit = True #Right Wing
    if Hit:return True
    return False
def PolyCollide(point,unrotatedpolygon,polytranslate,angle):
    polygon = []
    for p in unrotatedpolygon:
        p2 = RotateAround(p,angle)
        p2 = [p2[0]+polytranslate[0],p2[1]+polytranslate[1]]
        polygon.append(p2)
    x = point[0]
    y = point[1]
    Lines = []
    index = 0
    for index in xrange(len(polygon)):
        p0 = polygon[index]
        try: p1 = polygon[index+1]
        except: p1 = polygon[0]
        Lines.append([p0,p1])
    for l in Lines:
        p0 = l[0]
        p1 = l[1]
        x0 = p0[0]; y0 = p0[1]
        x1 = p1[0]; y1 = p1[1]
        test = (y - y0)*(x1 - x0) - (x - x0)*(y1 - y0)
        if test < 0: return False
    return True
