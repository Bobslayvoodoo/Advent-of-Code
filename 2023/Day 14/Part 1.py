LastGaps = []
TotalLoad = 0
File = []
with open("Input.txt") as F:
    for L in F:
        File.append(list(L.strip()))
        
Height = len(File)
for Y in range(len(File)):
    for X in range(len(File[0])):
        Current = File[Y][X]
        if len(LastGaps) <= X:
            LastGaps.append(0)
        if Current == "O":
            if LastGaps[X] < Y:
                NewY = LastGaps[X]
                LastGaps[X] = NewY + 1
                Load = Height - NewY
                File[NewY][X] = "O"
                File[Y][X] = "."
            else:
                Load = Height - Y
                LastGaps[X] = Y + 1
                
            TotalLoad += Load
        elif Current =="#":
            LastGaps[X] = Y + 1

if len(File) < 20:
    for L in File:
        print("".join(L))



print(TotalLoad)
            
            
            
