from Statistics import Statistics
from Lehmer import Lehmer
import matplotlib.pyplot as plt
import numpy as np
from math import pi

intervalAmount = 20

def main():
    variant = input("\n0 - max uniformity\n1 - period > 50000\nother - own values\n> ")
    if int(variant) == 0:
        startValue = 44293
        multiplier = 84589
        modulus = 217728
    elif int(variant) == 1:
        startValue = 20823
        multiplier = 4095
        modulus = 2147483647
    else:
        startValue = int(input("R0: "))
        multiplier = int(input("a: "))
        modulus = int(input("m: "))

    generator = Lehmer(multiplier, startValue, modulus)
    sequence = generator.GetSequence()
    unsortedSequence = sequence.copy()
    frequencies = generator.GetFrequencies(sequence, 20)

    plt.bar([x + 1 / intervalAmount for x in np.arange(0, 1, 1 / intervalAmount)], frequencies, width = 1 / intervalAmount, edgecolor="black")
    plt.show()

    statistics = Statistics()
    expectation = statistics.GetExpectation(sequence)
    dispersion = statistics.GetDispersion(sequence, expectation)

    manualCheckValue, check = statistics.ManualCheck(unsortedSequence)
    period, aperiodicLenght = generator.GetPeriod()

    print(f"\nmath expectation: {expectation}")
    print(f"dispersion: {dispersion}")
    print(f"mean square deviation: {np.sqrt(dispersion)}")
    print(f"manual check: {manualCheckValue}, seeks to Pi/4 ({pi / 4}): {check}")
    print(f"sequence period: {period}, aperiodic length: {aperiodicLenght}\n")

if __name__ == "__main__":
    main()