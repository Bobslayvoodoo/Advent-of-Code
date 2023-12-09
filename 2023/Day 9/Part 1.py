def DifferenceFinder(In):
    Out = []
    for N in range(1,len(In)):
        Out.append(int(In[N])-int(In[N-1]))

    return Out
        
Total = 0
with open("Input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        Layers = [line]
        CurrentLayer = line
        CurrentLayerNum = 0
        while len(set(CurrentLayer)) > 1:
            CurrentLayer = Layers[CurrentLayerNum]
            Layers.append(DifferenceFinder(CurrentLayer))
            CurrentLayerNum += 1
        
        while CurrentLayerNum > 0:
            CurrentLayerNum -= 1
            CurrentLayer = Layers[CurrentLayerNum]
            CurrentLayer.append(int(CurrentLayer[-1])+Layers[CurrentLayerNum+1][-1])
        Total += CurrentLayer[-1]        



print(Total)
