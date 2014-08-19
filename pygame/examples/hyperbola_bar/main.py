from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import sys, os, traceback
if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"
from math import *
pygame.display.init()
pygame.font.init()

#GRAPHICS OPTIONS
screen_size = [800,600]
multisample = 16

#SIMULATION OPTIONS
bar_elev = 0.0
bar_len = 0.5
through_angle = 60.0
length2 = 2.5 #2*length of bar

icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("Hyperbola Bar - Ian Mallett - v.1.0.0 - 2014")
if multisample:
    pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS,1)
    pygame.display.gl_set_attribute(GL_MULTISAMPLESAMPLES,multisample)
pygame.display.set_mode(screen_size,OPENGL|DOUBLEBUF)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)

##glEnable(GL_TEXTURE_2D)
glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
glTexEnvi(GL_POINT_SPRITE,GL_COORD_REPLACE,GL_TRUE)

glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)
glEnable(GL_DEPTH_TEST)

glPointSize(10.0)

def init():
    global dl_hyp
    pts = [get_pt(float(i)/float(100-1)) for i in range(100)]
    dl_hyp = glGenLists(1)
    glNewList(dl_hyp,GL_COMPILE)
    glBegin(GL_LINE_STRIP)
    for i in range(100):
        glVertex3f(*pts[i])
    glEnd()
    glEndList()

camera_rot = [70.0,30.0]
camera_radius = 8.0
camera_center = [0.0,0.0,0.0]
paused = False
def get_input():
    global camera_rot,camera_radius, paused
    keys_pressed = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos()
    mouse_rel = pygame.mouse.get_rel()
    for event in pygame.event.get():
        if   event.type == QUIT: return False
        elif event.type == KEYDOWN:
            if   event.key == K_ESCAPE: return False
            elif event.key == K_p:
                paused = not paused
        elif event.type == MOUSEBUTTONDOWN:
            if   event.button == 4: camera_radius *= 0.9
            elif event.button == 5: camera_radius /= 0.9
    if mouse_buttons[0]:
        camera_rot[0] += mouse_rel[0]
        camera_rot[1] += mouse_rel[1]
    return True
t = 0.0
def update():
    if paused: return
    global t
    t += 0.005
    if t>=1.0: t-=1.0
def trans_pt(t,pt):
    glPushMatrix()
    glLoadIdentity()
    
    glRotatef(through_angle*sin(2.0*pi*t), 0.0,1.0,0.0)
    glTranslatef(bar_len,bar_elev,0.0)
    glRotatef(20.0, 1.0,0.0,0.0)
    
    matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    
    glPopMatrix()
    return [
        matrix[0][0]*pt[0] + matrix[1][0]*pt[1] + matrix[2][0]*pt[2] + matrix[3][0]*1.0,
        matrix[0][1]*pt[0] + matrix[1][1]*pt[1] + matrix[2][1]*pt[2] + matrix[3][1]*1.0,
        matrix[0][2]*pt[0] + matrix[1][2]*pt[1] + matrix[2][2]*pt[2] + matrix[3][2]*1.0
    ]
def get_pt(t):
    p0 = trans_pt(t,[0.0,-length2,0.0])
    p1 = trans_pt(t,[0.0, length2,0.0])
    v = [p1[0]-p0[0],p1[1]-p0[1],p1[2]-p0[2]]
    l = (v[0]*v[0]+v[1]*v[1]+v[2]*v[2])**0.5
    v = [v[0]/l,v[1]/l,v[2]/l]
    #p0[2]+s*v[2] = 0.0
    s = -p0[2]/v[2]
    intersect = [p0[i]+s*v[i] for i in [0,1,2]]
    return intersect
def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glViewport(0,0,screen_size[0],screen_size[1])
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(screen_size[0])/float(screen_size[1]), 0.1,100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    camera_pos = [
        camera_center[0] + camera_radius*cos(radians(camera_rot[0]))*cos(radians(camera_rot[1])),
        camera_center[1] + camera_radius                            *sin(radians(camera_rot[1])),
        camera_center[2] + camera_radius*sin(radians(camera_rot[0]))*cos(radians(camera_rot[1]))
    ]
    gluLookAt(
        camera_pos[0],camera_pos[1],camera_pos[2],
        camera_center[0],camera_center[1],camera_center[2],
        0,1,0
    )

    glBegin(GL_LINES)
    glColor3f(1,0,0); glVertex3f(0,0,0);glVertex3f(1,0,0)
    glColor3f(0,1,0); glVertex3f(0,0,0);glVertex3f(0,1,0)
    glColor3f(0,0,1); glVertex3f(0,0,0);glVertex3f(0,0,1)
    glColor3f(1,1,1)
    glEnd()

    glPushMatrix()
    glRotatef(through_angle*sin(2.0*pi*t), 0.0,1.0,0.0)
    
    glBegin(GL_LINES)
    glColor3f(0.5,0.5,0.5)
    glVertex3f(0.0,bar_elev,0.0)
    glVertex3f(bar_len,bar_elev,0.0)
    glEnd()

    glTranslatef(bar_len,bar_elev,0.0)
    glRotatef(20.0, 1.0,0.0,0.0)
    glBegin(GL_LINES)
    glColor3f(0.5,0.5,0.5)
    glVertex3f(0.0,-length2,0.0)
    glVertex3f(0.0, length2,0.0)
    glEnd()
    
    glPopMatrix()
    
    glColor3f(1,1,0)

    glCallList(dl_hyp)

    pt = get_pt(t)
    glBegin(GL_POINTS)
    glVertex3f(*pt)
    glEnd()
    
##    glColor4f(1,1,1,0.5)
##    glBegin(GL_QUADS)
##    glVertex3f(0,0,0)
##    glVertex3f(1,0,0)
##    glVertex3f(1,1,0)
##    glVertex3f(0,1,0)
##    glEnd()
    glColor4f(1,1,1,1)
    
    pygame.display.flip()
def main():
    init()
    clock = pygame.time.Clock()
    while True:
        if not get_input(): break
        update()
        draw()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        pygame.quit()
        input()
