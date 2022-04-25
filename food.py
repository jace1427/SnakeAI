import random


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
