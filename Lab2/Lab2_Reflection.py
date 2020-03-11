import numpy as np
import pygame, sys
from pygame.locals import *
from pygame import gfxdraw
from .functions2 import convert_to_homogeneous_coordinate, convert_to_graph_coordinate, rotation, reflection



pygame.init()

size = (700,700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Transformation")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)

screen_surface.fill(WHITE)


#------------------------------------------------------------------------#


x_coord = [10,50,50,10]
y_coord = [50,50,10,10]
no_of_coord = 4

graph_old = []
def draw_original_polygon(original_x_coordinate, original_y_coordinate):
    for i in range(no_of_coord):
        temp_x_old, temp_y_old = convert_to_graph_coordinate(original_x_coordinate, original_y_coordinate, no_of_coord)
        # print("Rotated Original X Coordinate : {} ".format(temp_x_old))
        # print("Rotated Original Y Coordinate : {} ".format(temp_y_old))
        temp_graph_old = [temp_x_old[i], temp_y_old[i]]
        graph_old.append(temp_graph_old)
    # print(graph_old)
    pygame.gfxdraw.line(screen_surface, 350,0,350,700, BLACK)
    pygame.gfxdraw.line(screen_surface, 0,350,700,350, BLACK)
    pygame.gfxdraw.polygon(screen_surface, graph_old, RED)


graph_new = []
def draw_new_polygon(new_x_coordinate, new_y_coordinate):
    for i in range(no_of_coord):
        temp_x_new, temp_y_new = convert_to_graph_coordinate(new_x_coordinates, new_y_coordinates,no_of_coord)
        temp_graph_new = [temp_x_new[i], temp_y_new[i]]
        graph_new.append(temp_graph_new)
    # print(graph_new)
    pygame.gfxdraw.polygon(screen_surface, graph_new, BLUE)


print("Original X Coordinate: {}".format(x_coord))
print("Original Y Coordinate: {}".format(y_coord))




original_homogeneous_coordinate  = convert_to_homogeneous_coordinate(x_coord, y_coord, no_of_coord)
# print("Original Homogeneous coordinate: {}".format(original_homogeneous_coordinate))
# print('------')

rotated_original_x_coordinates, rotated_original_y_coordinates = rotation(original_homogeneous_coordinate)
# print("Rotated Original X Coordinate : {} ".format(rotated_original_x_coordinates))
# print("Rotated Original Y Coordinate : {} ".format(rotated_original_y_coordinates))

# reflected_homogeneous_coordinates = reflection(original_homogeneous_coordinate, no_of_coord)
reflected_homogeneous_coordinates = reflection(original_homogeneous_coordinate, 1, no_of_coord)
# print(reflected_homogeneous_coordinates)
# print(scaled_homogeneous_coordinates)
new_x_coordinates, new_y_coordinates = rotation(reflected_homogeneous_coordinates)
# print("Scaled and Rotated X Coordinate: {}".format(new_x_coordinates))
# print("Scaled and Rotated Y Coordinate: {}".format(new_y_coordinates))



draw_original_polygon(rotated_original_x_coordinates, rotated_original_y_coordinates)

draw_new_polygon(new_x_coordinates, new_y_coordinates)




#------------------------------------------------------------------------#


pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()