import sys
import pygame
from constants import *
from map_objects.cell import Cell
from map_objects.wall import Wall
from map_objects.door import Door
from seed import Seed


class Matrix:
    def __init__(self):
        self.game_matrix = []
        self.object_count_x = 27  # количество объектов, которые можно разместить по горизонтали
        self.object_count_y = 28  # количество объектов, которые можно разместить по вертикали
        # размер пакмана: 22х22
        self.size = 22
        self.margin_x = WINDOW_SIZE[0] - (self.size * self.object_count_x)
        self.margin_y = WINDOW_SIZE[1] - (self.size * self.object_count_y)
        self.rect_width = WINDOW_SIZE[0] - self.margin_x
        self.rect_height = WINDOW_SIZE[1] - self.margin_y
        self.rect_position_x = WINDOW_SIZE[0] // 2 - self.rect_width // 2
        self.rect_position_y = WINDOW_SIZE[1] // 2 - self.rect_height // 2
        self.cell_x = self.rect_width // self.object_count_x
        self.cell_y = self.rect_height // self.object_count_y

        for i in range(self.object_count_y):
            lst = []
            for j in range(self.object_count_x):
                center = self.rect_position_x + j * self.cell_x + self.cell_x // 2,\
                         self.rect_position_y + i * self.cell_y + self.cell_y // 2
                cell = Cell(self.cell_x, self.cell_y, center)
                lst.append(cell)
            self.game_matrix.append(lst)
        self.add_walls()
        self.add_doors()
        self.add_seeds()

    def draw_palette(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.rect_position_x,
                                               self.rect_position_y,
                                               self.rect_width, self.rect_height), 2)

        for i in range(self.object_count_x - 1):
            x_position_4_line = self.margin_x / 2 + (i + 1) * self.cell_x
            start_y_position_4_line = self.rect_position_y
            stop_y_position_4_line = self.rect_position_y + self.rect_height - 2
            pygame.draw.line(screen, (0, 255, 0),
                             (x_position_4_line, start_y_position_4_line),
                             (x_position_4_line, stop_y_position_4_line), 2)

        for i in range(self.object_count_y - 1):
            y_position_4_line = self.margin_y / 2 + (i + 1) * self.cell_y
            start_x_position_4_line = self.rect_position_x
            stop_x_position_4_line = self.rect_position_x + self.rect_width - 2
            pygame.draw.line(screen, (0, 255, 0),
                             (start_x_position_4_line, y_position_4_line),
                             (stop_x_position_4_line, y_position_4_line), 2)

    def add_walls(self):
        for wall_position_x, wall_position_y in WALLS_POSITIONS:
            cell = self.game_matrix[wall_position_x][wall_position_y]
            self.game_matrix[wall_position_x][wall_position_y] = Wall(cell.cell_x, cell.cell_y, cell.center)

    def add_doors(self):
        for door_position_x, door_position_y in DOOR_POSITIONS:
            cell = self.game_matrix[door_position_x][door_position_y]
            self.game_matrix[door_position_x][door_position_y] = Door(cell.cell_x, cell.cell_y, cell.center)

    def add_seeds(self):
        for seed_position_x, seed_position_y in SEEDS_POSITIONS:
            cell = self.game_matrix[seed_position_x][seed_position_y]
            self.game_matrix[seed_position_x][seed_position_y] = Seed(cell.cell_x, cell.cell_y, cell.center)

    def draw(self, screen, draw_palette=False):
        for row in self.game_matrix:
            for cell in row:
                cell.draw(screen)
        if draw_palette:
            self.draw_palette(screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    matrix = Matrix()

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        matrix.draw(screen)
        pygame.time.wait(10)
        pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()
