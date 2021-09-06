class BaseDistributor:

    def InputParameters(self):
        return self

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

    def GetDistribution(self, sequence): 
        return sequence