def FindReflectionLP(line,LPCandidates):
    NewLPCandidates = []
    for OriginalLP in LPCandidates:
        
        LP = OriginalLP
        RP = LP + 1
        Valid = True
        while LP >= 0 and RP < len(line):
            if line[LP] != line[RP]:
                Valid = False
                break
            
            
            LP -= 1
            RP += 1
        if Valid == True and OriginalLP >= 0 and OriginalLP < len(line)-1:
            NewLPCandidates.append(OriginalLP)
    return NewLPCandidates





Horizontals = []
VerticalLPs = []
HorizontalUPs = []




with open("Input.txt") as file:
    LPCandidates = []
    Current = None
    Rotated = []
    for line in file:
        if line == "\n": # new pattern
            
            if Current != "H":
                VerticalLPs.append(LPCandidates[0])
            else:
                Horizontals.append(Rotated)
            Rotated = []
            LPCandidates = []
            Current = None
        else: # same pattern
            line = line.strip()
            Rotated.append([])
            for X in line:
                Rotated[-1].append(X)
            if len(LPCandidates) == 0 and not Current:
                LPCandidates = list(range(len(line)))

            LPCandidates = list(FindReflectionLP(line,LPCandidates))
            
            if len(LPCandidates) == 0:
                Current = "H"
        
                
if Current != "H": # for the last one
    VerticalLPs.append(LPCandidates[0])
else:
    Horizontals.append(Rotated)


for Pattern in Horizontals:
    LPCandidates = []
    for X in range(len(Pattern[0])):
        line = []
        for Y in range(len(Pattern)):
            line.append(Pattern[Y][X])
        #print("".join(line))
        if len(LPCandidates) == 0:
            LPCandidates = list(range(len(line)))

        LPCandidates = list(FindReflectionLP(line,LPCandidates))

    HorizontalUPs.append(LPCandidates[0])

Total = 0
for LP in VerticalLPs:
    Total += LP + 1

for UP in HorizontalUPs:
    Total += 100 * (UP+1)

print(Total)
            
        
            
