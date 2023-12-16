class Beam():
    def __init__(self,X,Y,DX,DY):
        self.X = X
        self.Y = Y
        self.DX = DX
        self.DY = DY


Grid = []
EnergisedGrid = []
with open("Input.txt") as File:
    for Line in File:
        Line = Line.strip()
        Grid.append(list(Line))
        EnergisedGrid.append(["." for n in range(len(Line))])




Beams = [Beam(-1,0,1,0)]
TotalEnergised = 0
AllHistory = []
while len(Beams) > 0:
    BeamNumber = 0
    while BeamNumber < len(Beams):
        CurrentBeam = Beams[BeamNumber]
        if CurrentBeam.X >= 0:
            if EnergisedGrid[CurrentBeam.Y][CurrentBeam.X] == ".":
                TotalEnergised += 1
                EnergisedGrid[CurrentBeam.Y][CurrentBeam.X] = "#"

        NewX = CurrentBeam.X + CurrentBeam.DX
        NewY = CurrentBeam.Y + CurrentBeam.DY
        
        if NewX < 0 or NewX >= len(Grid[0]) or NewY < 0 or NewY >= len(Grid):
            Beams.pop(BeamNumber)
            continue
        
        Stamp = ((CurrentBeam.X,CurrentBeam.Y),(CurrentBeam.DX,CurrentBeam.DY))
        if Stamp in AllHistory:
            Beams.pop(BeamNumber)
            continue
        else:
            AllHistory.append(Stamp)
            
        CurrentBeam.X = NewX
        CurrentBeam.Y = NewY
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


print(TotalEnergised)


        
    
