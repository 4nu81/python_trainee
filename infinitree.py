# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Tree:
    def __init__(self):
        self.light_spin = 0
        self.cube_spin = 0
        self.cube_rate = 0
        self.cube_y = 0
        self.light_y = 1
        self.light_x = 0
        self.root_grow = 0.001
        self.root_rate = 0.001

    def glinit(self):
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHTING)
        glEnable(GL_DEPTH_TEST)
        glColorMaterial(GL_FRONT, GL_AMBIENT)
        glEnable(GL_COLOR_MATERIAL)
        #glMaterialfv(GL_FRONT, GL_SHININESS, 128.0) ##range:0-128
        glMaterialfv(GL_FRONT, GL_SPECULAR, (0.0, 0.5, 1.0, 1.0))	##set material properties
        glClearColor(0.0, 0.0, 0.0, 0.0)

    def lighting(self):
        glPushMatrix()
        glRotatef(-self.light_spin, 1, 0, 0)
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (1.0, -1.0, -1.0, 1.0)) ##direction its aiming
        glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 1.0)
        glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 3.0)

        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.0, 1.0, 1.0))
        glLightfv(GL_LIGHT0, GL_POSITION, (-1.0, 1.0 ,1.0,0.0)) ##location of light source
        glEnable(GL_LIGHT0)
        glPopMatrix()

        glPushMatrix()
        glLightfv(GL_LIGHT1, GL_DIFFUSE, (1.0, 1.0, 1.0, 0.0))
        glLightfv(GL_LIGHT1, GL_POSITION, (2.0, 1.0 ,1,0.0)) ## location of light source
        glEnable(GL_LIGHT1)
        glPopMatrix()

    def display(self):
        glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	##include depth buffer
        glMatrixMode (GL_PROJECTION)
        glLoadIdentity()
        gluPerspective (50.0, 1.0, 1.5, 80.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()
    
        gluLookAt(0,0.0,self.root_grow + 10, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        World.lighting()
        
        glRotatef(self.cube_spin, 0, self.cube_y, 0)
        
        glPushMatrix()
        glColor3f(0.0, 0.0, 3.25)
        glutWireCube(6)
        glPopMatrix()
        
        glTranslatef(0, -2, 0)
        World.drawbranch(self.root_grow,0.1)

        glutSwapBuffers()
    
    def drawbranch(self,grow,age):
        glPushMatrix()
        glColor3f(0, 2, 0)
        glRotatef(90, 0, 1, 0)
        glBegin(GL_LINES)
        glVertex3d(0, 0, 0)
        glVertex3d(0, grow, 0)
        glEnd()
        glTranslatef(0, grow, 0)
    
        if grow > age:
            glRotatef(30, 1, 0, 0)
            World.drawbranch(grow-age,age)
            glRotatef(-60, 1, 0, 0)
            World.drawbranch(grow-age,age)
        glPopMatrix()

    def animate(self):
        self.light_spin = self.light_spin + 1
        if self.light_spin > 360:
            self.light_spin = 0
        self.root_grow = self.root_grow + self.root_rate
        self.cube_spin = self.cube_spin + self.cube_rate
        glutPostRedisplay()

    def reshape(self, w, h):
        glViewport(0, 0, w, h)
        glutPostRedisplay();

    def mouse(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN: 
                glutIdleFunc(World.animate)
                glutPostRedisplay()
	
        if button ==  GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN: 
                if (self.cube_rate == 1):
                    self.cube_rate = 0
                    self.cube_spin = 0
                    self.cube_y = 0
                    self.light_y = 1
                    self.light_x =0
                else:
                    self.cube_y = 1
                    self.cube_rate = 1
                    self.light_y = 0
                    self.light_x =1

World = Tree()
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(450,400)
glutInitWindowPosition(100, 100)
glutCreateWindow('Tree')
World.glinit()
glutDisplayFunc(World.display)
glutReshapeFunc(World.reshape)
glutMouseFunc(World.mouse)
glutMainLoop()

