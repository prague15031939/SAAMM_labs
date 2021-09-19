from StateMachine import StateMachine
from Lehmer import Lehmer
from Statics import Statics
import numpy as np

startValue = 995053
multiplier = 550000
modulus = 1000002
startState="2000"
N=1000000
T=2

def main():
    p1=float(input("p1: "))
    p2=float(input("p2: "))

    generator = Lehmer(multiplier, startValue, modulus)
    stateMachine = StateMachine(startState,p1,p2)

    for i in range(N):
        p1_cur=generator.GetNext()
        p2_cur=generator.GetNext()
        stateMachine.SwitchState(p1_cur,p2_cur)

    statics=Statics(N,T)

    P2000,P1000,P2010,P1010,P2011,P1001,P1011,P2111,P1111,P2211,P1211,P0211=statics.CalculateStateProbability(stateMachine)
    Pbl,Potk,Q,Loch,Lc,A,Woch,Wc,K1,K2=statics.CalculateStatics(stateMachine)

    print(f"P2000: {P2000}")
    print(f"P1000: {P1000}")
    print(f"P2010: {P2010}")
    print(f"P1010: {P1010}")
    print(f"P2011: {P2011}")
    print(f"P1001: {P1001}")
    print(f"P1011: {P1011}")
    print(f"P2111: {P2111}")
    print(f"P1111: {P1111}")
    print(f"P2211: {P2211}")
    print(f"P1211: {P1211}")
    print(f"P0211: {P0211}")

    print(f"Вероятность отказа (Potk): {Potk}")
    print(f"Вероятность блокировки (Pbl): {Pbl}")
    print(f"Средняя длина очереди (Loch): {Loch}")
    print(f"Среднее число заявок, находящихся в системе (Lc): {Lc}")
    print(f"Относительная пропускная способность (Q): {Q}")
    print(f"Абсолютная пропускная способность (A): {A}")
    print(f"Среднее время пребывания заявки в очереди (Woch): {Woch}")
    print(f"Среднее время пребывания заявки в системе (Wc): {Wc}")
    print(f"Коэффициент загрузки канала (K1): {K1}")
    print(f"Коэффициент загрузки канала (K2): {K2}")

if __name__ == "__main__":
    main()