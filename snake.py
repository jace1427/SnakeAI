import numpy as np
from NN import NeuralNet


class Snake():
    def __init__(self):
        self.length = 4
        self.pos = np.array([250, 250])
        self.tailpos = np.array([[250, 250]])
        self.vel = np.array([10, 0])  # x, y
        self.brain = NeuralNet(24, 18, 4)
        self.vision = np.zeros(24)
        self.decision = np.zeros(4)
        self.lifetime = 0
        self.fitness = 0
        self.leftTolive = 200
        self.growCount = 0
        self.alive = True
        self.test = True

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

    def move(self, foodPos):
        self.mutate(0.01)
        self.look(foodPos)
        self.setVelocity()
        print(self.pos, self.vel)
        self.lifetime += 1
        self.leftTolive -= 1
        eat = False

        if self.leftTolive < 0:
            self.alive = False

        if self.goingToDie(self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]):
            self.alive = False

        if self.pos[0] + self.vel[0] == foodPos[0] and self.pos[1] + self.vel[1] == foodPos[1]:
            eat = True
            self.leftTolive += 100
            if self.test:
                self.growCount += 4
            else:
                self.growCount += 1

        if self.growCount > 0:
            self.growCount -= 1
            self.grow()
        else:
            for i in range(self.tailpos.shape[0] - 1):
                self.tailpos[i] = self.tailpos[i + 1]
            self.tailpos[self.tailpos.shape[0] - 2] = [self.pos[0], self.pos[1]]

        self.pos = np.add(self.pos, self.vel)
        return eat

    def grow(self):
        temp = self.pos.copy()
        self.tailpos.append(temp)

    def goingToDie(self, x, y):
        if (x < 0 or y < 0 or x >= 500 or y >= 500):
            return True

        return self.isOnTail(x, y)

    def isOnTail(self, x, y):
        for i in self.tailpos:
            if x == i[0] and y == i[1]:
                return True
        return False

    def look(self, foodPos):
        vision = []
        dirs = [[-10, 0], [-10, -10], [0, -10], [10, -10],
                [10, 0], [10, 10], [0, 10], [-10, 10]]
        for i in range(8):
            temp = self.lookInDirection(dirs[i], foodPos)
            vision.append(temp[0])
            vision.append(temp[1])
            vision.append(temp[2])
        self.vision = vision

    def lookInDirection(self, direction, foodPos):
        visionInDirection = [0, 0, 0]
        foodIsFound = False
        tailIsFound = False
        pos = self.pos.copy()
        distance = 0
        pos += direction
        distance += 1

        while not (pos[0] < 0 or pos[1] < 0 or pos[0] >= 500 or pos[1] >= 500):
            if not (foodIsFound and pos[0] == foodPos[0] and pos[1] == foodPos[1]):
                visionInDirection[0] = 1
                foodIsFound = True
            if not (tailIsFound and self.isOnTail(pos[0], pos[1])):
                visionInDirection[1] = 1 / distance
                tailIsFound = True
            pos += direction
            distance += 1

        visionInDirection[2] = 1 / distance

        return visionInDirection

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

    def clone(self):
        clone = Snake()
        clone.brain = self.brain.clone()
        clone.alive = True
        return clone

    def saveSnake(self, snakeNo, score, popID):
        snakeStats = f"Top Score,PopulationID\n{score},{popID}"
        save(snakeStats, "data/SnakeStats" + snakeNo + ".csv")
        save(self.brain.NetToTable, "data/SnakeStats" + snakeNo + ".csv")

    def loadSnake(self, snakeNo):
        load = Snake()
        t = loadTable("data/Snake" + snakeNo + ".csv")
        load.brain.TableToNet(t)
        return load