import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

pygame.init()

size = (700,700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)

screen_surface.fill(WHITE)

def bresenham(x0,y0,x1,y1):
    dx = x1 - x0
    dy = y1 - y0
    m = abs(dy/dx)
    print('Slope (m) = {}'.format(m))
    if m < 1:
        print("Slope less than one.")
        gfxdraw.pixel(screen_surface, round(x0), round(y0), BLACK)
        bresenham_l(dx, dy,x0,y0)
        # pass
    else:
        print("Sloper greater than one.")
        gfxdraw.pixel(screen_surface, round(x0), round(y0), BLACK)
        bresenham_g(dx,dy,x0,y0)

def bresenham_l(dx,dy,x0,y0):
    #initial decision parameter
    p0 = 2 * dy - dx
    x,y = x0,y0
    pk = p0

    points = []
    for i in range(abs(dx)):
        if pk < 0:
            x,y = x+1, y
            gfxdraw.pixel(screen_surface, round(x), round(y), BLACK)
            pk = pk + 2 * dy
            points.append((pk,x,y))
        else:
            x,y = x + 1, y+1
            gfxdraw.pixel(screen_surface, round(x), round(y), BLACK)
            pk = pk + 2 * dy - 2 * dx
            points.append((pk,x,y))

    for point in points:
        print(point)


def bresenham_g(dx,dy,x0,y0):
    #initial decision parameter
    p0 = 2 * dx - dy
    x,y = x0,y0
    pk = p0

    points = []
    for i in range(abs(dy)):
        if pk < 0:
            x,y = x, y+1
            gfxdraw.pixel(screen_surface, round(x), round(y), BLACK)
            pk = pk + 2 * dy
            points.append((pk,x,y))
        else:
            x,y = x + 1, y+1
            gfxdraw.pixel(screen_surface, round(x), round(y), BLACK)
            pk = pk + 2 * dx - 2 * dy
            points.append((pk,x,y))

    for point in points:
        print(point)


bresenham(600,700,100,100)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(  )