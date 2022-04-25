import numpy as np
from matrix import Matrix


class NeuralNet:
    def __init__(self, inputs, hidden, output):
        self.iNodes = inputs
        self.hNodes = hidden
        self.oNodes = output

        self.whi = Matrix(self.hNodes, self.iNodes + 1)
        self.whh = Matrix(self.hNodes, self.hNodes + 1)
        self.woh = Matrix(self.oNodes, self.hNodes + 1)

        self.whi.randomize()
        self.whh.randomize()
        self.woh.randomize()

    def mutate(self, mutationRate):
        self.whi.mutate(mutationRate)
        self.whh.mutate(mutationRate)
        self.woh.mutate(mutationRate)

    def output(self, inputsArr):
        inputs = Matrix().singleColumnMatrixFromArray(inputsArr)
        inputBias = inputs.addBias()

        hiddenInputs = self.whi.dot(inputBias.m)

        hiddenOutputs = hiddenInputs.activate()

        hiddenOutputsBias = hiddenOutputs.addBias()

        hiddenInputs2 = self.whh.dot(hiddenOutputsBias.m)
        hiddenOutputs2 = hiddenInputs2.activate()
        hiddenOutputsBias2 = hiddenOutputs2.addBias()

        outputInputs = self.woh.dot(hiddenOutputsBias2.m)
        outputs = outputInputs.activate()

        print(outputs)
        return outputs.toArray()

    def crossover(self, partner):
        child = NeuralNet(self.iNodes, self.hNodes, self.oNodes)
        child.whi = self.whi.crossover(partner.whi)
        child.whh = self.whh.crossover(partner.whh)
        child.woh = self.woh.crossover(partner.woh)
        return child

    def clone(self):
        clone = NeuralNet(self.iNodes, self.hNodes, self.oNodes)
        clone.whi = self.whi.clone()
        clone.whh = self.whh.clone()
        clone.woh = self.woh.clone()
        return clone

    def NetToTable(self):
        whi = self.whi.toArray()
        whh = self.whh.toArray()
        woh = self.woh.toArray()

        t = np.array([whi, whh, woh], dtype=list)
        return t

    def TableToNet(self, t):
        self.whi.fromArray(t[0])
        self.whh.fromArray(t[1])
        self.woh.fromArray(t[2])
