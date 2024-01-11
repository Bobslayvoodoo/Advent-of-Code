Workflows = dict()


class Workflow():
    def __init__(self,Name,Conditions):
        self.Name = Name
        Workflows[Name] = self
        self.RawConditions = Conditions

    def ProcessConditions(self):
        Conditions = self.RawConditions.split(",")
        self.Conditions = []
        for Condition in Conditions:
            if ":" in Condition:
                Stuff = Condition.split(":")
                if Stuff[1] in Workflows.keys():
                    self.Conditions.append((Stuff[0],Workflows[Stuff[1]]))
                else:
                    self.Conditions.append((Stuff[0],Stuff[1]))
            else:
                if Condition in Workflows.keys():
                    self.Conditions.append(("True",Workflows[Condition]))
                else:
                    self.Conditions.append(("True",Condition))

                

    def ProcessPart(self,CurrentPart):
        for Condition,Destination in self.Conditions:
            x = CurrentPart.x
            m = CurrentPart.m
            a = CurrentPart.a
            s = CurrentPart.s
            if eval(Condition):
                return Destination


class Part():
    def __init__(self,x,m,a,s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.Sum = x+m+a+s
        self.CurrentWorkFlow = Workflows["in"]
    def EvaluatePart(self):
        while type(self.CurrentWorkFlow) != str:
            #print(self.CurrentWorkFlow.Name)
            self.CurrentWorkFlow = self.CurrentWorkFlow.ProcessPart(self)
        if self.CurrentWorkFlow == "A":
            return self.Sum
        else:
            return 0


with open("Input.txt") as File:
    Total = 0
    for Line in File:
        if Line == "\n":
            break
        Line = Line.strip().split("{")
        Name = Line[0]
        Cs = Line[1][:-1]
        Workflow(Name,Cs)

    for W in Workflows.values():
        W.ProcessConditions()

    for Line in File:
        Line = Line.strip()[1:-1].split(",")
        x = int(Line[0].split("=")[1])
        m = int(Line[1].split("=")[1])
        a = int(Line[2].split("=")[1])
        s = int(Line[3].split("=")[1])
        NewPart = Part(x,m,a,s)
        Total += NewPart.EvaluatePart()
    print(Total)


