import time

import pygame,sys
from random import randint
import Cells, first_population

first_colony = {'start': (0, 0), 'max_population': 400, 'areal': {'height': 20, 'width': 20},
                'size': 5}

first_cells = first_population.start_colony(first_colony)


def conver_to_rect(first_cells):

    cells = [Cells.Cell(first_colony['size'],
                        first_colony['size'],
                        element[0] * first_colony['size'],
                        element[1] * first_colony['size']).draw_rect() for element in
             first_cells]

    return cells

def near(x,y,cells,first_colony):
    # print(cells)
    counter=0
    eiht_sides = [[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]
    for i in eiht_sides:
        new_place = [x+i[0],y+i[1]]
        if new_place in cells:
            counter+=1
    return counter


def check_cells(old):
    new = list(old)

    min_x = min(old, key=lambda x: x[0])[0]
    max_x = max(old, key=lambda x: x[0])[0]

    min_y = min(old, key=lambda y: y[1])[1]
    max_y = max(old, key=lambda y: y[1])[1]

    for i in range(min_y, max_y+3):
        for j in range(min_x, max_x+3):
            count = near(j, i, old, first_colony)
            if [j, i] in old:
                if count in (2,3):
                    pass
                elif count > 3:
                    new.remove([j, i])
                elif count < 2:
                    new.remove([j, i])
            else:
                if count == 3:
                    new.append([j, i])

    return new

windows_w = 1000
windows_h = 800

pygame.init()
screen = pygame.display.set_mode((windows_w, windows_h))

while True:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

    cells = conver_to_rect(first_cells)
    for cell in cells:
        pygame.draw.rect(screen, 'white', cell, 0)
    pygame.display.update()
    first_cells = check_cells(first_cells)
    if first_cells == []:
        break