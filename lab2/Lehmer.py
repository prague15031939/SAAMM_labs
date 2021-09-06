from Distributors.BaseDistributor import BaseDistributor

class Lehmer(BaseDistributor):

    def __init__(self, multiplier, start, modulus):
        self.a = multiplier
        self.R = start
        self.m = modulus

        self.x = None
        self.__precision = 0.0001

    def GetSequence(self):
        self.x = self.R

        sequence = [self.GetNext()]
        temp = self.GetNext()
        while all(abs(item - temp) > self.__precision for item in sequence):
            sequence.append(temp)
            temp = self.GetNext() 
        else:
            self.periodValue = temp
        return sequence

    def GetNext(self):
        self.x = self.a * self.x % self.m
        return self.x / self.m



