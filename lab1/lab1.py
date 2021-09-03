from Statistics import Statistics
from Lehmer import Lehmer
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from Lehmer import Lehmer

# R0 = 44293
# a = 2117183648
# m = 4292917296

intervalAmount = 20

def main():
    startValue = 44293#int(input("R0: "))
    multiplier = 2117183648#int(input("a: "))
    modulus = 4292917296#int(input("m: "))

    generator = Lehmer(multiplier, startValue, modulus)
    sequence = generator.GetSequence()
    unsortedSequence = sequence.copy()
    frequencies = generator.GetFrequencies(sequence, 20)

    plt.bar([x + 1 / intervalAmount for x in np.arange(0, 1, 1 / intervalAmount)], frequencies, width = 1 / intervalAmount)
    plt.show()

    statistics = Statistics()
    expectation = statistics.GetExpectation(sequence)
    print(f"math expectation: {expectation}")

    dispersion = statistics.GetDispersion(sequence, expectation)
    print(f"dispersion: {dispersion}")

    print(f"mean square deviation: {np.sqrt(dispersion)}")

    manualCheckValue, check = statistics.ManualCheck(unsortedSequence)

    print(f"manual check is {manualCheckValue}, seeks to Pi/4 ({pi / 4}): {check}")
    

if __name__ == "__main__":
    main()