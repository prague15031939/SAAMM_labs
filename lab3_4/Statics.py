class Statics:

    def __init__(self, N, T):
        self.N = N
        self.T=T

    def CalculateStateProbability(self, stateMachine):
        P2000=stateMachine.P2000/self.N
        P1000=stateMachine.P1000/self.N
        P2010=stateMachine.P2010/self.N
        P1010=stateMachine.P1010/self.N
        P2011=stateMachine.P2011/self.N
        P1001=stateMachine.P1001/self.N
        P1011=stateMachine.P1011/self.N
        P2111=stateMachine.P2111/self.N
        P1111=stateMachine.P1111/self.N
        P2211=stateMachine.P2211/self.N
        P1211=stateMachine.P1211/self.N
        P0211=stateMachine.P0211/self.N
        return P2000,P1000,P2010,P1010,P2011,P1001,P1011,P2111,P1111,P2211,P1211,P0211


    def CalculateStatics(self, stateMachine):
        Pbl=stateMachine.Pbl/self.N
        Potk=stateMachine.Potk/self.N
        Q=stateMachine.Q/self.N
        Loch=stateMachine.Loch/self.N
        Lc=stateMachine.Lc/self.N
        A=1/self.T*(stateMachine.A/self.N)
        K1=stateMachine.K1/self.N
        K2=stateMachine.K2/self.N
        Woch=Loch/A
        Wc=Lc/A
        return Pbl,Potk,Q,Loch,Lc,A,Woch,Wc,K1,K2
