from .BaseDistributor import BaseDistributor
from random import randint

class TriangleDistributor(BaseDistributor):

    def __init__(self):
        self.a = None
        self.b = None

    def InputParameters(self):
        self.a = float(input("a: "))
        self.b = float(input("b: "))
        return self

    def GetDistribution(self, sequence):
        result = []
        for item in sequence:
            R = max([sequence[randint(0, len(sequence) - 1)], sequence[randint(0, len(sequence) - 1)]])
            result.append(self.a + (self.b - self.a) * R)
        return result