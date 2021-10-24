class StateMachine:

    def __init__(self, startState, po=0.5, p1=0.4, p2=0.4):
        self.state = startState
        self.po = po
        self.p1 = p1
        self.p2 = p2

        self.P000 = 0
        self.P001 = 0
        self.P010 = 0
        self.P110 = 0
        self.P011 = 0
        self.P111 = 0
        self.P211 = 0
        self.P210 = 0

        self.Pbl = 0
        self.Potk = 0
        self.Q = 0
        self.Loch = 0
        self.Lc = 0
        self.A = 0
        self.K1 = 0
        self.K2 = 0

    def SwitchState(self, po, p1, p2):
        if self.state == "000":
            self.P000 += 1
            if po <= self.po:
                self.state = "000"
            if 1 - po <= 1 - self.po:
                self.state = "010"

        elif self.state == "010":
            self.P010 += 1
            if (po <= self.po) and (p1 <= self.p1):
                self.state = "010"
            if ((1 - po) <= (1 - self.po)) and (p1 <= self.p1):
                self.state = "110"
            if (po <= self.po) and ((1 - p1) <= (1 - self.p1)):
                self.state = "001"
            if ((1 - po) <= (1 - self.po)) and ((1 - p1) <= (1 - self.p1)):
                self.state = "011"

        elif self.state == "001":
            self.P001 += 1
            if (po <= self.po) and (1 - p2 <= 1 - self.p2):
                self.state = "000"
            if (po <= self.po) and (p2 <= self.p2):
                self.state = "001"
            if (1 - po <= 1 - self.po) and (1 - p2 <= 1 - self.p2):
                self.state = "010"
            if (1 - po <= 1 - self.po) and (p2 <= self.p2):
                self.state = "011"

        elif self.state == "110":
            self.P110 += 1
            if (po <= self.po) and (p1 <= self.p1):
                self.state = "110"
            if (po <= self.po) and (1 - p1 <= 1 - self.p1):
                self.state = "011"
            if (1 - po <= 1 - self.po) and (p1 <= self.p1):
                self.state = "210"
            if (1 - po <= 1 - self.po) and (1 - p1 <= 1 - self.p1):
                self.state = "111"

        elif self.state == "011":
            self.P011 += 1
            i = 0
            if ((po <= self.po) and (p1 <= self.p1) and (p2 <= self.p2)) or ((1 - po <= 1 - self.po) and (1 - p1 <= 1 - self.p1)):
                self.state = "011"
                i +=1
            elif (po <= self.po) and (p1 <= self.p1) and (1 - p2 <= 1 - self.p2):
                self.state = "010"
                i += 1
            elif (po <= self.po) and (p1 <= self.p1):
                self.state = "001"
                i += 1
            elif (1 - po <= 1 - self.po) and (p1 <= self.p1) and (1 - p2 <= 1 - self.p2):
                self.state = "110"
                i += 1
            elif (1 - po <= 1 - self.po) and (p1 <= self.p1):
                self.state = "111"
                i +=1
            #if (i != 1):
             #   print(self.state)

        elif self.state == "111":
            self.P111 += 1
            if ((po <= self.po) and (p1 <= self.p1) and (p2 <= self.p2)) or ((1 - po <= 1 - self.po) and (1 - p1 <= 1 - self.p1)):
                self.state = "111"
            if (po <= self.po) and (1 - p1 <= 1 - self.p1):
                self.state = "011"
            if (po <= self.po) and (p1 <= self.p1) and (1 - p2 <= 1 - self.p2):
                self.state = "110"
            if (1 - po <= 1 - self.po) and (p1 <= self.p1) and (p2 <= self.p2):
                self.state = "211"
            if (1 - po <= 1 - self.po) and (p1 <= self.p1) and (1 - p2 <= 1 - self.p2):
                self.state = "210"

        elif self.state == "211":
            self.P211 += 1 
            i = 0
            if ((po <= self.po) and (p1 <= self.p1) and (p2 <= self.p2)) or ((1 - po <= 1 - self.po) and (1 - p1 <= 1 - self.p1) and (1 - p2 <= 1 - self.p2)):
                self.state = "211"
                i += 1
            if (po <= self.po) and (1 - p1 <= 1 - self.p1):
                self.state = "111"
                i += 1
            if (po <= self.po) and (p1 <= self.p1) and (1 - p2 <= 1 - self.p2):
                self.state = "210"
                i += 1
            #if (i != 1):
             #   print(self.state)

        elif self.state == "210":
            self.P210 += 1 
            i = 0
            if (po <= self.po) and (p1 <= self.p1):
                self.state = "210"
                i += 1
            if (po <= self.po) and (1 - p1 <= 1 - self.p1):
                self.state = "111"
                i += 1
            if (1 - po <= 1 - self.po) and (1 - p1 <= 1 - self.p1):
                self.state = "211"
                i += 1
            #if (i != 1):
             #  print(self.state, po, p1)