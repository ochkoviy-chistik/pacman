import pygame
from map_objects.cell import Cell


class Door (Cell):
    def __init__(self, cell_x, cell_y, center):
        super().__init__(cell_x, cell_y, center)

    def draw(self, screen):
        pygame.draw.rect(screen, (63, 0, 0),
                         (self.upper_left_corner[0], self.upper_left_corner[1],
                          self.cell_x, self.cell_y // 3))
