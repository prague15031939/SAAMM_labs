from BaseDistributor import BaseDistributor
from math import sqrt
from random import randint

class GaussDistributor(BaseDistributor):

    def __init__(self):
        self.expc = None
        self.mdev = None

    def InputParameters(self):
        self.expc = float(input("expc: "))
        self.mdev = float(input("mdev: "))
        return self

    def GetDistribution(self, sequence):
        result = []
        for item in sequence:
            R = sum([sequence[randint(0, len(sequence) - 1)] for i in range(5)])
            result.append(self.expc + self.mdev * sqrt(2) * (R - 3))
        return result