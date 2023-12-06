with open("Input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        if line[0] == "seeds:":
            CurrentBatch = line[1:]
            NextBatch = list(CurrentBatch)
        elif line[0].isnumeric():
            DestinationStart = int(line[0])
            SourceStart = int(line[1])
            RangeLength = int(line[2])
            
            for SeedNum in range(len(CurrentBatch)):
                Difference = int(CurrentBatch[SeedNum]) - SourceStart
                if Difference >= 0 and Difference < RangeLength:
                    NextBatch[SeedNum] = DestinationStart + Difference
        elif len(line)>1 and line[1] == "map:":
            CurrentBatch = list(NextBatch)
            NextBatch = list(CurrentBatch)
print(min(NextBatch))

