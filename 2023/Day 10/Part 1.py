Neighbours = {
    "|":((0,1),(0,-1)),
    "-":((1,0),(-1,0)),
    "L":((0,1),(1,0)),
    "J":((0,1),(-1,0)),
    "7":((0,-1),(-1,0)),
    "F":((0,-1),(1,0))
    }

class Pipe():
    def __init__(self,Shape,Position):
        self.Shape = Shape
        self.Position = Position
        self.Neighbours = []
        AllPipes[Position] = self
        
    def AssignNeighbours(self,System):
        if self.Shape == "S" or self.Shape == ".":
            return
        
        for Vector in Neighbours[self.Shape]:
            NewX = self.Position[0] + Vector[0]
            NewY = self.Position[1] - Vector[1]
            if NewX >= 0 and NewX < len(Network[0]) and NewY >= 0 and NewY < len(Network):
                NeighbourPipe = Network[NewY][NewX]
                Connected = False
                if NeighbourPipe.Shape == "S":
                    Connected = True
                    NeighbourPipe.Neighbours.append(self)
                    self.Neighbours.append(NeighbourPipe)
                    continue
                if NeighbourPipe.Shape == ".":
                    break
                for NVector in Neighbours[NeighbourPipe.Shape]:
                    if (NewX + NVector[0] == self.Position[0]) and (NewY - NVector[1] == self.Position[1]):
                        Connected = True
                        break

                if Connected == True:
                    self.Neighbours.append(NeighbourPipe)
            
def Dijkstra(StartPosition):
    Distances = dict()
    Unvisited = set()
    for CurrentPipe in AllPipes.values():
        Distances[CurrentPipe.Position] = float("inf")
        Unvisited.add(CurrentPipe)
    Distances[StartPosition] = 0

    while len(Unvisited) > 0:
        ClosestDistance = float("inf")
        for P in Unvisited:
            Position = P.Position
            if ClosestDistance >= Distances[Position]:
                ClosestDistance = Distances[Position]
                ClosestPipe = AllPipes[Position]
        if ClosestDistance == float("inf"):
            break
        
        Unvisited.discard(ClosestPipe)
        for NeigbourPipe in Unvisited:
            if NeigbourPipe in ClosestPipe.Neighbours:
                PossibleDistance = ClosestDistance + 1
                if PossibleDistance < Distances[NeigbourPipe.Position]:
                    Distances[NeigbourPipe.Position] = PossibleDistance
    return Distances
        


Network = []
AllPipes = dict()

with open("Input.txt") as file:
    for Y,line in enumerate(file):
        line = line.strip()
        Network.append([])
        for X,PipeShape in enumerate(line):
            if PipeShape == "S":
                StartPos = (X,Y)
            NewPipe = Pipe(PipeShape,(X,Y))
            Network[-1].append(NewPipe)

for Row in Network:
    for P in Row:
        P.AssignNeighbours(Network)

Dists = Dijkstra(StartPos)
Highest = 0
for Value in Dists.values():
    if Value > Highest and Value != float("inf"):
        Highest = Value

print(Highest)

##for Row in Network:
##    Out = ""
##    for P in Row:
##        if Dists[P.Position] == float("inf"):
##            Out += "."
##        else:
##            Out += str(Dists[P.Position])

##    print(Out)

