import pygame, sys
from pygame.locals import *
from pygame import gfxdraw

pygame.init()

size = (700,700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Mid-Point Circle Drawing Algorithm")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)

screen_surface.fill(WHITE)


def mid_point_circle(radius, xc , yc):
	x0,y0 = 0, radius
	print("Radius of circle: {}".format(radius))
	gfxdraw.pixel(screen_surface, x0,y0, BLACK)
	#initial decision parameter
	if type(radius) == float:
		p0 = (5/4)  - radius
	else:
		p0 = 1 - radius

	pk = p0
	x, y = x0, y0

	while x < y:
		if pk < 0:
			x, y = x + 1, y
			pk = pk + 2 * x + 1
			gfxdraw.pixel(screen_surface, x + xc, y + yc, BLACK)
			plot_other_points(x,y,xc,yc)
		else:
			x, y = x + 1, y - 1
			pk = pk + 2 * x - 2 * y + 1
			gfxdraw.pixel(screen_surface, x + xc, y + yc, BLACK)
			plot_other_points(x, y, xc, yc)
	# print("Center : {}".format(x, y))

def plot_other_points(x,y,xc,yc):
	gfxdraw.pixel(screen_surface,x + xc, -y+xc, BLACK)
	gfxdraw.pixel(screen_surface, -x + xc, y + yc, BLACK)
	gfxdraw.pixel(screen_surface, -x + xc, -y + yc, BLACK)
	gfxdraw.pixel(screen_surface, y + xc, x + yc, BLACK)
	gfxdraw.pixel(screen_surface, y + xc, -x + yc, BLACK)
	gfxdraw.pixel(screen_surface, -y + xc, -x + yc, BLACK)
	gfxdraw.pixel(screen_surface, -y + xc, x + yc, BLACK)

mid_point_circle(100,200,200)


pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()