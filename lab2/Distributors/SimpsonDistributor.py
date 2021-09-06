from BaseDistributor import BaseDistributor
from random import randint

class SimpsonDistributor(BaseDistributor):

    def __init__(self):
        self.a = None
        self.b = None

    def InputParameters(self):
        self.a = float(input("a: "))
        self.b = float(input("b: "))
        return self

    def GetDistribution(self, sequence):
        for i, item in enumerate(sequence):
            sequence[i] = self.a / 2 + (self.b / 2 - self.a / 2) * item

        result = []
        for item in sequence:
            result.append(sequence[randint(0, len(sequence) - 1)] + sequence[randint(0, len(sequence) - 1)])
        return result