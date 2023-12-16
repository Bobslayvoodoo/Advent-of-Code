class Beam():
    def __init__(self,X,Y,DX,DY):
        self.X = X
        self.Y = Y
        self.DX = DX
        self.DY = DY


Grid = []

with open("Input.txt") as File:
    for Line in File:
        Line = Line.strip()
        Grid.append(list(Line))




BestEnergised = 0


StartBeams = []
for X in range(len(Grid[0])):
    StartBeams.append(Beam(X,-1,0,1))
    StartBeams.append(Beam(X,len(Grid),0,-1))

for Y in range(len(Grid)):
    StartBeams.append(Beam(-1,Y,1,0))
    StartBeams.append(Beam(len(Grid),Y,-1,0))


    
for n,StartBeam in enumerate(StartBeams):
    print(f"{n} out of {len(StartBeams)}")
    StartX,StartY = StartBeam.X,StartBeam.Y
    EnergisedGrid = []
    AllHistory = []
    for Line in Grid:
        EnergisedGrid.append(["." for n in range(len(Line))])
    Beams = [StartBeam]
    TotalEnergised = 0
    while len(Beams) > 0:
        BeamNumber = 0
        while BeamNumber < len(Beams):
            CurrentBeam = Beams[BeamNumber]
            if CurrentBeam.X >= 0 and CurrentBeam.X < len(Grid[0]) and CurrentBeam.Y >= 0 and CurrentBeam.Y < len(Grid):
                if EnergisedGrid[CurrentBeam.Y][CurrentBeam.X] == ".":
                    TotalEnergised += 1
                    EnergisedGrid[CurrentBeam.Y][CurrentBeam.X] = "#"

            NewX = CurrentBeam.X + CurrentBeam.DX
            NewY = CurrentBeam.Y + CurrentBeam.DY
            if NewX < 0 or NewX >= len(Grid[0]) or NewY < 0 or NewY >= len(Grid):
                Beams.pop(BeamNumber)
                continue
            
            
                
            CurrentBeam.X = NewX
            CurrentBeam.Y = NewY
            Stamp = ((CurrentBeam.X,CurrentBeam.Y),(CurrentBeam.DX,CurrentBeam.DY))
            if Stamp in AllHistory:
                Beams.pop(BeamNumber)
                continue
            else:
                AllHistory.append(Stamp)
            Mirror = Grid[CurrentBeam.Y][CurrentBeam.X]
            if (CurrentBeam.DX == 1 and Mirror == "/") or (CurrentBeam.DX == -1 and Mirror == "\\"):
                CurrentBeam.DX = 0
                CurrentBeam.DY = -1
            elif (CurrentBeam.DX == -1 and Mirror == "/") or (CurrentBeam.DX == 1 and Mirror == "\\"):
                CurrentBeam.DX = 0
                CurrentBeam.DY = 1
            elif (CurrentBeam.DY == 1 and Mirror == "/") or (CurrentBeam.DY == -1 and Mirror == "\\"):
                CurrentBeam.DX = -1
                CurrentBeam.DY = 0
            elif (CurrentBeam.DY == -1 and Mirror == "/") or (CurrentBeam.DY == 1 and Mirror == "\\"):
                CurrentBeam.DX = 1
                CurrentBeam.DY = 0
            elif CurrentBeam.DX != 0 and Mirror == "|":
                NewBeam = Beam(CurrentBeam.X,CurrentBeam.Y,0,1)
                Beams.append(NewBeam)
                CurrentBeam.DX = 0
                CurrentBeam.DY = -1
            elif CurrentBeam.DY != 0 and Mirror == "-":
                NewBeam = Beam(CurrentBeam.X,CurrentBeam.Y,1,0)
                Beams.append(NewBeam)
                CurrentBeam.DX = -1
                CurrentBeam.DY = 0

            BeamNumber += 1
    if TotalEnergised > BestEnergised:
        BestEnergised = TotalEnergised

print(BestEnergised)

        
    
