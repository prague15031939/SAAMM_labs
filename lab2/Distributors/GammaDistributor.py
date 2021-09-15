from .BaseDistributor import BaseDistributor
from math import floor, log
from random import randint
from numpy import prod

class GammaDistributor(BaseDistributor):

    def __init__(self):
        self.lmbd = None
        self.eta = None

    def InputParameters(self):
        self.lmbd = float(input("lambda: "))
        self.eta = float(input("eta: "))
        return self

    def GetDistribution(self, sequence):
        result = []
        for item in sequence:
            R = prod([sequence[randint(0, len(sequence) - 1)] for i in range(floor(self.eta))])
            result.append(-log(R) / self.lmbd)
        return result