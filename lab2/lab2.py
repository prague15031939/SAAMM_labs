from Statistics import Statistics
from Lehmer import Lehmer
import matplotlib.pyplot as plt
import numpy as np

from Distributors.ExponentialDistributor import ExponentialDistributor
from Distributors.GammaDistributor import GammaDistributor
from Distributors.GaussDistributor import GaussDistributor
from Distributors.SimpsonDistributor import SimpsonDistributor
from Distributors.TriangleDistributor import TriangleDistributor
from Distributors.UniformDistributor import UniformDistributor

intervalAmount = 20

def main():
    startValue = 44293
    multiplier = 84589
    modulus = 217728

    print(f"\nLehmer generator parameters: R0 = {startValue}, a = {multiplier}, m = {modulus}")

    while True:

        generator = Lehmer(multiplier, startValue, modulus)
        sequence = generator.GetSequence()

        distributors = [UniformDistributor(), GaussDistributor(), ExponentialDistributor(), GammaDistributor(), TriangleDistributor(), SimpsonDistributor()]

        print(f"1 - Uniform, 2 - Gauss, 3 - Exponential, 4 - Gamma, 5 - Triangle, 6 - Simpson, 0 - exit")
        variant = int(input("choose distribution: "))
        if variant == 0:
            break
        
        sequence = distributors[variant - 1].InputParameters().GetDistribution(sequence)

        frequencies = generator.GetFrequencies(sequence, intervalAmount)[:intervalAmount]

        plt.bar([x + 1 / intervalAmount for x in np.arange(0, 1, 1 / intervalAmount)], frequencies, width = 1 / intervalAmount, edgecolor="black")
        plt.show()

        statistics = Statistics()
        expectation = statistics.GetExpectation(sequence)
        dispersion = statistics.GetDispersion(sequence, expectation)

        print(f"\nmath expectation: {expectation}")
        print(f"dispersion: {dispersion}")
        print(f"mean square deviation: {np.sqrt(dispersion)}\n")

if __name__ == "__main__":
    main()