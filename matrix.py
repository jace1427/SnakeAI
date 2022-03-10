import numpy as np


class Matrix():
    def __init__(self, rows=0, cols=0, m=None):
        self.r = rows
        self.c = cols
        if m is None:
            self.m = np.zeros((self.r, self.c))
        else:
            self.m = m

    def __repr__(self):
        return self.m.__repr__()

    def __str__(self):
        return self.m.__str__()

    def multiply_scalar(self, n):
        self.m = np.multiply(self.m, n)

    def dot(self, n):
        new = np.dot(self.m, n)
        return Matrix(new.shape[0], new.shape[1], new)

    def randomize(self):
        self.m = np.random.rand(self.r, self.c)
        self.m = np.multiply(self.m, 2)
        self.m -= 1

    def add_scalar(self, n):
        self.m = np.add(self.m, n)

    def add(self, n):
        return np.add(self.m, n)

    def subtract(self, n):
        return np.subtract(self.m, n)

    def multiply_matrix(self, n):
        return np.multiply(self.m, n)

    def transpose(self):
        return np.transpose(self.m)

    def singleColumnMatrixFromArray(self, arr):
        ret = np.array([arr]).T
        return Matrix(ret.shape[0], ret.shape[1], ret)

    def fromArray(self, arr):
        self.m = np.array(arr).reshape(self.r, self.c)

    def toArray(self):
        return self.m.flatten()

    def addBias(self):
        n = np.append(self.m[:, 0], 1)
        n = np.array([n]).T
        return Matrix(n.shape[0], n.shape[1], n)

    def sigmoid(self, x):
        return 1 / (1 + pow(np.e, -x))

    def activate(self):
        n = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                n.m[i][j] = self.sigmoid(self.m[i][j])
        return n

    def sigmoidDerived(self):
        n = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                n.m[i][j] = (self.m[i][j] * (1 - self.m[i][j]))
        return n

    def removeBottomlayer(self):
        n = Matrix(self.r - 1, self.c)
        for i in range(n.r):
            for j in range(self.c):
                n.m[i][j] = self.m[i][j]
        return n

    def mutate(self, mutationRate):
        for i in range(self.r):
            for j in range(self.c):
                rand = np.random.rand()
                if rand < mutationRate:
                    self.m[i][j] += np.random.normal(0, 1)

                    if self.m[i][j] > 1:
                        self.m[i][j] = 1
                    if self.m[i][j] < -1:
                        self.m[i][j] = -1

    def crossover(self, partner):
        child = Matrix(self.r, self.c)

        rr = np.floor(np.random.rand() * self.r)
        rc = np.floor(np.random.rand() * self.c)

        for i in range(self.r):
            for j in range(self.c):
                if (i < rr) or (i == rr and j <= rc):
                    child.m[i][j] = self.m[i][j]
                else:
                    child.m[i][j] = partner[i][j]
        return child

    def clone(self):
        return self.m.copy()
