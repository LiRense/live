import pygame

class Cell():
    def __init__(self, height,width,pos_x, pos_y):
        self.size_w = width
        self.size_l = height
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.size_w, self.size_l)