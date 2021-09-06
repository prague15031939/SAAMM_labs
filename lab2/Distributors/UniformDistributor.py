from BaseDistributor import BaseDistributor

class UniformDistributor(BaseDistributor):

    def __init__(self):
        self.a = None
        self.b = None
    
    def InputParameters(self):
        self.a = float(input("a: "))
        self.b = float(input("b: "))
        return self

    def GetDistribution(self, sequence):
        return [self.a + (self.b - self.a) * item for item in sequence]