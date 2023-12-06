Engine = []

def GetNeighboursCoords(Center):
    Neighbours = []
    for Coord in ((-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)):
        NewX = Center[0] + Coord[0]
        NewY = Center[1] + Coord[1]
        if NewX < 0 or NewY < 0:
            continue
        if NewX >= len(Engine[-1]) or NewY >= len(Engine):
            continue
        Neighbours.append((NewX,NewY))
    return Neighbours



with open("Input.txt") as file:
    for line in file:
        Engine.append([])
        for character in line.strip():
            Engine[-1].append(character)

Total = 0
for y,Row in enumerate(Engine):
    for x,Character in enumerate(Row):
        if not Character.isnumeric() and Character != ".":
            ##character is symbol
            PartNumbers = []
            PreviousSF = {y+1:[],
                          y:[],
                          y-1:[]}
            for Neigbour in GetNeighboursCoords((x,y)):
                CurX = Neigbour[0]
                CurY = Neigbour[1]
                
                Current = Engine[CurY][CurX]
                if Current.isnumeric():
                    S = Neigbour[0]
                    F = Neigbour[0]
                    while Current.isnumeric() and F < len(Row):
                        F += 1
                        Current = "".join(Engine[CurY][F:F+1])
                        
                    Current = Engine[CurY][CurX]
                    while Current.isnumeric() and S >= 0:
                        S -= 1
                        Current = Engine[CurY][S]
                    S += 1
                    if len(PreviousSF[CurY]) > 0 and S <= PreviousSF[CurY][0] and F >= PreviousSF[CurY][1]:
                        continue
                    PreviousSF[CurY] = [S,F]
                    #print(("".join(Engine[CurY][S:F])))
                    PartNumbers.append(int("".join(Engine[CurY][S:F])))
            Product = 0
            if Character == "*" and len(PartNumbers) == 2:
                Product = PartNumbers[0] * PartNumbers[1]
            #print(PartNumbers)
            Total += Product

print(Total)
                    
                    
