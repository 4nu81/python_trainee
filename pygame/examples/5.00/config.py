#!/usr/bin/python
# -*- coding: utf-8 -*-

#Initial screen resolution
screen_size = [800,600]

#Initial bounds of real axis
bounds_x = [-2.0,1.0]
#Initial bounds of complex axis
bounds_y = [-1.0,1.0]

#Will allow the zoom to go much deeper, but requires a newer GPU.
#With single-precision, can get up to 50,000x zoom.  With double
#precision, can get up to 10,000,000,000,000x zoom.
use_double_precision = False

#Smooth through the bands of color
use_smooth_shading = False

#How much to scale the colors' spacing, if they're smoothly shaded
smooth_shading_scale = 1.0

#For smooth shading, the iterations will need to be higher for a
#smaller shading scale.
iterations = 100

#Closer to 1.0 is slower zooming
#Closer to 0.0 is faster zooming
zoom_scalar = 0.98

#The amount of work done goes up quadratically with this number!  Compiling the shader will
#also take increasingly longer as this increases (maybe also quadratic).
antialias = 1
