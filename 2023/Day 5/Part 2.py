with open("Input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        if line[0] == "seeds:":
            line = line[1:]
            x = 0
            CurrentBatch = []
            while x <= len(line)-2:
                RangeStart = int(line[x])
                RangeLength = int(line[x+1])
                SeedRange = (RangeStart,RangeLength)
                CurrentBatch.append(SeedRange)
                x += 2

            NextBatch = list(CurrentBatch)
        elif line[0].isnumeric():
            DestinationStart = int(line[0])
            SourceStart = int(line[1])
            RangeLength = int(line[2])
            SeedNum = 0
            while SeedNum < len(CurrentBatch):
                SeedRange = CurrentBatch[SeedNum]
                if SourceStart <= SeedRange[0] and SeedRange[0] + SeedRange[1] <= SourceStart + RangeLength:
                    # perfectly in range
                    #print(SeedRange,"all in")
                    Difference = SeedRange[0] - SourceStart
                    NewDestination = DestinationStart + Difference
                    NextBatch[SeedNum] = (NewDestination,SeedRange[1])
                elif SeedRange[0] < SourceStart and SeedRange[0] + SeedRange[1] <= SourceStart + RangeLength and SeedRange[0] + SeedRange[1] >= SourceStart:
                    #  lower half out of range
                    #print(SeedRange,"lower outside")
                    StartDifference = SourceStart - SeedRange[0]
                    NewLength = SeedRange[1] - StartDifference
                    NextBatch.append((DestinationStart,NewLength))
                    #left behind
                    NewLength = SourceStart - SeedRange[0]
                    CurrentBatch[SeedNum] = (SeedRange[0],NewLength)
                    NextBatch[SeedNum] = (SeedRange[0],NewLength)
                elif SourceStart <= SeedRange[0] and SourceStart + RangeLength < SeedRange[0] + SeedRange[1] and SeedRange[0] < SourceStart + RangeLength :
                    # upper half out of range
                    #print(SeedRange,"upper outside")
                    
                    Difference = SeedRange[0] - SourceStart
                    NewStart = DestinationStart + Difference
                    NewLength = (SourceStart+RangeLength)-SeedRange[0]
                    NextBatch.append((NewStart,NewLength))

                    #left behind
                    NewStart = (SourceStart+RangeLength)
                    NewLength = (SeedRange[0]+SeedRange[1]) - NewStart
                    CurrentBatch[SeedNum] = (NewStart,NewLength)
                    NextBatch[SeedNum] = (NewStart,NewLength)
                elif SeedRange[0] < SourceStart and SourceStart + RangeLength < SeedRange[0] + SeedRange[1]:
                    #print(SeedRange,"outside both")
                    # both lower and upper out of range
                    NextBatch.append((DestinationStart,RangeLength))
                    # lower left behind
                    NewLength = SourceStart - SeedRange[0]
                    CurrentBatch[SeedNum] = (SeedRange[0],NewLength)
                    NextBatch[SeedNum] = (SeedRange[0],NewLength)
                    # upper left behind
                    NewStart = (SourceStart+RangeLength)
                    NewLength = (SeedRange[0]+SeedRange[1]) - NewStart
                    CurrentBatch.append((NewStart,NewLength))
                    NextBatch.append((NewStart,NewLength))
                    
                    
                SeedNum += 1
                    
                    
                
        elif len(line)>1 and line[1] == "map:":
            #print("-----------------------\n")
            #print(line[0],NextBatch)
            CurrentBatch = list(set(NextBatch))
            NextBatch = list(CurrentBatch)
#print(NextBatch)
print(min(NextBatch)[0])

