import math
import random

random.seed()

def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        tangent = math.atan2(dy, dx) + 0.5 * math.pi

        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors(
            (p1.angle, p1.speed * (p1.mass - p2.mass) / total_mass),
            (tangent, 2 * p2.speed * p2.mass / total_mass),
        )

        (p2.angle, p2.speed) = addVectors(
            (p2.angle, p2.speed * (p2.mass - p1.mass) / total_mass),
            (tangent + math.pi, 2 * p1.speed * p1.mass / total_mass),
        )

        elasticity = p1.elasticity * p2.elasticity
        p1.speed *= elasticity
        p2.speed *= elasticity

        # Ueberlappen verhindern
        overlap = (p1.size + p2.size - dist)
        dx = math.sin(tangent) * overlap
        dy = math.cos(tangent) * overlap

        p1.x += dx
        p1.y -= dy
        p2.x -= dx
        p2.y += dy

def combine(p1,p2):
    d = math.hypot(p1.x-p2.x, p1.y-p2.y)
    collision_d = p1.size + p2.size
    if d < collision_d:
        total_mass = p1.mass + p2.mass
        p1.x = (p1.x*p1.mass + p2.x*p2.mass) / total_mass
        p1.y = (p1.y*p1.mass + p2.y*p2.mass) / total_mass
        (p1.angle, p1.speed) = addVectors(
            (p1.angle, p1.speed*p1.mass/total_mass),
            (p2.angle, p2.speed*p2.mass/total_mass),
        )
        p1.speed *= (p1.elasticity*p2.elasticity)
        p1.mass += p2.mass
        p1.collide_with = p2

def addVectors((a1, l1),(a2, l2)):
    x = math.sin(a1) * l1 + math.sin(a2) * l2
    y = math.cos(a1) * l1 + math.cos(a2) * l2

    length = math.hypot(x, y)
    angle = (0.5 * math.pi - math.atan2(y, x))
    return angle, length


## Environment ##
class Environment:
    def __init__(self, (width, height), **kargs):
        self.width = width
        self.height = height
        self.particles = []
        self.color = (255,255,255)
        self.mass_of_air = 0.2
        self.elasticity = 0.75
        self.gravity = (math.pi, 0.001)
        self.bounds = kargs.get('bounds', ((0,0),(width,height)))
        self.holes = kargs.get('holes', [])

        self.particle_functions1 = []
        self.particle_functions2 = []
        self.function_dict = {
            'move': (1, lambda p: p.move()),
            'drag': (1, lambda p: p.getdraged()),
            'bounce': (1, lambda p: self.bounce(p)),
            'accelerate': (1, lambda p: p.accelerate(self.gravity)),
            'outofbounds': (1, lambda p: self.outofbounds(p)),
            'collide': (2, lambda p1, p2: collide(p1,p2)),
            'attract': (2, lambda p1, p2: p1.attract(p2)),
            'combine': (2, lambda p1, p2: combine(p1,p2)),
        }

    def addFunctions(self, function_list):
        for func in function_list:
            n, f = self.function_dict.get(func, (-1,None))
            if n == 1:
                self.particle_functions1.append(f)
            elif n == 2:
                self.particle_functions2.append(f)
            else:
                print "No such function: {f}".format(f=f)

    def inHole(self, particle):
        for (x,y,s) in self.holes:
            if particle.x1 > x - s and particle.x1 < x + s:
                pass

    def findParticle(self, (x, y)):
        for p in self.particles:
            if math.hypot(x - p.x, y - p.y) <= p.size:
                return p
        return None

    def addParticles(self, n=1, **kargs):
        for i in range(n):
            size = kargs.get('size', random.randint(10,20))
            mass = kargs.get('mass', random.randint(100,10000))

            ((bound_x0,bound_y0),(bound_x1,bound_y1)) = self.bounds
            x = float(kargs.get('x', random.uniform(bound_x0 + size, bound_x1 - size)))
            y = float(kargs.get('y', random.uniform(bound_y0 + size, bound_y1 - size)))

            p = Particle((x,y), size, mass)

            p.name = kargs.get('name', '')
            p.textcolor = kargs.get('textcolor', (255,255,255))
            p.angle = kargs.get('angle', random.uniform(0, 2*math.pi))
            p.speed = kargs.get('speed', random.random())
            p.color = kargs.get('color', (0,0,255))
            p.drag = (p.mass / (p.mass + self.mass_of_air)) ** p.size

            self.particles.append(p)

    def update(self):
        for i,particle in enumerate(self.particles):
            for f in self.particle_functions1:
                f(particle)
            for particle2 in self.particles[i+1:]:
                for f in self.particle_functions2:
                    f(particle, particle2)

    def bounce(self, p):
        ((bound_x0,bound_y0),(bound_x1,bound_y1)) = self.bounds
        if p.x > bound_x1 - p.size:
            p.angle = - p.angle
            p.speed *= self.elasticity
            p.x = bound_x1 - p.size
        elif p.x - p.size < bound_x0:
            p.angle = - p.angle
            p.speed *= self.elasticity
            p.x = bound_x0 + p.size

        if p.y > bound_y1 - p.size:
            p.angle = math.pi - p.angle
            p.speed *= self.elasticity
            p.y = bound_y1 - p.size
        elif p.y - p.size < bound_y0:
            p.angle = math.pi - p.angle
            p.speed *= self.elasticity
            p.y = bound_y0 + p.size

    def outofbounds(self, p):
        if p.x > 2 * self.width or p.x < -self.width or p.y > 2 * self.height or p.y < -self.height:
            p.toremove = True

## Particles ##
class Particle():
    def __init__(self, (x, y), size, mass=1):
        self.size = size
        self.x = x
        self.y = y
        self.color = (0,0,255)
        self.mass = mass
        self.thickness = 2
        self.elasticity = 0.9

    def attract(self, other, update=True):
        dx = (self.x - other.x)
        dy = (self.y - other.y)
        dist = math.hypot(dx, dy)

        theta = math.atan2(dy, dx)
        force = 0.2 * self.mass * other.mass / dist**2
        self.accelerate((theta - 0.5 * math.pi, force/self.mass))
        if update:
            other.accelerate((theta + 0.5 * math.pi, force/other.mass))

    def mouseMove(self, (x, y)):
        dx = x - self.x
        dy = y - self.y
        self.angle = 0.5 * math.pi + math.atan2(dy, dx)
        self.speed = math.hypot(dx, dy) * 0.1

    def getdraged(self):
        self.speed *= self.drag

    def accelerate(self, vector):
        self.angle, self.speed = addVectors((self.angle, self.speed), vector)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
