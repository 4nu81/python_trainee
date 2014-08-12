import math
import random

random.seed()

def collide(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    d = math.hypot(dx, dy)
    if d < (p1.size + p2.size):
        total_mass = p1.mass + p2.mass
        tangent = math.atan2(dy, dx) - 0.5 * math.pi

        (p1.angle, p1.speed) = addVectors(
            (p1.angle, p1.speed * (p1.mass - p2.mass) / total_mass),
            (tangent, 2 * p2.speed * p2.mass / total_mass))
        (p2.angle, p2.speed) = addVectors(
            (p2.angle, p2.speed * (p2.mass - p1.mass) / total_mass),
            (tangent + math.pi, 2 * p1.speed * p1.mass / total_mass))

        elasticity = p1.elasticity * p2.elasticity
        p1.speed *= elasticity
        p2.speed *= elasticity

        angle = 0.5 * math.pi + tangent
        overlap = (p1.size + p2.size - d )
        p1.x -= math.sin(angle) * overlap
        p1.y += math.cos(angle) * overlap
        p2.x += math.sin(angle) * overlap
        p2.y -= math.cos(angle) * overlap

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
    def __init__(self, (width, height)):
        self.width = width
        self.height = height
        self.particles = []
        self.color = (255,255,255)
        self.mass_of_air = 0.2
        self.elasticity = 0.75
        self.gravity = (math.pi, 0.001)

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

    def findParticle(self, (x, y)):
        for p in self.particles:
            if math.hypot(x - p.x, y - p.y) <= p.size:
                return p
        return None

    def addParticles(self, n=1, **kargs):
        for i in range(n):
            size = kargs.get('size', random.randint(10,20))
            mass = kargs.get('mass', random.randint(100,10000))
            x = kargs.get('x', random.uniform(size, self.width - size))
            y = kargs.get('y', random.uniform(size, self.height - size))

            p = Particle((x,y), size, mass)

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
        if p.x > self.width - p.size:
            p.angle = - p.angle
            p.speed *= self.elasticity
            p.x = self.width - p.size
        elif p.x - p.size < 0:
            p.angle = - p.angle
            p.speed *= self.elasticity
            p.x = 0 + p.size

        if p.y > self.height - p.size:
            p.angle = math.pi - p.angle
            p.speed *= self.elasticity
            p.y = self.height - p.size
        elif p.y - p.size < 0:
            p.angle = math.pi - p.angle
            p.speed *= self.elasticity
            p.y = 0 + p.size

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

    def attract(self, other):
        dx = (self.x - other.x)
        dy = (self.y - other.y)
        dist = math.hypot(dx, dy)

        theta = math.atan2(dy, dx)
        force = 0.2 * self.mass * other.mass / dist**2
        self.accelerate((theta - 0.5 * math.pi, force/self.mass))
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
