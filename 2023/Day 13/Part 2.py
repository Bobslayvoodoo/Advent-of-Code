def FindReflectionLP(line,LPCandidates,OneOffLPCandidates):
    NewLPCandidates = []
    NewOneOffLPCandidates = []
    Combo = LPCandidates + OneOffLPCandidates
    #print(LPCandidates)
    #print(OneOffLPCandidates)
    for Num,OriginalLP in enumerate(Combo):
        #print(OriginalLP)
        DiffOnes = 0
        LP = OriginalLP
        RP = LP + 1
        Valid = True
        if Num > len(LPCandidates)-1:
            Valid = False
            DiffOnes += 1
        while LP >= 0 and RP < len(line):
            if line[LP] != line[RP]:
                Valid = False
                DiffOnes += 1
            
            
            LP -= 1
            RP += 1
        if Valid == True and OriginalLP >= 0 and OriginalLP < len(line)-1:
            NewLPCandidates.append(OriginalLP)
        elif DiffOnes == 1 and OriginalLP >= 0 and OriginalLP < len(line)-1:
            NewOneOffLPCandidates.append(OriginalLP)
    return list(NewLPCandidates),list(NewOneOffLPCandidates)





Horizontals = []
VerticalLPs = []
HorizontalUPs = []




with open("Input.txt") as file:
    LPCandidates = []
    Current = None
    OneOffLPs = []
    Rotated = []
    for line in file:
        if line == "\n": # new pattern
            if len(OneOffLPs) == 1:
                VerticalLPs.append(OneOffLPs[0])
            else:
                Horizontals.append(Rotated)
            Rotated = []
            LPCandidates = []
            OneOffLPs = []
            Current = None
        else: # same pattern
            line = line.strip()
            Rotated.append([])
            for X in line:
                Rotated[-1].append(X)
            if len(LPCandidates) == 0 and not Current:
                LPCandidates = list(range(len(line)))

            LPCandidates,OneOffLPs = FindReflectionLP(line,LPCandidates,OneOffLPs)
            
            if len(LPCandidates) == 0:
                Current = "H"
            
        
                

Horizontals.append(Rotated)

for Pattern in Horizontals:
    #print("-----------")
    LPCandidates = []
    OneOffLPs = []
    for X in range(len(Pattern[0])):
        line = []
        #print(" -- new line --")
        for Y in range(len(Pattern)):
            line.append(Pattern[Y][X])
        #print("".join(line))
        if X == 0:
            LPCandidates = list(range(len(line)))

        LPCandidates,OneOffLPs = FindReflectionLP(line,LPCandidates,OneOffLPs)

    if len(OneOffLPs) == 1:
        HorizontalUPs.append(OneOffLPs[0])
    #elif len(OneOffLPs) > 1:
        #print(OneOffLPs)
        #for L in Pattern:
            #print("".join(L))
        #print("----------------------------")

Total = 0
for LP in VerticalLPs:
    Total += LP + 1

for UP in HorizontalUPs:
    Total += 100 * (UP+1)

print(Total)
            
        
            
