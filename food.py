import numpy as np


class Food():

    def __init__(self):
        self.pos = np.zeros([400 + np.random.rand(0, 40) * 10, np.random.rand(0, 40) * 10])

    def show(self):
        fill(255, 0, 0)
        rect(self.pos[0], self.pos[1], 10, 10)

    def clone(self):
        clone = Food()
        clone.pos = self.pos.copy()
        return clone
