import pygame, sys
from pygame.locals import *
import pygame.gfxdraw


pygame.init()
screen_resolution = pygame.display.Info()
print(screen_resolution.current_h)
print(screen_resolution.current_w)

print(f"Screen Resolution : {screen_resolution.current_w} x {screen_resolution.current_h}")

size = (1500,1200)
window_surface = pygame.display.set_mode((size[0] - 400, size[1] - 300),HWSURFACE|DOUBLEBUF|RESIZABLE, 0, 32)
pygame.display.set_caption("Nepal's Flag")

#setting up color variables or constants RGB
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)
GRAY = (128,128,128)
LIME = (0,255,0)
PURPLE = (128,0,128)
TEAL = (0,128,128)
YELLOW = (255,255,0)

window_surface.fill(WHITE)
'''((300,100),(700,400),(475,400),(700,700),(300,700))'''


pygame.display.flip()


# pygame.gfxdraw.aapolygon(window_surface,((300,100),(700,400),(475,400),(700,700),(300,700)),BLUE)
# pygame.gfxdraw.polygon(window_surface,((300,100),(700,400),(475,400),(700,700),(300,700)),BLUE)
# pygame.gfxdraw.filled_polygon(window_surface,((300,100),(700,400),(475,400),(700,700),(300,700)),RED)
# pygame.gfxdraw.polygon(window_surface,((300,100),(700,400),(475,400),(700,700),(300,700)),RED)
# pygame.draw.polygon(window_surface, RED, ((310,)),0)
# pygame.gfxdraw.aapolygon(window_surface,((300,100),(700,400),(475,400),(700,700),(300,700)),RED)

'''Flag's Shape'''
pygame.gfxdraw.filled_polygon(window_surface,((300,100),(700,400),(475,400),(700,700),(300,700)), RED)
pygame.draw.polygon(window_surface,BLUE,((300,100),(700,400),(475,400),(700,700),(300,700),(300,800)), 15)

sun = pygame.image.load('sun1.png')
# pygame.transform.scale(window_surface, (0,0))
window_surface.blit(sun, (340,470))

moon = pygame.image.load('moon1.png')
window_surface.blit(moon, (340,230))
# pygame.gfxdraw.aacircle(window_surface,425, 550, 50, WHITE)
# pygame.gfxdraw.filled_circle(window_surface, 425, 550, 50, WHITE)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()