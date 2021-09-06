from numpy import mean 

class Statistics:

    def GetExpectation(self, sequence):
        return mean(sequence)

    def GetDispersion(self, sequence, mx):
        t = sum([(item - mx) ** 2 for item in sequence])
        return t / len(sequence)