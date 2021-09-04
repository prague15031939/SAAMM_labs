class Lehmer:

    def __init__(self, multiplier, start, modulus):
        self.a = multiplier
        self.R = start
        self.m = modulus

        self.x = None
        self.__precision = 0.0001
        self.periodValue = None

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

    def GetSequenceOf(self, count):
        self.x = self.R
        return [self.GetNext() for i in range(count)]

    def GetNext(self):
        self.x = self.a * self.x % self.m
        return self.x / self.m

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

    def GetPeriod(self):
        testSequence = self.GetSequenceOf(10 ** 5)
        v = testSequence[-1]
        hits = [i for i, item in enumerate(testSequence) if abs(item - v) < self.__precision]
        return hits[1] - hits[0], hits[1]

