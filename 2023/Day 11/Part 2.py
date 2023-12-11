Space = []
Galaxies = dict()
ExpansionAmount = 1000000

def FindDistanceToGalaxies(StartPosition,SpecialRows,SpecialColumns):
    Distances = dict()
    for Galaxy,Position in Galaxies.items():
        DeltaX = abs(StartPosition[0]-Position[0])
        DeltaY = abs(StartPosition[1]-Position[1])
        Distance =  DeltaX + DeltaY
        # X expansions
        R = list(range(min(StartPosition[0],Position[0]),max(StartPosition[0],Position[0])+1))
        Expansions = len(R+SpecialColumns) - len(set(R+SpecialColumns))
        Distance += Expansions * (ExpansionAmount-1)

        # Y expansions
        R = list(range(min(StartPosition[1],Position[1]),max(StartPosition[1],Position[1])+1))
        Expansions = len(R+SpecialRows) - len(set(R+SpecialRows))
        Distance += Expansions * (ExpansionAmount-1)
        Distances[Position] = Distance
    return Distances




GalaxyCount = 0
EmptyRows = []
EmptyColumns = []
ColumnCounts = []



with open("Input.txt") as file:
    for Y,line in enumerate(file):
        Space.append([])
        StartGCount = GalaxyCount
        for X,Part in enumerate(line.strip()):
            if len(ColumnCounts) <= X:
                ColumnCounts.append(0)
            if Part == "#":
                GalaxyCount += 1
                ColumnCounts[X] += 1
                Space[-1].append(str(GalaxyCount))
                Galaxies[str(GalaxyCount)] = (X,Y)
            else:
                Space[-1].append(".")
        if StartGCount == GalaxyCount:
            EmptyRows.append(Y)

    for X,Count in enumerate(ColumnCounts):
        if Count == 0:
            EmptyColumns.append(X)

#print(EmptyColumns)
#print(EmptyRows)
#for Y in Space:
#    print("".join(Y))

Total = 0
for Number,Position in Galaxies.items():
    Distances = FindDistanceToGalaxies(Position,EmptyRows,EmptyColumns)
    for Num,Pos in Galaxies.items():
        if Num >= Number:
            Dist = Distances[Pos]
            Total += Dist
            #print(f"{Number} to {Num} is {Dist}")

print(Total)
        
    

        
            
