
        
def FallUp(Platform):
    LastGaps = []
    Height = len(Platform)
    for Y in range(Height):
        for X in range(len(Platform[0])):
            Current = Platform[Y][X]
            if len(LastGaps) <= X:
                LastGaps.append(0)
            if Current == "O":
                if LastGaps[X] < Y:
                    NewY = LastGaps[X]
                    LastGaps[X] = NewY + 1
                    Platform[NewY][X] = "O"
                    Platform[Y][X] = "."
                else:
                    LastGaps[X] = Y + 1
                    
            elif Current =="#":
                LastGaps[X] = Y + 1

    return list(Platform)

def GetLoad(Platform):
    Load = 0
    Height = len(Platform)
    for Y in range(Height):
        for X in range(len(Platform[0])):
            Current = Platform[Y][X]
            if Current == "O":
                Load += Height - Y
    return Load
                
                

def RotatePlatform(Platform):
    NewPlatform = []
    for OldX in range(len(Platform)):
        NewPlatform.append([])
        for OldY in range(len(Platform[0])-1,-1,-1):
            NewPlatform[-1].append(Platform[OldY][OldX])

    return NewPlatform

def Serialize(Platform):
    Flat = []
    for Row in Platform:
        for Rock in Row:
            Flat.append(Rock)
    return "".join(Flat)

Rocks = []
File = []

with open("Input.txt") as F:
    for L in F:
        File.append(list(L.strip()))




CycleHistory = []
previousResult = 0
Cycle = 0
PreviousDifference = 0
SpeedMode = False
LastLeg = False
RequiredCycles = 1000000000
while Cycle < RequiredCycles:
    for Rotation in range(4):
        File = FallUp(File)
        File = RotatePlatform(File)
    Load = GetLoad(File)
    if SpeedMode == False:
        Flat = Serialize(File)
        if Flat in CycleHistory[previousResult:]:
            SmallIndex = CycleHistory[previousResult:].index(Flat)
            NewDifference = Cycle-(SmallIndex+previousResult)
            previousResult = CycleHistory.index(Flat)

            if NewDifference == PreviousDifference:
                SpeedMode = True
                #print(NewDifference)
                print("Speed Mode Started")
            PreviousDifference = NewDifference
        CycleHistory.append(Flat)
    elif LastLeg == False:
        Remaining = (RequiredCycles) - Cycle
        RepeatsRemaining = int(Remaining // NewDifference)
        Cycle += (RepeatsRemaining-1) * NewDifference
        #print(Cycle)
        LastLeg = True
        continue
    

    
    Cycle += 1
    
    #if (Cycle) % 1000 == 0:
        #print(f"Cycle: {Cycle} Load: {Load}")

if len(File) < 20:
    for L in File:
        print("".join(L))

    
print(Load-1)
                





            
            
            
