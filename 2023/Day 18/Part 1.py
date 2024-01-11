def FloodCount(Layer):
    TrenchCount = 0
    for Y,Row in enumerate(Layer):
        LineCount = 0
        for X,Ground in enumerate(Row):
            if Ground == "#":
                TrenchCount += 1
                if Y > 0 and Y+1<len(Layer):
                    if Layer[Y-1][X] == "#" and Layer[Y+1][X] == "#":
                        LineCount += 1
                    elif Layer[Y-1][X] == "#":
                        LineCount += 1
                elif Y == len(Layer)-1:
                    if Layer[Y-1][X] == "#":
                        LineCount += 1
                    
                    
            else:
                if LineCount % 2 == 1:
                    TrenchCount += 1
    return TrenchCount
with open("Input.txt") as File:
    CX = 0
    CY = 0
    MaxX = 0
    MaxY = 0
    MinX = 0
    MinY = 0
    for Line in File:
        Line = Line.strip().split(" ")
        if Line[0] == "R":
            CX += int(Line[1])
        elif Line[0] == "L":
            CX -= int(Line[1])
        elif Line[0] == "D":
            CY += int(Line[1])
        elif Line[0] == "U":
            CY -= int(Line[1])
        if CX > MaxX:
            MaxX = CX
        elif CX < MinX:
            MinX = CX
        if CY > MaxY:
            MaxY = CY
        elif CY < MinY:
            MinY = CY
            
CurrentLayer = []
MaxY += 1
MaxX += 1
for Y in range(MaxY-MinY):
    CurrentLayer.append(["." for n in range(MaxX-MinX)])


with open("Input.txt") as File:
    
    CurrentX = -MinX
    CurrentY = -MinY
    for Line in File:
        Data = Line.strip().split(" ")
        Length = int(Data[1])
        if Data[0] == "R":
            while CurrentX < len(CurrentLayer[CurrentY]) and Length > 0:
                Length -= 1
                CurrentX += 1
                CurrentLayer[CurrentY][CurrentX] = "#" 
        elif Data[0] == "L":
            while CurrentX > 0 and Length > 0:
                Length -= 1
                CurrentX -= 1
                CurrentLayer[CurrentY][CurrentX] = "#"
            if CurrentX < 0:
                print("I did not plan for this")
                
        elif Data[0] == "U":
            while CurrentY > 0 and Length > 0:
                Length -= 1
                CurrentY -= 1
                CurrentLayer[CurrentY][CurrentX] = "#"
            if CurrentX < 0:
                print("I did not plan for this")
        elif Data[0] == "D":
            while CurrentY < len(CurrentLayer)-1 and Length > 0:
                Length -= 1
                CurrentY += 1
                CurrentLayer[CurrentY][CurrentX] = "#"


LongestRow = 0
for L in CurrentLayer:
    if len(L) > LongestRow:
        LongestRow = len(L)

for Y,L in enumerate(CurrentLayer):
    if len(L) < LongestRow:
        for i in range(LongestRow-len(CurrentLayer[Y])):
            CurrentLayer[Y].append(".")
        
    

    if len(L) < 10:
        print("".join(L))
print(FloodCount(CurrentLayer))
