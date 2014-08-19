from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import sys, os, traceback
import gl_shader
if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"
from math import *
pygame.display.init()
pygame.font.init()

class Source(object):
    def __init__(self, pos=[0.0,0.0],strength=-0.1):
        self.pos = list(pos)
        self.strength = strength
    def __repr__(self): return str(self.strength)+"@["+str(self.pos[0])+","+str(self.pos[1])+"]"
    def pass_to(self, shader,i):
        shader.pass_vec2("sources["+str(i)+"].pos",self.pos)
        shader.pass_float("sources["+str(i)+"].strength",self.strength)
    def draw(self, selected):
        if selected: glColor3f(0,1,1)
        else:        glColor3f(1,1,0)
        glBegin(GL_POINTS)
        glVertex3f(self.pos[0],0.0,self.pos[1])
        glEnd()
        glColor3f(1,1,1)

######## SIMULATION PARAMETERS ########
max_sources = 16 #Maximum number of field sources (i.e. maximum length of "sources" variable)

N      = 16 #Number of simulated cells per block
offset = -4 #first block
scale  =  8 #num blocks each axis

sources = [Source()]

######## GRAPHICS PARAMETERS ########
screen_size = [1024,768]
multisample = 0
cutoff_magnitude = 1.0 #magnitude after which fields will not be drawn

######## USAGE ########

print("Field Intersections by Ian Mallett")
print("  Notes:")
print("    A fixed number of sources are supported; this can be increased/decreased")
print("      by adjusting the simulation parameters.")
print("    By default (for compatibility), no multisampling is enabled under graphics")
print("      parameters.  Rendering quality is drastically increased by adding it.")
print("")
print("  Controls:")
print("    ESCAPE             - Quit")
print("")
print("    A                  - Add a new source")
print("    X                  - Remove the selected source")
print("")
print("    UP ARROW           - Add to selected source's magnitude")
print("    DOWN ARROW         - Subtract from selected source's magnitude")
print("    SHIFT + UP ARROW   - Add to selected source's magnitude (fast)")
print("    SHIFT + DOWN ARROW - Subtract from selected source's magnitude (fast)")
print("")
print("    Left-Click         - Toggle select a source")
print("    Drag               - Moves the selected source")
print("")
print("    Right-Click + Drag - Rotate camera")
print("    Scrollwheel        - Zoom camera")

######## PROGRAM ########

icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("Field Intersections - Ian Mallett - v.1.0.0 - 2014")
if multisample:
    pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS,1)
    pygame.display.gl_set_attribute(GL_MULTISAMPLESAMPLES,multisample)
pygame.display.set_mode(screen_size,OPENGL|DOUBLEBUF)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)

##glEnable(GL_TEXTURE_2D)
##glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
##glTexEnvi(GL_POINT_SPRITE,GL_COORD_REPLACE,GL_TRUE)

glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)

glPointSize(10)

shader = gl_shader.Shader([
    gl_shader.ProgramShaderVertex("""
struct Source { vec2 pos; float strength; };
uniform Source sources["""+str(max_sources)+"""];
uniform int num_sources;
uniform float sc;
varying float kill;
void main(void) {
    float field = 0.0;
    for (int i=0;i<num_sources;++i) {
        vec2 delta = gl_Vertex.xz - sources[i].pos;
        field += sources[i].strength / dot(delta,delta);
    }
    
    field *= sc;
    
    kill = """+str(cutoff_magnitude)+"""+1.0 - abs(field);
    
    gl_FrontColor = gl_Color;
    gl_Position = gl_ModelViewProjectionMatrix * vec4(gl_Vertex.x,field,gl_Vertex.z, 1.0);
}
    """),
    gl_shader.ProgramShaderFragment("""
varying float kill;
void main(void) {
    vec4 color = gl_Color;
    color.a *= clamp(kill,0.0,1.0);
    gl_FragData[0] = color;
}""")
])
shader.print_errors()

dl_map = glGenLists(1)
glNewList(dl_map,GL_COMPILE)
def vert(x,z):
    glVertex3f(
        offset+scale*float(x)/float(N*scale-1),
        0.0,
        offset+scale*float(z)/float(N*scale-1)
    )
glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
glBegin(GL_QUADS)
for z in range(N*scale):
    for x in range(N*scale):
        vert(x,  z  )
        vert(x+1,z  )
        vert(x+1,z+1)
        vert(x,  z+1)
glEnd()
glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
glColor3f(1,0,0)
glBegin(GL_LINES)
for z in range(0,N*scale+1,N):
    for x in range(N*scale):
        vert(x,  z)
        vert(x+1,z)
for z in range(N*scale):
    for x in range(0,N*scale+1,N):
        vert(x,z  )
        vert(x,z+1)
glEnd()
glColor3f(1,1,1)
glEndList()

selected_source = -1

camera_rot = [35.0,20.0]
camera_radius = 6.0
camera_center = [0.0,0.0,0.0]
def get_input():
    global mouse_position, camera_rot,camera_radius, sources,selected_source
    keys_pressed = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos()
    mouse_rel = pygame.mouse.get_rel()
    for event in pygame.event.get():
        if   event.type == QUIT: return False
        elif event.type == KEYDOWN:
            if   event.key == K_ESCAPE: return False
##            elif event.key == K_1: selected_source=0
##            elif event.key == K_2: selected_source=1
##            elif event.key == K_3: selected_source=2
##            elif event.key == K_4: selected_source=3
##            elif event.key == K_5: selected_source=4
##            elif event.key == K_6: selected_source=5
##            elif event.key == K_7: selected_source=6
##            elif event.key == K_8: selected_source=7
##            elif event.key == K_9: selected_source=8
            elif event.key == K_a:
                if len(sources) < max_sources:
                    sources.append(Source())
            elif event.key == K_x:
                if len(sources) != 0 and selected_source != -1:
                    sources2 = []
                    for s in sources:
                        if s == sources[selected_source]:
                            continue
                        else:
                            sources2.append(s)
                    sources = sources2
                    selected_source = -1
        elif event.type == MOUSEBUTTONDOWN:
            if   event.button == 4: camera_radius *= 0.9
            elif event.button == 5: camera_radius /= 0.9
            else:
                if len(sources) > 0:
                    l2s = []
                    for s in sources:
                        delta = [cursor_x-s.pos[0],cursor_z-s.pos[1]]
                        l2 = delta[0]*delta[0] + delta[1]*delta[1]
                        l2s.append(l2)
                    m = min(zip(l2s,range(0,len(sources),1)))
                    if m[0] < 0.2:
                        if selected_source == m[1]:
                            selected_source = -1
                        else:
                            selected_source = m[1]
    if mouse_buttons[2]:
        camera_rot[0] += mouse_rel[0]
        camera_rot[1] += mouse_rel[1]
    if selected_source != -1:
        if keys_pressed[K_UP]:
            if keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]:
                sources[selected_source].strength += 0.010
            else:
                sources[selected_source].strength += 0.001
        if keys_pressed[K_DOWN]:
            if keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]:
                sources[selected_source].strength -= 0.010
            else:
                sources[selected_source].strength -= 0.001
    return True
def draw():
    global cursor_x,cursor_z
    #View
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

    #Pass 1: picking for moving mouse
    glClear(GL_DEPTH_BUFFER_BIT)

    glBegin(GL_QUADS)
    glVertex3f(-10000.0,0.0,-10000.0)
    glVertex3f( 10000.0,0.0,-10000.0)
    glVertex3f( 10000.0,0.0, 10000.0)
    glVertex3f(-10000.0,0.0, 10000.0)
    glEnd()

    viewport = glGetIntegerv(GL_VIEWPORT)
    modelview = glGetDoublev(GL_MODELVIEW_MATRIX)
    projection = glGetDoublev(GL_PROJECTION_MATRIX)

    win_x,win_y = mouse_position[0],screen_size[1]-mouse_position[1]
    win_z = glReadPixels(win_x,win_y,1,1,GL_DEPTH_COMPONENT,GL_FLOAT)
    cursor_x,cursor_y,cursor_z = gluUnProject(win_x,win_y,win_z,modelview,projection,viewport)

    if selected_source != -1 and selected_source < len(sources):
        sources[selected_source].pos[0] = cursor_x
        sources[selected_source].pos[1] = cursor_z

    #Pass 2: draw normally
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glDisable(GL_DEPTH_TEST)
    gl_shader.Shader.use(shader)
    for i in range(len(sources)):
        sources[i].pass_to(shader,i)
    shader.pass_int("num_sources",len(sources))
    shader.pass_float("sc",1.0)
    glCallList(dl_map)
    gl_shader.Shader.use(None)
    glEnable(GL_DEPTH_TEST)

    i = 0
    for s in sources:
        s.draw(i==selected_source)
        i += 1

##    glColor3f(1,0,0)
##    glBegin(GL_LINE_LOOP)
##    glVertex3f(0,0,0)
##    glVertex3f(1,0,0)
##    glVertex3f(1,0,1)
##    glVertex3f(0,0,1)
##    glEnd()
##    glColor3f(1,1,1)

##    glBegin(GL_LINES)
##    glVertex3f(obj_x,0,obj_z)
##    glVertex3f(obj_x,1,obj_z)
##    glEnd()
    
    pygame.display.flip()
def main():
    clock = pygame.time.Clock()
    while True:
##        print(sources)
        if not get_input(): break
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
