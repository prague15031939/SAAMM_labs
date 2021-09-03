from numpy import mean 
from math import pi

class Statistics:

    def GetExpectation(self, sequence):
        return mean(sequence)

    def GetDispersion(self, sequence, mx):
        t = sum([(item - mx) ** 2 for item in sequence])
        return t / len(sequence)

    def ManualCheck(self, sequence):
        n = 2
        pairs = [sequence[i * n:(i + 1) * n] for i in range((len(sequence) + n - 1) // n )]
        if len(pairs[len(pairs) - 1]) == 1:
            pairs.pop()

        k = len([pair for pair in pairs if pair[0] ** 2 + pair[1] ** 2 < 1])
        target = 2 * k / len(sequence)

        return target, abs(target - pi / 4) < 0.05