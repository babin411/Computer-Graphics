import pygame, sys
from pygame.locals import *
from pygame import gfxdraw


pygame.init()

size = (700,700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Window To Viewport Transformation!")

BLACK = (0,0,0)
WHITE = (255,255,255)

screen_surface.fill(WHITE)

#---------------------------------------------------------------------------------------------------------------------------------#

def Window_to_viewport_transformation(xw,yw,xwmin,xwmax,ywmin,ywmax,xvmin,xvmax,yvmin,yvmax):
    #calculating values of scaling factor sx and sy
    sx = (xvmax - xvmin) / (xwmax - xwmin)
    sy = (yvmax - yvmin) / (ywmax - ywmin)

    #calculating viewport points
    xv = xvmin + (xw - xwmin) * sx
    yv = yvmin + (yw - ywmin) * sy
    return int(xv), int(yv)



#defining window boundaries
xwmin = 20
xwmax = 80
ywmin = 40
ywmax = 80

#defining viewport boundaries
xvmin = 30
xvmax = 60
yvmin = 40
yvmax = 60

# x_coordinate_of_viewport, y_coordinate_of_viewport = Window_to_viewport_transformation(xw,yw,xwmin,xwmax,ywmin,ywmax,xvmin,xvmax,yvmin,yvmax)
# print("X-Coordinate of Viewport: {}\n"
#       "Y-Coordinate of Viewpoert: {}".format(int(x_coordinate_of_viewport),int(y_coordinate_of_viewport)))
x_coord = []
y_coord = []
no_of_coord = 2
for i in range(no_of_coord):
    x = int(input("Enter x-coordinate: "))
    y = int(input("Enter y-coordinate: "))
    x_coord.append(x)
    y_coord.append(y)

transformed_x_coord = []
transformed_y_coord = []
for i in range(no_of_coord):
    x_coordinate_of_viewport, y_coordinate_of_viewport = Window_to_viewport_transformation(x_coord[i],y_coord[i],xwmin,xwmax,ywmin,ywmax,xvmin,xvmax,yvmin,yvmax)
    transformed_x_coord.append(x_coordinate_of_viewport)
    transformed_y_coord.append(y_coordinate_of_viewport)

coordinate1 = (int(transformed_x_coord[0]), int(transformed_y_coord[0]))
coordinate2 = (int(transformed_x_coord[1]), int(transformed_y_coord[1]))


for i in range(no_of_coord):
    print("X-Coordinate of viewport {}: {}".format(i,transformed_x_coord[i]))
    print("Y-Coordinate of Viewport {}: {}".format(i,transformed_y_coord[i]))




pygame.draw.line(screen_surface, BLACK, coordinate1, coordinate2, 1)
#---------------------------------------------------------------------------------------------------------------------------------#
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()