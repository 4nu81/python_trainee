from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import sys, os, traceback
if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"
from math import *
pygame.display.init()
pygame.font.init()

import gl_shader as mod_program
import gl_texture as mod_texture
from quaternion import *

screen_size = [1000,500]
multisample = 0
icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("Off-Center Map Projections - Ian Mallett - v.1.0.0 - 2014")
if multisample:
	pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS,1)
	pygame.display.gl_set_attribute(GL_MULTISAMPLESAMPLES,multisample)
pygame.display.set_mode(screen_size,OPENGL|DOUBLEBUF)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)

glEnable(GL_TEXTURE_2D)
#glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
#glTexEnvi(GL_POINT_SPRITE,GL_COORD_REPLACE,GL_TRUE)

glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)
glEnable(GL_DEPTH_TEST)

program = mod_program.Program([
	mod_program.ShaderFragment("""
uniform sampler2D tex2D_1;
uniform vec4 rotation;
const float tau = 6.28318530718;
//a + bi + cj + dk
//w + xi + yj + zk
vec4 q_conjugate(vec4 q) {
    return vec4(q.x,-q.yzw);
}
vec4 qq_mult(vec4 q1, vec4 q2) {
	return vec4(
		q1.x*q2.x - q1.y*q2.y - q1.z*q2.z - q1.w*q2.w,
		q1.x*q2.y + q1.y*q2.x + q1.z*q2.w - q1.w*q2.z,
		q1.x*q2.z - q1.y*q2.w + q1.z*q2.x + q1.w*q2.y,
		q1.x*q2.w + q1.y*q2.z - q1.z*q2.y + q1.w*q2.x
    );
}
vec3 qv_mult(vec4 q1, vec3 v1) {
    vec4 q2 = vec4(0.0,v1);
    return qq_mult(qq_mult(q1,q2), q_conjugate(q1)).yzw;
}
void main(void) {
	float s = gl_TexCoord[0].x;
	float t = gl_TexCoord[0].y;

	vec3 world = vec3(
		cos(tau * s) * cos(0.5*tau*(t-0.5)),
		               sin(0.5*tau*(t-0.5)),
		sin(tau * s) * cos(0.5*tau*(t-0.5))
	);
	world = qv_mult(rotation,world);

	s = (1.0/tau)*atan(world.z,world.x);
	t = 0.5 + (1.0/(0.5*tau))*asin(world.y);

	gl_FragData[0] = texture2D(tex2D_1,vec2(s,t));
}""")
])
program.print_errors()

texture = mod_texture.Texture2D.from_path("equirectangular.jpg");
texture.set_nicest()

rotation = [1.0,0.0,0.0,0.0]

def get_input():
	global rotation
	keys_pressed = pygame.key.get_pressed()
	mouse_buttons = pygame.mouse.get_pressed()
	mouse_position = pygame.mouse.get_pos()
	mouse_rel = pygame.mouse.get_rel()
	for event in pygame.event.get():
		if   event.type == QUIT: return False
		elif event.type == KEYDOWN:
			if   event.key == K_ESCAPE: return False
	sc = 0.01
	if keys_pressed[K_a]:
		rotation = qq_mult(rotation,axisangle_to_q((0.0,1.0,0.0), sc))
	if keys_pressed[K_d]:
		rotation = qq_mult(rotation,axisangle_to_q((0.0,1.0,0.0),-sc))
	if keys_pressed[K_s]:
		rotation = qq_mult(rotation,axisangle_to_q((0.0,0.0,1.0), sc))
	if keys_pressed[K_w]:
		rotation = qq_mult(rotation,axisangle_to_q((0.0,0.0,1.0),-sc))
	if keys_pressed[K_q]:
		rotation = qq_mult(rotation,axisangle_to_q((1.0,0.0,0.0),-sc))
	if keys_pressed[K_e]:
		rotation = qq_mult(rotation,axisangle_to_q((1.0,0.0,0.0), sc))
	return True
def draw():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	
	glViewport(0,0,screen_size[0],screen_size[1])
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,screen_size[0],0,screen_size[1])
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	mod_program.Program.use(program)
	program.pass_texture(texture,1)
	program.pass_vec4("rotation",rotation)

	glBegin(GL_QUADS);
	glTexCoord2f(0.0,0.0); glVertex2f(             0,             0)
	glTexCoord2f(1.0,0.0); glVertex2f(screen_size[0],             0)
	glTexCoord2f(1.0,1.0); glVertex2f(screen_size[0],screen_size[1])
	glTexCoord2f(0.0,1.0); glVertex2f(             0,screen_size[1])
	glEnd();

	mod_program.Program.use(None)
	
	pygame.display.flip()
def main():
	clock = pygame.time.Clock()
	while True:
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

