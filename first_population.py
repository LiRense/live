import random
from random import randint

def counter_cels(matrix):
    total_elements = 0

    for row in matrix:
        for element in row:
            total_elements += element['cell']
    # print(total_elements)
    return total_elements

def start_colony(first_colony):
    first_cells = []

    for height in range(first_colony['areal']['height']):
        layer = []
        for width in range(first_colony['areal']['width']):
            status = {}
            status['location'] = {'x': height, 'y': width}
            if counter_cels(first_cells) < first_colony['max_population']:
                status['cell'] = random.choice([0,1])
                layer.append(status)
            else:
                status['cell'] = 0
                layer.append(status)
        first_cells.append(layer)
        # print(first_cells)

    return changer(first_cells)


def changer(matrix):
    new_list = []
    for row in matrix:
        for element in row:
            if element['cell'] == 1:
                new_list.append([element['location']['x'],element['location']['y']])
    return new_list



