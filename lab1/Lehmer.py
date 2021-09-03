from typing import Sequence


class Lehmer:

    def __init__(self, multiplier, start, modulus):
        self.a = multiplier
        self.R = start
        self.m = modulus

    def GetSequence(self):
        sequence = [self.GetNext()]
        temp = self.GetNext()
        while all(abs(item - temp) > 0.0001 for item in sequence):
            sequence.append(temp)
            temp = self.GetNext() 
        return sequence

    def GetNext(self):
        self.R = self.a * self.R % self.m
        return  self.R / self.m

    def GetFrequencies(self, sequence, intervalAmount):
        sequence.sort()

        sequenceLength = len(sequence)
        xMax = max(sequence)
        xMin = min(sequence)
        xRange = xMax - xMin
        intervalLength = xRange / intervalAmount

        frequencies = []
        intervalBegin = xMin
        while intervalBegin < xMax:
            hitNumber = len([value for value in sequence if intervalBegin <= value <= intervalBegin + intervalLength])
            intervalBegin += intervalLength
            frequencies.append(hitNumber / sequenceLength)
        
        return frequencies

