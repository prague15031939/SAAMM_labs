class StateMachine:

    def __init__(self, startState, p1, p2):
        self.state=startState
        self.p1=p1
        self.p2=p2
        self.P2000=0
        self.P1000=0
        self.P2010=0
        self.P1010=0
        self.P2011=0
        self.P1001=0
        self.P1011=0
        self.P2111=0
        self.P1111=0
        self.P2211=0
        self.P1211=0
        self.P0211=0
        self.Pbl=0
        self.Potk=0
        self.Q=0
        self.Loch=0
        self.Lc=0
        self.A=0
        self.K1=0
        self.K2=0


    def SwitchState(self, p1_cur, p2_cur):
        if self.state=="2000":
            self.state="1000"

        elif self.state=="1000":
            self.P1000+=1
            self.state="2010"
            self.Q+=1
            self.A+=1

        elif self.state=="2010":
            self.P2010+=1
            self.Q+=1
            self.A+=1
            self.Lc+=1
            self.K1+=1
            if p1_cur<=self.p1:
                self.state="1000"
            if p1_cur>self.p1:
                self.state="1010"

        elif self.state=="1010":
            self.P1010+=1
            self.Q+=1
            self.A+=1
            self.Lc+=1
            self.K1+=1
            if p1_cur<=self.p1:
                self.state="2010"
            if p1_cur>self.p1:
                self.state="2011"

        elif self.state=="2011":
            self.P2011+=1
            self.Q+=1
            self.A+=1
            self.Lc+=2
            self.K1+=1
            self.K2+=1
            if (p1_cur<=self.p1) and (p2_cur<=self.p2):
                self.state="1000"
            if (p1_cur>self.p1) and (p2_cur<=self.p2):
                self.state="1010"
            if (p1_cur<=self.p1) and (p2_cur>self.p2):
                self.state="1001"
            if (p1_cur>self.p1) and (p2_cur>self.p2):
                self.state="1011"

        elif self.state=="1001":
            self.P1001+=1
            self.Q+=1
            self.A+=1
            self.Lc+=1
            self.K2+=1
            if p2_cur<=self.p2:
                self.state="2010"
            if p2_cur>self.p2:
                self.state="2011"
        
        elif self.state=="1011":
            self.P1011+=1
            self.Q+=1
            self.A+=1
            self.Lc+=2
            self.K1+=1
            self.K2+=1
            if ((p1_cur<=self.p1) and (p2_cur>self.p2)) or (p1_cur>self.p1) and (p2_cur<=self.p2):
                self.state="2011"
            if (p1_cur<=self.p1) and (p2_cur<=self.p2):
                self.state="2010"
            if (p1_cur>self.p1) and (p2_cur>self.p2):
                self.state="2111"

        elif self.state=="2111":
            self.P2111+=1
            self.Q+=1
            self.A+=1
            self.Lc+=3
            self.Loch+=1
            self.K1+=1
            self.K2+=1
            if ((p1_cur<=self.p1) and (p2_cur>self.p2)) or (p1_cur>self.p1) and (p2_cur<=self.p2):
                self.state="1011"
            if (p1_cur<=self.p1) and (p2_cur<=self.p2):
                self.state="1010"
            if (p1_cur>self.p1) and (p2_cur>self.p2):
                self.state="1111"

        elif self.state=="1111":
            self.P1111+=1
            self.Q+=1
            self.A+=1
            self.Lc+=3
            self.Loch+=1
            self.K1+=1
            self.K2+=1
            if ((p1_cur<=self.p1) and (p2_cur>self.p2)) or (p1_cur>self.p1) and (p2_cur<=self.p2):
                self.state="2111"
            if (p1_cur<=self.p1) and (p2_cur<=self.p2):
                self.state="2011"
            if (p1_cur>self.p1) and (p2_cur>self.p2):
                self.state="2211"

        elif self.state=="2211":
            self.P2211+=1
            self.Q+=1
            self.A+=1
            self.Lc+=4
            self.Loch+=2
            self.K1+=1
            self.K2+=1
            if ((p1_cur<=self.p1) and (p2_cur>self.p2)) or (p1_cur>self.p1) and (p2_cur<=self.p2):
                self.state="1111"
            if (p1_cur<=self.p1) and (p2_cur<=self.p2):
                self.state="1011"
            if (p1_cur>self.p1) and (p2_cur>self.p2):
                self.state="1211"

        elif self.state=="1211":
            self.P1211+=1
            self.Q+=1
            self.A+=1
            self.Lc+=4
            self.Loch+=2
            self.K1+=1
            self.K2+=1
            if ((p1_cur<=self.p1) and (p2_cur>self.p2)) or (p1_cur>self.p1) and (p2_cur<=self.p2):
                self.state="2211"
            if (p1_cur<=self.p1) and (p2_cur<=self.p2):
                self.state="2111"
            if (p1_cur>self.p1) and (p2_cur>self.p2):
                self.state="0211"

        elif self.state=="0211":
            self.P0211+=1
            self.Q+=1
            self.Pbl+=1
            self.Lc+=4
            self.Loch+=2
            self.K1+=1
            self.K2+=1
            if ((p1_cur<=self.p1) and (p2_cur>self.p2)) or (p1_cur>self.p1) and (p2_cur<=self.p2):
                self.state="2211"
            if (p1_cur<=self.p1) and (p2_cur<=self.p2):
                self.state="2111"
            if (p1_cur>self.p1) and (p2_cur>self.p2):
                self.state="0211"


            