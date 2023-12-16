class Node():
    def __init__(self,Name,Left,Right):
        self.Name = Name
        self.Left = Left
        self.Right = Right
import math
def FindPrimeFactors(Number):
    Primes = []
    while Number%2 == 0:
        Primes.append(int(Number/2))
        Number = int(Number / 2)

    for i in range(3,int(math.sqrt(Number))+1):
        while Number % i == 0:
            Primes.append(i)
            Number = int(Number/i)

    Primes.append(Number)
    print(Primes)
    return Primes




Network = dict()
with open("Input.txt") as File:
    for Row,Line in enumerate(File):
        if Row == 0:
            Directions = Line.strip()
        elif Row >= 2:
            Line = Line.strip().split("=")
            Key = Line[0].strip()
            D = Line[1][2:-1].split(",")
            Left = D[0].strip()
            Right = D[1].strip()
            NewNode = Node(Key,Left,Right)
            Network[Key] = NewNode
CurrentNodes = []
TimesSinceLastWin = []
for N in Network.values():
    if N.Name[2] == "A":
        CurrentNodes.append(N)
        TimesSinceLastWin.append([2])
    N.Left = Network[N.Left]
    N.Right = Network[N.Right]

CompleteCycle = {}
for N in Network.values():
    CurrentNode = N
    for Direct in Directions:
        if Direct == "L":
            CurrentNode = CurrentNode.Left
        elif Direct == "R":
            CurrentNode = CurrentNode.Right
        else:
            print("Something has gone wrong")

    CompleteCycle[N.Name] = CurrentNode

        


Steps = 0
TotalProduct = 1
Offset = 0
Finished = False
WinningSteps = []
while Finished == False:
    Finished = True
    CurrentHighestMultiple = 0
    
            
    if len(CurrentNodes) == 0:
        for W in WinningSteps:
            if W[0] > CurrentHighestMultiple:
                CurrentHighestMultiple = W[0]
                CHmod = W[1]

    #if Steps > 10000000:
        #print(Steps)
    if len(CurrentNodes) == 0:
        break
    Steps += 1
    Dnum = (Steps-1) % len(Directions)
    Direction = Directions[Dnum]

           
    CurrentNodeNumber = 0
    for Win in WinningSteps:
        if Steps%Win[0] != Win[1]:
            Finished = False
    while CurrentNodeNumber < len(CurrentNodes):
        CurrentNode = CurrentNodes[CurrentNodeNumber]
        if Direction == "L":
            CurrentNodes[CurrentNodeNumber] = CurrentNode.Left
        elif Direction == "R":
            CurrentNodes[CurrentNodeNumber] = CurrentNode.Right
        else:
            print("Something has gone wrong")
        if CurrentNodes[CurrentNodeNumber].Name[2] != "Z":
            Finished = False
            TimesSinceLastWin[CurrentNodeNumber][-1] += 1
        else:
            if len(TimesSinceLastWin[CurrentNodeNumber]) > 10:
                TimesSinceLastWin[CurrentNodeNumber].pop(0)
            if len(set(TimesSinceLastWin[CurrentNodeNumber])) == 1 and len(TimesSinceLastWin[CurrentNodeNumber]) > 9:
                Multiple = TimesSinceLastWin[CurrentNodeNumber][-1]
                WinningSteps.append((Multiple,Steps%Multiple))
                print(CurrentNodes[CurrentNodeNumber].Name,Multiple,Steps,Steps%Multiple)
                CurrentNodes.pop(CurrentNodeNumber)
                
                continue
            TimesSinceLastWin[CurrentNodeNumber].append(1)

        
        CurrentNodeNumber += 1

if len(CurrentNodes) == 0:
    AllPrimes = dict()
    for W in WinningSteps:
        CurrentPrimes = dict()
        for P in FindPrimeFactors(W[0]):
            if P in CurrentPrimes:
                CurrentPrimes[P] += 1
            else:
                CurrentPrimes[P] = 1

        for P,Num in CurrentPrimes.items():
            if P in AllPrimes:
                if Num > AllPrimes[P]:
                    AllPrimes[P] = Num
            else:
                AllPrimes[P] = Num
                
    Steps = 1
    for P,num in AllPrimes.items():
        Steps *= (P**num)

print(Steps)   
            
