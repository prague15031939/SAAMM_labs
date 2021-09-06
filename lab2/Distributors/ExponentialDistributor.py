from BaseDistributor import BaseDistributor
from math import log

class ExponentialDistributor(BaseDistributor):

    def __init__(self):
        self.lmbd = None

    def InputParameters(self):
        self.lmbd = float(input("lambda: "))
        return self

    def GetDistribution(self, sequence):
        return [abs(log(item) / self.lmbd) for item in sequence]