import numpy as np
import matplotlib.pyplot as plt


class GridWorld(object):
    def __init__(self, m, n, magicSquares):
        self.grid = np.zeros((m, n))
        self.m = m
        self.n = n
        self.stateSpace = [i for i in range(self.m * self.n)]
        self.stateSpace.remove(self.m * self.n - 1)
        self.stateSpacePlus = [i for i in range(self.m * self.n)]
        self.actionSpace = {'U': -self.m, 'D': self.m, 'L': -1, 'R': 1}
        self.possibleActions = ['U', 'D', 'L', 'R']
        self.addMagicSquares(magicSquares)
        self.agentPosition = 0

    def addMagicSquares(self, magicSqares):
        self.magicSquares = magicSqares
        i = 2
        for square in magicSqares:
            x = square // self.m
            y = square % self.n
            self.grid[x][y] = i
            i += 1