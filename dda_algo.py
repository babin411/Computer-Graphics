import pygame, sys
		# x = x + x_inc
from pygame.locals import *
from pygame import gfxdraw

pygame.init()

size = (700,700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("DDA Line Drawing Algorithm")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)

screen_surface.fill(WHITE)

def dda(x0,y0,x1,y1):
	dx = x1 - x0
	dy = y1 - y0

	if abs(dx) > abs(dy):
		stepsize = dx
	else:
		stepsize = dy

	x_inc = dx / stepsize
	y_inc = dy / stepsize

	gfxdraw.pixel(screen_surface,x0,y0, BLACK)
	x, y = x0, y0
	points = []
	for i in range(stepsize):
		x = x + x_inc
		y = y + y_inc
		points.append((x,y))
		gfxdraw.pixel(screen_surface, round(x), round(y), BLACK)

	for point in points:
		print(point)

dda(200,300,500,600)


pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
