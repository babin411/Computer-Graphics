import numpy as np



def convert_to_graph_coordinate(x_coord, y_coord, no_of_coord):
    '''takes a list of original x_coordinates and y_coordinates and transforms them into
    graph coordinates with 350,350 as its center.'''
    graph_x_coordinate = []
    graph_y_coordinate = []
    for i in range(no_of_coord):
        temp_x_coord = x_coord[i] + 350
        temp_y_coord = y_coord[i] + 350
        graph_x_coordinate.append(temp_x_coord)
        graph_y_coordinate.append(temp_y_coord)
    return graph_x_coordinate, graph_y_coordinate


def convert_to_homogeneous_coordinate(x_coordinate, y_coordinate, no_of_coord):
    '''takes a list of x_coordinates, y_coordinates and no of coordinates
    and runs a for loop for the coordinates and returns a
    list of homogeneous coordinate that has a bunch of homogeneous coordinates '''
    list_of_homogeneous_coordinate = []
    for i in range(no_of_coord):
        temp_x_coord = x_coordinate[i]
        temp_y_coord = y_coordinate[i]
        homogeneous_coordinate = [temp_x_coord, temp_y_coord, 1]
        homogeneous_coordinate = np.asarray(homogeneous_coordinate).reshape(3, 1)
        list_of_homogeneous_coordinate.append(homogeneous_coordinate)

    list_of_homogeneous_coordinate = np.asarray(list_of_homogeneous_coordinate)

    return list_of_homogeneous_coordinate



def rotation(list_of_homogeneous_coordinate, theta = -90):
    '''' take a list of homogenous coordinates and rotates it by an angle of 270 degree'''
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
    # print("Rotated X Coordinate: {}".format(rotated_x_coordinate))
    # print("Rotated Y Coordinate: {}".format(rotated_y_coordinate))

    return rotated_x_coordinate, rotated_y_coordinate



def scaling(list_of_homogeneous_coordinate, no_of_coord):
    '''takes a list of homogenous coordinate and using matrix multiplication
    sacles the x_coordinate and y_coordinate according to their scale factors.'''
    scaled_x_coordinate = []
    scaled_y_coordinate = []
    sx =4
    sy =4
    new_scaled_coordinate = []
    scaling_matrix = [sx,0,0,0,sy,0,0,0,1]
    scaling_matrix = np.asarray(scaling_matrix).reshape(3,3)
    for i in range(len(list_of_homogeneous_coordinate)):
        new_scaled_coordinate.append(np.dot(scaling_matrix, list_of_homogeneous_coordinate[i]))
        scaled_x_coordinate.append(new_scaled_coordinate[i][0][0])
        scaled_y_coordinate.append(new_scaled_coordinate[i][1][0])
    print("Scaled X Coordinate: {}".format(scaled_x_coordinate))
    print("Scaled Y Coordinate: {}".format(scaled_y_coordinate))
    scaled_homogeneous_coordinate = convert_to_homogeneous_coordinate(scaled_x_coordinate, scaled_y_coordinate, no_of_coord)
    return scaled_homogeneous_coordinate


def translation(list_of_homogeneous_coordinate, no_of_coord):
    translated_x_coordinate = []
    translated_y_coordinate = []
    tx = 100
    ty = 50
    new_translated_coordinate = []
    translation_matrix = [1,0,tx,0,1,ty,0,0,1]
    translation_matrix = np.asarray(translation_matrix).reshape(3,3)
    for i in range(len(list_of_homogeneous_coordinate)):
        new_translated_coordinate.append(np.dot(translation_matrix, list_of_homogeneous_coordinate[i]))
        translated_x_coordinate.append(new_translated_coordinate[i][0][0])
        translated_y_coordinate.append(new_translated_coordinate[i][1][0])
    print("Translated X Coordinate: {}".format(translated_x_coordinate))
    print("Translated Y Coordinate: {}".format(translated_y_coordinate))
    translated_homogeneous_coordinate = convert_to_homogeneous_coordinate(translated_x_coordinate, translated_y_coordinate, no_of_coord)
    return translated_homogeneous_coordinate


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
    translated_homogeneous_coordinate = convert_to_homogeneous_coordinate(reflected_x_coordinate, reflected_y_coordinate, no_of_coord)
    return translated_homogeneous_coordinate


def shearing(list_of_homogeneous_coordinate, axis, no_of_coord):
    sheared_x_coordinate =[]
    sheared_y_coordinate = []
    new_coordinate_after_shearing = []
    shx = 2
    shy = 2
    if axis == 0: #shearing along x-axis
        matrix_for_xshear = [1,shx,0,0,1,0,0,0,1]
        matrix_for_xshear = np.asarray(matrix_for_xshear).reshape(3,3)
        for i in range(len(list_of_homogeneous_coordinate)):
            new_coordinate_after_shearing.append(np.dot(matrix_for_xshear, list_of_homogeneous_coordinate[i]))
            sheared_x_coordinate.append(new_coordinate_after_shearing[i][0][0])
            sheared_y_coordinate.append(new_coordinate_after_shearing[i][1][0])
    elif axis ==1 :
        matrix_for_yshear = [1,0,0,shy,1,0,0,0,1]
        matrix_for_yshear = np.asarray(matrix_for_yshear).reshape(3,3)
        for i in range(len(list_of_homogeneous_coordinate)):
            new_coordinate_after_shearing.append(np.dot(matrix_for_yshear, list_of_homogeneous_coordinate[i]))
            sheared_x_coordinate.append(new_coordinate_after_shearing[i][0][0])
            sheared_y_coordinate.append(new_coordinate_after_shearing[i][1][0])

    print("Sheared X Coordinate: {}".format(sheared_x_coordinate))
    print("Sheared Y Coordinate: {}".format(sheared_y_coordinate))

    sheared_homogeneous_coordinate = convert_to_homogeneous_coordinate(sheared_x_coordinate, sheared_y_coordinate, no_of_coord)
    return sheared_homogeneous_coordinate