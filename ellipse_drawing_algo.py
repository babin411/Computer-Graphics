import pygame, sys
from pygame.locals import *
from pygame import gfxdraw
import math

pygame.init()

size = (700,700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Mid-point Ellipse Drawing Algorithm")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)

screen_surface.fill(WHITE)


def draw_ellipse(rx, ry, xc,yc):
    x , y = 0 , ry
    points = []
    #for region 1
    p1 = ry**2 - (rx**2 * ry) + (1/4)*(rx**2)
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    while(dx < dy):
        if p1 < 0:
            x , y = x + 1, y
            dx = dx + 2 * ry**2
            p1 = p1 + dx + ry**2
            gfxdraw.pixel(screen_surface, x + xc, y + yc, BLACK)
            draw_other_points(x, y, xc, yc)
            points.append((x+xc,y+yc))
        else:
            x , y = x + 1, y -1
            dx = dx + (2*ry**2)
            dy = dy - (2*rx**2)
            p1 = p1 + dx - dy + ry**2
            gfxdraw.pixel(screen_surface, x + xc, y + yc, BLACK)
            draw_other_points(x, y, xc, yc)
            points.append((x+xc,y+yc))
    #for region 2
    p2 = ry**2 * (x + (1/2))**2 + rx**2 * (y-1)**2 - (rx**2 * ry**2)

    while (y>=0):
        if p2 > 0:
            x, y = x, y-1
            dy = dy - (2*rx*rx)
            p2 = p2 + (rx**2) - dy
            gfxdraw.pixel(screen_surface, x + xc, y + yc, BLACK)
            draw_other_points(x, y, xc, yc)
            points.append((x+xc,y+yc))
        else:
            x,y = x+1, y-1
            dx = dx + (2*ry**2)
            dy = dy - (2*rx**2)
            p2 = p2 + dx -dy + (rx**2)
            gfxdraw.pixel(screen_surface, x + xc, y + yc, BLACK)
            draw_other_points(x, y, xc, yc)
            points.append((x+xc,y+yc))

    for point in points:
        print(point)

def draw_other_points(x,y,xc,yc):
    gfxdraw.pixel(screen_surface, x + xc, -y + yc, BLACK)
    gfxdraw.pixel(screen_surface, -x + xc, y + yc, BLACK)
    gfxdraw.pixel(screen_surface, -x + xc, -y + yc, BLACK)


draw_ellipse(80,60,100,100)


pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
