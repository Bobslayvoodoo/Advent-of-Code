Circuit = {}
PulseQueue = []
PulseTotals = [0,0]
class Module():
    def __init__(self,line):
        line = line.strip().split(">")
        self.__BackwardConnections = []
        
        self.CurrentPulse = 0
        self.__RawConnections = line[1]
        self.Name = line[0][:-2]
        if line[0][0] == "%":
            self.Name = self.Name[1:]
            self.__Type = "Flip-Flop"
            self.__Memory = 0
        elif line[0][0] == "&":
            self.Name = self.Name[1:]
            self.__Type = "Conjunction"
        elif line[0][:-2] == "broadcaster":
            self.__Type = "Broadcaster"
        else:
            self.__Type = "Nothing"
            
        Circuit[self.Name] = self

    def AddBackwardConnection(self,ModuleObject):
        self.__BackwardConnections.append(ModuleObject)

    def ConnectConnections(self):
        self.__ForwardConnections = []
        for M in self.__RawConnections.strip().split(","):
            Name = M.strip()
            if Name in Circuit.keys():
                M = Circuit[Name]
                M.AddBackwardConnection(self)
                self.__ForwardConnections.append(M)
            else:
                self.__ForwardConnections.append("output")

    def ProccessPulse(self,Pulse=None,Starter=None):
        
        if self.__Type == "Broadcaster":
            if Pulse == 0:
                self.CurrentPulse = Pulse
            else:
                self.CurrentPulse = Starter.CurrentPulse
        elif self.__Type == "Flip-Flop":
            if Starter.CurrentPulse == 0:
                if self.__Memory == 0:
                    self.__Memory = 1
                    self.CurrentPulse = 1
                elif self.__Memory == 1:
                    self.__Memory = 0
                    self.CurrentPulse = 0
            else:
                return
        elif self.__Type == "Conjunction":
            memory = []
            for Connection in self.__BackwardConnections:
                memory.append(Connection.CurrentPulse)
            if len(set(memory)) == 1 and memory[0] == 1:
                self.CurrentPulse = 0
            else:
                self.CurrentPulse = 1
        for Connection in self.__ForwardConnections:
            
            PulseTotals[self.CurrentPulse] += 1
            if type(Connection) == Module:
                #print(f"{self.Name} -{self.CurrentPulse}-> {Connection.Name} ")
                PulseQueue.append((self,Connection))
            else:
                #print(f"{self.Name} -{self.CurrentPulse}-> Output ")
                pass
            


with open("Input.txt") as File:
    for Line in File:
        Module(Line)
    for M in Circuit.values():
        M.ConnectConnections()

ButtonPresses = 1000
Presses = 0
Serials = []
PulseTotalsHistory = []
while True:
    if len(PulseQueue) == 0:
        if Presses >= ButtonPresses:
            break
        Serial = []
        for M in Circuit.values():
            Serial.append(str(M.CurrentPulse))
        Serial = "".join(Serial)
        if Serial in Serials:
            PreviousNum = Serials.index(Serial)
            Difference = Presses - PreviousNum
            PulseDifferences = (PulseTotals[0]-PulseTotalsHistory[PreviousNum][0],PulseTotals[1]-PulseTotalsHistory[PreviousNum][1])
            JumpLocation = int(((ButtonPresses//Difference)-1) * Difference)
            JumpDistance = JumpLocation - Presses
            JumpDistance = (JumpDistance//Difference) * Difference
            JumpLocation = Presses + JumpDistance
            if JumpDistance > 0 and JumpLocation<ButtonPresses:
                PulseTotals = [PulseTotals[0]+((JumpDistance//Difference)*PulseDifferences[0]),PulseTotals[1]+((JumpDistance//Difference)*PulseDifferences[1])]
                Presses = JumpLocation
                Serials = []
                PulseTotalsHistory = []
        else:
            Serials.append(Serial)
            PulseTotalsHistory.append(tuple(PulseTotals))
        
        PulseTotals[0] += 1
        Presses += 1
        #print("------------ Button Press ------------")
        Circuit["broadcaster"].ProccessPulse(Pulse=0)
    else:
        M = PulseQueue.pop(0)
        M[1].ProccessPulse(Starter=M[0])

print(PulseTotals)
print(PulseTotals[0] * PulseTotals[1])
                
                
