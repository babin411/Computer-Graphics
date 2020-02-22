import numpy as np
import pygame, sys
from pygame.locals import *
from pygame import gfxdraw


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


x_coord = [20,60,60,20]
y_coord = [60,60,20,20]
no_of_coord = 4


def convert_to_gc(x_coordinate, y_coordinate, no_of_coord):
    graph_x_coordinate = []
    graph_y_coordinate = []
    for i in range(no_of_coord):
        temp_x_coord = x_coordinate[i] + 350
        temp_y_coord = y_coordinate[i] + 350
        graph_x_coordinate.append(temp_x_coord)
        graph_y_coordinate.append(temp_y_coord)
    return graph_x_coordinate, graph_y_coordinate



def convert_to_hc(x_coordinate, y_coordinate, no_of_coord):
    list_of_homogeneous_coordinate = []
    for i in range(no_of_coord):
        temp_x_coord = x_coordinate[i]
        temp_y_coord = y_coordinate[i]
        homogeneous_coordinate = [temp_x_coord, temp_y_coord, 1]
        homogeneous_coordinate = np.asarray(homogeneous_coordinate).reshape(3, 1)
        list_of_homogeneous_coordinate.append(homogeneous_coordinate)

    list_of_homogeneous_coordinate = np.asarray(list_of_homogeneous_coordinate)

    return list_of_homogeneous_coordinate



def rotation(list_of_homogeneous_coordinate):
    theta = -90
    rotated_x_coordinate = []
    rotated_y_coordinate = []
    new_rotated_coordinate = []
    radian = ((2 * np.pi) / 360) * theta
    r = [np.cos(radian), -np.sin(radian), 0,
         np.sin(radian), np.cos(radian), 0,
         0, 0, 1]
    r = np.asarray(r).reshape(3, 3)
    for i in range(len(list_of_homogeneous_coordinate)):
        new_rotated_coordinate.append(np.dot(r, list_of_homogeneous_coordinate[i]))
        rotated_x_coordinate.append(new_rotated_coordinate[i][0][0])
        rotated_y_coordinate.append(new_rotated_coordinate[i][1][0])
    return rotated_x_coordinate, rotated_y_coordinate



def reflection(list_of_homogeneous_coordinate, axis, no_of_coord):
    reflected_x_coordinate = []
    reflected_y_coordinate = []
    new_coordinate_after_reflection = []
    if axis == 0:#for x-axis
        matrix_for_xaxis = [1,0,0,0,-1,0,0,0,1]
        matrix_for_xaxis = np.asarray(matrix_for_xaxis).reshape(3,3)
        for i in range(len(list_of_homogeneous_coordinate)):
            new_coordinate_after_reflection.append(np.dot(matrix_for_xaxis, list_of_homogeneous_coordinate[i]))
            reflected_x_coordinate.append(new_coordinate_after_reflection[i][0][0])
            reflected_y_coordinate.append(new_coordinate_after_reflection[i][1][0])
    elif axis == 1:
        matrix_for_yaxis = [-1, 0, 0, 0, 1, 0, 0, 0, 1]
        matrix_for_yaxis = np.asarray(matrix_for_yaxis).reshape(3, 3)
        for i in range(len(list_of_homogeneous_coordinate)):
            new_coordinate_after_reflection.append(np.dot(matrix_for_yaxis, list_of_homogeneous_coordinate[i]))
            reflected_x_coordinate.append(new_coordinate_after_reflection[i][0][0])
            reflected_y_coordinate.append(new_coordinate_after_reflection[i][1][0])
    else:
        print("You've entered wrong axis value.\n"
              "Enter:\n"
              "0 - for reflection along x-axis\n"
              "1 - for reflection along y-axis")

    print("Reflected X Coordinate: {}".format(reflected_x_coordinate))
    print("Reflected Y Coordinate: {}".format(reflected_y_coordinate))
    reflected_hc = convert_to_hc(reflected_x_coordinate, reflected_y_coordinate, no_of_coord)
    return reflected_hc


graph_old = []
def draw_o_polygon(original_x_coordinate, original_y_coordinate):
    for i in range(no_of_coord):
        temp_x_old, temp_y_old = convert_to_gc(original_x_coordinate, original_y_coordinate, no_of_coord)
        temp_graph_old = [temp_x_old[i], temp_y_old[i]]
        graph_old.append(temp_graph_old)
    pygame.gfxdraw.line(screen_surface, 350,0,350,700, BLACK)
    pygame.gfxdraw.line(screen_surface, 0,350,700,350, BLACK)
    pygame.gfxdraw.polygon(screen_surface, graph_old, RED)


graph_new = []
def draw_n_polygon(new_x_coordinate, new_y_coordinate):
    for i in range(no_of_coord):
        temp_x_new, temp_y_new = convert_to_gc(new_x_coordinate, new_y_coordinate,no_of_coord)
        temp_graph_new = [temp_x_new[i], temp_y_new[i]]
        graph_new.append(temp_graph_new)
    pygame.gfxdraw.polygon(screen_surface, graph_new, BLUE)



print("Original X Coordinate: {}".format(x_coord))
print("Original Y Coordinate: {}".format(y_coord))




original_homogeneous_coordinate  = convert_to_hc(x_coord, y_coord, no_of_coord)
rotated_x_coordinates, rotated_y_coordinates = rotation(original_homogeneous_coordinate)
reflected_hc = reflection(original_homogeneous_coordinate, 1,no_of_coord)
new_x_coordinates, new_y_coordinates = rotation(reflected_hc)
draw_o_polygon(rotated_x_coordinates, rotated_y_coordinates)
draw_n_polygon(new_x_coordinates, new_y_coordinates)



#------------------------------------------------------------------------#


pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()