import random
import pygame


white = pygame.Color(255, 255, 255)


class Food():
    def __init__(self, win_x, win_y):
        self.win_x = win_x
        self.win_y = win_y
        self.pos = [random.randrange(1, (self.win_x // 10)) * 10,
                    random.randrange(1, (self.win_y // 10)) * 10]
        self.spawn = True

    def __getitem__(self, key):
        return self.pos[key]

    def new(self):
        self.pos = [random.randrange(1, (self.win_x // 10)) * 10,
                    random.randrange(1, (self.win_y // 10)) * 10]

    def draw(self, game_window):
        pygame.draw.rect(game_window, white, pygame.Rect(self.pos[0], self.pos[1], 10, 10))
