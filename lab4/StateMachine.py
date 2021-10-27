class StateMachine:

    def __init__(self, startState, po=0.5, p1=0.6, p2=0.6):
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
            if po:
                self.state = "000"
            if not po:
                self.state = "010"

        elif self.state == "010":
            self.P010 += 1
            if po and p1:
                self.state = "010"
            if (not po) and p1:
                self.state = "110"
            if po and (not p1):
                self.state = "001"
            if (not po) and (not p1):
                self.state = "011"

        elif self.state == "001":
            self.P001 += 1
            if po and (not p2):
                self.state = "000"
            if po and p2:
                self.state = "001"
            if (not po) and (not p2):
                self.state = "010"
            if (not po) and p2:
                self.state = "011"

        elif self.state == "110":
            self.P110 += 1
            if po and p1:
                self.state = "110"
            if po and (not p1):
                self.state = "011"
            if (not po) and p1:
                self.state = "210"
            if (not po) and (not p1):
                self.state = "111"

        elif self.state == "011":
            self.P011 += 1
            if (po and p1 and p2) or ((not po) and (not p1)):
                self.state = "011"
            elif po and p1 and (not p2):
                self.state = "010"
            elif po and not p1:
                self.state = "001"
            elif (not po) and p1 and (not p2):
                self.state = "110"
            elif (not po) and p1 and p2:
                self.state = "111"

        elif self.state == "111":
            self.P111 += 1
            if (po and p1 and p2) or ((not po) and (not p1)):
                self.state = "111"
            if po and (not p1):
                self.state = "011"
            if po and p1 and (not p2):
                self.state = "110"
            if (not po) and p1 and p2:
                self.state = "211"
            if (not po) and p1 and (not p2):
                self.state = "210"

        elif self.state == "211":
            self.P211 += 1 
            if (po and p1 and p2) or ((not po) and (not p1) and (not p2)) or (not po) and p2:
                self.state = "211"
            if po and (not p1):
                self.state = "111"
            if p1 and (not p2):
                self.state = "210"

        elif self.state == "210":
            self.P210 += 1 
            if po and p1 or (not po) and p1:
                self.state = "210"
            if po and (not p1):
                self.state = "111"
            if (not po) and (not p1):
                self.state = "211"