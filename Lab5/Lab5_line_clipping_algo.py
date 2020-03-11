
import pygame, sys
from pygame.locals import *
from pygame import gfxdraw


pygame.init()

size = (700,700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Cohen Sutherland Line Clipping Algorithm")

BLACK = (0,0,0)
WHITE = (255,255,255)
# RED = (255,0,0)
# GREEN = (0,128,0)
# BLUE = (0,0,255)

screen_surface.fill(WHITE)


#------------------------------------------------------------------------#


# Python program to implement Cohen Sutherland algorithm
# for line clipping. 
x1, y1,x2,y2 = 10,30,80,90
# Defining region codes 
INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000

# Defining x_max,y_max and x_min,y_min for rectangle 
# Since diagonal points are enough to define a rectangle 
x_max = 90
y_max = 70
x_min = 20
y_min = 20


# Function to compute region code for a point(x,y) 
def computeCode(x, y):
    code = INSIDE
    if x < x_min:  # to the left of rectangle
        code |= LEFT
    elif x > x_max:  # to the right of rectangle
        code |= RIGHT
    if y < y_min:  # below the rectangle
        code |= BOTTOM
    elif y > y_max:  # above the rectangle
        code |= TOP

    return code


# Implementing Cohen-Sutherland algorithm 
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2) 
def cohenSutherlandClip(x1, y1, x2, y2):
    # Compute region codes for P1, P2
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:

        # If both endpoints lie within rectangle 
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # If both endpoints are outside rectangle 
        elif (code1 & code2) != 0:
            break

        # Some segment lies within the rectangle 
        else:

            # Line Needs clipping 
            # At least one of the points is outside,  
            # select it 
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

                # Find intersection point
            # using formulas y = y1 + slope * (x - x1),  
            # x = x1 + (1 / slope) * (y - y1) 
            if code_out & TOP:

                # point is above the clip rectangle 
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:

                # point is below the clip rectangle 
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:

                # point is to the right of the clip rectangle 
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:

                # point is to the left of the clip rectangle 
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

                # Now intersection point x,y is found
            # We replace point outside clipping rectangle 
            # by intersection point 
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

    if accept:
        print("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1, y1, x2, y2))
        pygame.draw.line(screen_surface, BLACK,(400+x1,400-y1), (400+x2, 400-y2),1)
        # Here the user can add code to display the rectangle 
        # along with the accepted (portion of) lines 

    else:
        print("Line rejected")

    # Driver Script
pygame.draw.polygon(screen_surface, BLACK, ((x_min + 400, 400 - y_min),
                                        (x_max + 400, 400 - y_min),
                                        (x_max + 400, 400 - y_max),
                                        (x_min + 400, 400 - y_max)), 1)

# pygame.draw.line(screen_surface, BLACK,(400+x1, 400-y1),(400+x2, 400-y2))



# First Line segment
# P11 = (5, 5), P12 = (7, 7)

cohenSutherlandClip(x1,y1,x2,y2)



pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()