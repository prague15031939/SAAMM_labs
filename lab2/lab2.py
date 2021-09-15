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
    startValue = 995053
    multiplier = 550000
    modulus = 1000002

    print(f"\nLehmer generator parameters: R0 = {startValue}, a = {multiplier}, m = {modulus}")

    while True:

        generator = Lehmer(multiplier, startValue, modulus)
        sequence = generator.GetSequenceOf(5 * (10 ** 5))

        distributors = [UniformDistributor(), GaussDistributor(), ExponentialDistributor(), GammaDistributor(), TriangleDistributor(), SimpsonDistributor()]

        print(f"1 - Uniform, 2 - Gauss, 3 - Exponential, 4 - Gamma, 5 - Triangle, 6 - Simpson, 0 - exit")
        variant = int(input("choose distribution: "))
        if variant == 0:
            break
        
        sequence = distributors[variant - 1].InputParameters().GetDistribution(sequence)

        frequencies, xMin, xMax = generator.GetFrequencies(sequence, intervalAmount)

        delta = (xMax - xMin) / intervalAmount

        plt.bar([x + delta for x in np.arange(xMin, xMax, delta).tolist()][:intervalAmount], frequencies[:intervalAmount], width = delta, edgecolor="black")
        plt.show()

        statistics = Statistics()
        expectation = statistics.GetExpectation(sequence)
        dispersion = statistics.GetDispersion(sequence, expectation)

        print(f"\nmath expectation: {expectation}")
        print(f"dispersion: {dispersion}")
        print(f"mean square deviation: {np.sqrt(dispersion)}\n")

if __name__ == "__main__":
    main()