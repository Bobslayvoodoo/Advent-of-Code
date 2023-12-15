Total = 0

with open("Input.txt") as File:
    for Line in File:
        Data = Line.strip().split(" ")
        Springs = Data[0]
        Groups = Data[1].split(",")
        NumberUnknowns = Springs.count("?")
        Permutations = (2**NumberUnknowns)-2
        CurrentNumber = 0
        CurrentTotal = 0
        #print("-------------------------")
        while CurrentNumber <= Permutations+1:
            Arrangement = list(bin(CurrentNumber))[2:]
            if len(Arrangement) <= NumberUnknowns:
                Arrangement = ["0" for n in range((NumberUnknowns)-len(Arrangement))] + Arrangement
            Arrangement = "".join(Arrangement)
            Arrangement = Arrangement.replace("0",".")
            Arrangement = Arrangement.replace("1","#")
            N = 0
            Gnum = 0
            ContinuousCount = 0
            #NewA = []
            for RealN,Character in enumerate(Springs):
                if Character == "?":
                    Character = Arrangement[N]
                    N += 1
                if Character == "#":
                    #NewA.append(Character)
                    ContinuousCount += 1
                    if Gnum < len(Groups) and int(Groups[Gnum]) < ContinuousCount:
                       break
                elif Character == ".":
                    #NewA.append(Character)
                    if ContinuousCount > 0:
                        if Gnum < len(Groups) and ContinuousCount != int(Groups[Gnum]):
                            break
                        ContinuousCount = 0
                        Gnum += 1
                        if Gnum > len(Groups):
                            break
                    
            else:
                if Character == "." and Gnum == len(Groups):
                    CurrentTotal += 1
                    #print("".join(NewA))
                elif Character == "#" and Gnum == len(Groups)-1:
                    if ContinuousCount == int(Groups[Gnum]):
                        CurrentTotal += 1
                        #print("".join(NewA))
                        
                        

            CurrentNumber += 1
        #print(CurrentTotal)
        Total += CurrentTotal

print(Total)
        
