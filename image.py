import Image
import ImageDraw
import math
import random
import time

width = 400
height = 300

def drawTree(x1,y1, angle, depth):
    if depth > 0:
        if depth > 2:
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * 5)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * 5)
            color = (48,24,12)
            draw.line((x1,y1,x2,y2), fill=color, width = depth ** 2 / 2**3)
        else:
            x2 = x1 + int(math.cos(math.radians(angle)) * 5)
            y2 = y1 + int(math.sin(math.radians(angle)) * 5)
            color = (0,255,0)
            draw.line((x1,y1,x2,y2), fill=color, width = 3)


#        drawTree(x2, y2, angle - 40, depth - 2)
#        drawTree(x2, y2, angle + 0, depth - 1)
#        drawTree(x2, y2, angle + 40, depth - 2)

        drawTree(x2, y2, angle - random.randint(10,40), depth - 2)
        drawTree(x2, y2, angle + random.randint(-5,5), depth -1)
        drawTree(x2, y2, angle + random.randint(10,40), depth -2)

img = Image.new('RGB', (width,height), 'black')
draw = ImageDraw.Draw(img)

drawTree(width / 2,height, - 90, 10)
draw.text((20,20), 'I am Groot', fill = (255,255,255))

img.save('baum.png', 'PNG')
del draw
del img
