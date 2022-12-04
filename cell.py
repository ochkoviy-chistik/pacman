class Cell:
    def __init__(self, cell_x, cell_y, center):
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.center = center
        self.upper_left_corner = center[0] - self.cell_x // 2, center[1] - self.cell_y // 2

    def draw(self, screen):
        pass
