import pygame
from map_objects.cell import Cell


class Seed (Cell):
    visibility = True

    def __init__(self, seed_x, seed_y, center):
        super().__init__(seed_x, seed_y, center)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.center, 3)

    #должен быть еще цикл добавления сидов на карту. Это у леши в __init__ карты.

    #должна быть проверка на оставшиеся зерна и геймовер. Хз у кого это

def eat_seed(seed, score_str):
    seed.visibility = False
    new_score = int(score_str) + 10
    score_str = str(new_score)
    #print('It works')
    return score_str

seed = Seed(0,0,(0,0))
eat_seed(seed, '0')
