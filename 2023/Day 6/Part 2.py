def MidPoint(Start,End):
    Mid = int(Start + (End-Start)//2)
    return Mid

Times = []
Distances = []

with open("Input.txt") as file:
    for line in file:
        line = line.strip().split(":")
        if line[0] == "Time":
            for time in line[1].strip().split(" "):
                if time.isnumeric():
                    Times.append(time)
            Time = int("".join(Times))
        elif line[0] == "Distance":
            for Dist in line[1].strip().split(" "):
                if Dist.isnumeric():
                    Distances.append(Dist)
            Record = int("".join(Distances))


def RaceWinCheck(HoldTime,TotalTime=Time,Record=Record):
    DistanceTravelled = HoldTime * (TotalTime-HoldTime)
    if HoldTime < 1:
        return False
    if DistanceTravelled > Record:
        return True
    else:
        return False
            

## binary search kinda thing?

Found = False
CurrentHoldTime = int(Time//2)
CurrentLower = 0
CurrentUpper = Time
while not Found: ## lower bound

    if RaceWinCheck(CurrentHoldTime) and not RaceWinCheck(CurrentHoldTime-1):
        LowerBound = CurrentHoldTime
        Found = True
        break
    if RaceWinCheck(CurrentHoldTime): # must be to the left
        CurrentUpper = CurrentHoldTime
        CurrentHoldTime = MidPoint(CurrentLower,CurrentUpper)
    else: # must be to the right
        CurrentLower = CurrentHoldTime
        CurrentHoldTime = MidPoint(CurrentLower,CurrentUpper)


CurrentHoldTime = int(Time+(Time//2))
CurrentLower = 0
CurrentUpper = Time
Found = False
while not Found: ## upper bound
    if RaceWinCheck(CurrentHoldTime) and not RaceWinCheck(CurrentHoldTime+1):
        UpperBound = CurrentHoldTime
        Found = True
        break
    if RaceWinCheck(CurrentHoldTime):
        CurrentLower = CurrentHoldTime
        CurrentHoldTime = MidPoint(CurrentLower,CurrentUpper)
    else:
        CurrentUpper = CurrentHoldTime
        CurrentHoldTime = MidPoint(CurrentLower,CurrentUpper)


#print(LowerBound)
#print(UpperBound)
FinalTotal = 1+UpperBound - LowerBound


print(FinalTotal)

