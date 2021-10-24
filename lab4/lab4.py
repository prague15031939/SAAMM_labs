from StateMachine import StateMachine
from Lehmer import Lehmer
import numpy as np

startValue = 995053
multiplier = 550000
modulus = 1000002
startState = "000"
N = 1000000
T = 2

def main():
    #po = float(input("po: "))
    #p1 = float(input("p1: "))
    #p2 = float(input("p2: "))

    generator = Lehmer(multiplier, startValue, modulus)
    stateMachine = StateMachine(startState)

    for i in range(N):
        po = generator.GetNext()
        p1 = generator.GetNext()
        p2 = generator.GetNext()
        stateMachine.SwitchState(po, p1, p2)

    print(f"P000: {stateMachine.P000 / N}")
    print(f"P010: {stateMachine.P010 / N}")
    print(f"P001: {stateMachine.P001 / N}")
    print(f"P110: {stateMachine.P110 / N}")
    print(f"P011: {stateMachine.P011 / N}")
    print(f"P111: {stateMachine.P111 / N}")
    print(f"P211: {stateMachine.P211 / N}")
    print(f"P210: {stateMachine.P210 / N}")

    print(f"sum: {stateMachine.P000 / N + stateMachine.P010 / N + stateMachine.P001 / N + stateMachine.P110 / N + stateMachine.P011 / N + stateMachine.P111 / N + stateMachine.P210 / N + stateMachine.P211 / N}")

    #print(f"Вероятность отказа (Potk): {Potk}")
    #print(f"Вероятность блокировки (Pbl): {Pbl}")
    #print(f"Средняя длина очереди (Loch): {Loch}")
    #print(f"Среднее число заявок, находящихся в системе (Lc): {Lc}")
    #print(f"Относительная пропускная способность (Q): {Q}")
    #print(f"Абсолютная пропускная способность (A): {A}")
    #print(f"Среднее время пребывания заявки в очереди (Woch): {Woch}")
    #print(f"Среднее время пребывания заявки в системе (Wc): {Wc}")
    #print(f"Коэффициент загрузки канала (K1): {K1}")
    #print(f"Коэффициент загрузки канала (K2): {K2}")


if __name__ == "__main__":
    main()