import numpy as np
from NN import NeuralNet
from food import Food


class Snake():
    def __init__(self):
        self.length = 4
        self.pos = np.array([100, 50])
        self.tailpos = np.array([[90, 50], [80, 50], [70, 50]])
        self.vel = np.array([10, 0])  # x, y
        self.food = Food()
        self.brain = NeuralNet(24, 18, 4)
        self.vision = np.zeros(24)
        self.decision = np.zeros(4)
        self.lifetime = 0
        self.fitness = 0
        self.leftTolive = 200
        self.growCount = 0
        self.alive = True
        self.test = False

    def mutate(self, mr):
        self.brain.mutate(mr)

    def setVelocity(self):
        self.decision = self.brain.output(self.vision)
        maxInd = np.argmax(self.decision)

        if maxInd == 0:
            self.vel[0] = -10
            self.vel[1] = 0
        if maxInd == 1:
            self.vel[0] = 0
            self.vel[1] = -10
        if maxInd == 2:
            self.vel[0] = 10
            self.vel[1] = 0
        else:
            self.vel[0] = 0
            self.vel[1] = 10

    def move(self):
        self.lifetime += 1
        self.leftTolive -= 1

        if self.leftTolive < 0:
            self.alive = False

        if self.goingToDie(self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]):
            self.alive = False

        if self.pos[0] + self.vel[0] == self.food.pos[0] and self.pos[1] + self.vel[1] == self.food.pos[1]:
            self.eat()

        if self.growCount > 0:
            self.growCount -= 1
            self.grow()
        else:
            for i in range(self.tailpos.shape[0] - 1):
                self.tailpos[i] = self.tailpos[i + 1]
            self.tailpos[self.tailpos.shape[0] - 2] = [self.pos[0], self.pos[1]]

        self.pos = np.add(self.pos, self.vel)

    def eat(self):
        food = Food()

        while [food.pos[0], food.pos[1]] in self.tailpos:
            food = Food()

        self.leftTolive += 100

        if self.test:
            self.growCount += 4
        else:
            self.growCount += 1

    def show(self):
        fill(255)
        stroke(0)
        for i in self.tailpos:
            rect(i[0], i[1])
        rect(self.pos[0], self.pos[1])
        food.show()

    def grow(self):
        temp = self.pos.copy()
        self.tailpos.append(temp)

    def goingToDie(self, x, y):
        if (x < 400 or y < 0 or x >= 800 or y >= 400):
            return True

        return self.isOnTail(x, y)

    def isOnTail(self, x, y):
        for i in self.tailpos:
            if x == i[0] and y == i[1]:
                return True
        return False

    def calcFitness(self):
        if (self.length < 10):
            self.fitness = np.floor(self.lifetime * self.lifetime * 2**np.floor(self.length))
        else:
            self.fitness = self.lifetime * self.lifetime
            self.fitness *= 2**10
            self.fitness *= self.length - 9

    def crossover(self, partner):
        child = Snake()
        child.brain = self.brain.crossover(partner.brain)
        return child

    def saveSnake(snakeNo, score, popID):
        pass

if __name__ == '__main__':
    s = Snake()
    s.move()
